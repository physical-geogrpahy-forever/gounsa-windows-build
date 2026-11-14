using System;
using System.Globalization;
using System.IO;
using System.Reflection;
using System.Windows.Forms;
using LORICA4;

// Independent controlled sensitivity test invoking the real LORICA
// calculate_sediment_dynamics() function, not merely the coefficient helper.
// Each scenario constructs a fresh identical soil/DEM state.
// Deliberately no TREED Julia run: FPC is the mean effective first-year FPC
// measured from the verified v1.1 artifact (0.728597).
public static class LoricaFpcDirectTest
{
    static readonly BindingFlags Instance = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
    static readonly BindingFlags Static = BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
    static string root;

    static void Set(Mother_form f, string name, object value)
    {
        var field = f.GetType().GetField(name, Instance);
        if (field == null) throw new MissingFieldException(f.GetType().FullName, name);
        field.SetValue(f, value);
    }

    static T Get<T>(Mother_form f, string name)
    {
        var field = f.GetType().GetField(name, Instance);
        if (field == null) throw new MissingFieldException(f.GetType().FullName, name);
        return (T)field.GetValue(f);
    }

    static object Invoke(object o, string method, params object[] args)
    {
        var m = o.GetType().GetMethod(method, Instance);
        if (m == null) throw new MissingMethodException(o.GetType().FullName, method);
        return m.Invoke(o, args);
    }

    static object InvokeRunner(string method, params object[] args)
    {
        var m = typeof(LoricaTreedThirtyYear).GetMethod(method, Static);
        if (m == null) throw new MissingMethodException("LoricaTreedThirtyYear", method);
        return m.Invoke(null, args);
    }

    static double ErosionKg(double beta, double fpc, double k, bool cellKOverride, out double transportedKg)
    {
        string dir = Path.Combine(root, "case_" + Directory.GetDirectories(root).Length.ToString("D2", CultureInfo.InvariantCulture));
        Directory.CreateDirectory(dir);
        using (Mother_form f = (Mother_form)InvokeRunner("BuildConvergentCase", dir, 1, false))
        {
            const int sourceRow = 1, sourceCol = 1, targetRow = 1, targetCol = 2;
            Set(f, "K_fac", new double[5,5]);
            Set(f, "bio_protection", new double[5,5]);
            Set(f, "aridity_vegetation", new double[5,5]);
            Set(f, "advection_erodibility", k);
            Set(f, "bio_protection_configured", beta);
            Set(f, "m", 0.5);
            Set(f, "n", 1.0);
            Set(f, "dh", 1.0);
            Set(f, "erodibility_value_m", k);
            Set(f, "erosion_threshold_kg", 0.0);
            Set(f, "rock_protection_constant", 0.0);
            Set(f, "constant_selective_transcap", 0.0);
            Set(f, "upper_particle_size", new double[] {0.01, 0.002, 0.00005, 0.000002, 0.0000001});
            Get<CheckBox>(f,"daily_water").Checked = true;
            Get<CheckBox>(f,"version_lux_checkbox").Checked = false;
            Get<CheckBox>(f,"OSL_checkbox").Checked = false;
            Get<CheckBox>(f,"CN_checkbox").Checked = false;
            Get<double[,]>(f,"aridity_vegetation")[sourceRow,sourceCol] = fpc;
            if (cellKOverride) Get<double[,]>(f,"K_fac")[sourceRow,sourceCol] = k * 2.0;
            double before = (double)InvokeRunner("SoilMassAt", f, sourceRow, sourceCol);
            // The actual source-cell erosion routine, with a positive transport
            // capacity and an initially empty sediment-in-transport array.
            Invoke(f, "calculate_sediment_dynamics", sourceRow, sourceCol, 0, 1, 0.1, 1.0, 1.0);
            double after = (double)InvokeRunner("SoilMassAt", f, sourceRow, sourceCol);
            var trans = Get<double[,,]>(f,"sediment_in_transport_kg");
            transportedKg = 0.0;
            for (int s=0;s<5;s++) transportedKg += trans[targetRow,targetCol,s];
            double loss = before - after;
            if (!(loss>0.0) || Double.IsNaN(loss)) throw new Exception("No actual positive sediment erosion");
            if (Math.Abs(loss - transportedKg) > 1e-7)
                throw new Exception("Eroded mineral mass does not equal routed mineral mass: " + loss + " vs " + transportedKg);
            return loss;
        }
    }

    static void Close(double actual, double expected, string label, double relTol=1e-6)
    {
        if (Math.Abs(actual - expected) > relTol * Math.Max(1.0, Math.Abs(expected)))
            throw new Exception(label + ": actual=" + actual.ToString("R",CultureInfo.InvariantCulture)
                + " expected=" + expected.ToString("R",CultureInfo.InvariantCulture));
    }

    [STAThread]
    public static void Main(string[] args)
    {
        root = Path.GetFullPath(args.Length>0 ? args[0] : "fpc_direct_test");
        Directory.CreateDirectory(root);
        const double fpc = 0.728597;
        const double k=0.0001;
        double t0,tBare,t1,t2,tK2;
        double e0=ErosionKg(0.0,fpc,k,false,out t0);
        double bare=ErosionKg(1.0,0.0,k,false,out tBare);
        double e1=ErosionKg(1.0,fpc,k,false,out t1);
        double e2=ErosionKg(2.0,fpc,k,false,out t2);
        double doubled=ErosionKg(0.0,fpc,k,true,out tK2);
        Close(bare,e0,"Bare soil must give baseline soil erosion");
        Close(e1/e0,Math.Exp(-fpc),"Erosion response beta=1",1e-6);
        Close(e2/e0,Math.Exp(-2*fpc),"Erosion response beta=2",1e-6);
        Close(doubled/e0,2.0,"Local K response",1e-6);
        string csv = "case,beta,FPC,sourceK,erosion_kg,transport_kg,ratio_to_beta0\n"
            +"beta0,0,"+fpc+","+k+","+e0+","+t0+",1\n"
            +"FPC0,1,0,"+k+","+bare+","+tBare+","+(bare/e0)+"\n"
            +"beta1,1,"+fpc+","+k+","+e1+","+t1+","+(e1/e0)+"\n"
            +"beta2,2,"+fpc+","+k+","+e2+","+t2+","+(e2/e0)+"\n"
            +"K2,0,"+fpc+","+(2*k)+","+doubled+","+tK2+","+(doubled/e0)+"\n";
        File.WriteAllText(Path.Combine(root,"fpc_direct_sensitivity.csv"),csv);
        Console.WriteLine(csv);
        Console.WriteLine("LORICA_V11_ACTUAL_SEDIMENT_FPC_SENSITIVITY_PASS");
    }
}
