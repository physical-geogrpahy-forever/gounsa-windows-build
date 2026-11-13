using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Globalization;
using System.Text;
using System.Reflection;
using System.Threading.Tasks;
using System.Windows.Forms;
using LORICA4;

public static class LoricaTreedLandslideSmoke
{
    static string OutputRoot;
    static readonly BindingFlags BF = BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public;

    static FieldInfo Field(object o, string name)
    {
        FieldInfo f = o.GetType().GetField(name, BF);
        if (f == null) throw new MissingFieldException(o.GetType().FullName, name);
        return f;
    }

    static void Set(object o, string name, object value)
    {
        Field(o, name).SetValue(o, value);
    }

    static T Get<T>(object o, string name)
    {
        return (T)Field(o, name).GetValue(o);
    }

    static void Call(object o, string name, params object[] args)
    {
        MethodInfo m = o.GetType().GetMethod(name, BF);
        if (m == null) throw new MissingMethodException(o.GetType().FullName, name);
        m.Invoke(o, args);
    }

    static double CallDouble(object o, string name, params object[] args)
    {
        MethodInfo m = o.GetType().GetMethod(name, BF);
        if (m == null) throw new MissingMethodException(o.GetType().FullName, name);
        return Convert.ToDouble(m.Invoke(o, args), CultureInfo.InvariantCulture);
    }

    static double SumAbs(double[,] a)
    {
        double s = 0.0;
        for (int r = 0; r < a.GetLength(0); r++)
        for (int c = 0; c < a.GetLength(1); c++)
            s += Math.Abs(a[r, c]);
        return s;
    }

    static double TotalSoilMass(Mother_form f)
    {
        double[,,,] tex = Get<double[,,,]>(f, "texture_kg");
        double[,,] y = Get<double[,,]>(f, "young_SOM_kg");
        double[,,] o = Get<double[,,]>(f, "old_SOM_kg");
        double total = 0.0;
        for (int r = 0; r < tex.GetLength(0); r++)
        for (int c = 0; c < tex.GetLength(1); c++)
        for (int l = 0; l < tex.GetLength(2); l++)
        {
            for (int k = 0; k < tex.GetLength(3); k++) total += tex[r,c,l,k];
            total += y[r,c,l] + o[r,c,l];
        }
        return total;
    }

    static double TotalTransportMass(Mother_form f)
    {
        double[,,] sed = Get<double[,,]>(f, "sediment_in_transport_kg");
        double[,] y = Get<double[,]>(f, "young_SOM_in_transport_kg");
        double[,] o = Get<double[,]>(f, "old_SOM_in_transport_kg");
        double[,,,] lay = Get<double[,,,]>(f, "lay_sediment_in_transport_kg");
        double[,,] ly = Get<double[,,]>(f, "lay_young_SOM_in_transport_kg");
        double[,,] lo = Get<double[,,]>(f, "lay_old_SOM_in_transport_kg");
        double total = 0.0;
        foreach (double v in sed) total += v;
        foreach (double v in y) total += v;
        foreach (double v in o) total += v;
        foreach (double v in lay) total += v;
        foreach (double v in ly) total += v;
        foreach (double v in lo) total += v;
        return total;
    }

    static double TotalTransientWaterTransportMassAtBoundary(Mother_form f)
    {
        double[,,] sed = Get<double[,,]>(f, "sediment_in_transport_kg");
        double[,] y = Get<double[,]>(f, "young_SOM_in_transport_kg");
        double[,] o = Get<double[,]>(f, "old_SOM_in_transport_kg");
        int nr = sed.GetLength(0), nc = sed.GetLength(1);
        double total = 0.0;
        for (int r = 0; r < nr; r++)
        for (int col = 0; col < nc; col++)
        {
            if (r != 0 && col != 0 && r != nr - 1 && col != nc - 1) continue;
            total += y[r,col] + o[r,col];
            for (int k = 0; k < sed.GetLength(2); k++) total += sed[r,col,k];
        }
        return total;
    }

    static double TotalPersistentLandslideMass(Mother_form f)
    {
        // v0.9 stores landslide residuals in layer-resolved arrays for both
        // mixing modes. Mixed arrays are transient and reused by water erosion.
        double[,,,] lay = Get<double[,,,]>(f, "lay_sediment_in_transport_kg");
        double[,,] ly = Get<double[,,]>(f, "lay_young_SOM_in_transport_kg");
        double[,,] lo = Get<double[,,]>(f, "lay_old_SOM_in_transport_kg");
        double total = 0.0;
        foreach (double v in lay) total += v;
        foreach (double v in ly) total += v;
        foreach (double v in lo) total += v;
        return total;
    }

    static double SoilMassAt(Mother_form f, int r, int c)
    {
        double[,,,] tex = Get<double[,,,]>(f, "texture_kg");
        double[,,] y = Get<double[,,]>(f, "young_SOM_kg");
        double[,,] o = Get<double[,,]>(f, "old_SOM_kg");
        double total = 0.0;
        for (int l = 0; l < tex.GetLength(2); l++)
        {
            for (int k = 0; k < tex.GetLength(3); k++) total += tex[r,c,l,k];
            total += y[r,c,l] + o[r,c,l];
        }
        return total;
    }

    static double TransportMassAt(Mother_form f, int r, int c)
    {
        double[,,] sed = Get<double[,,]>(f, "sediment_in_transport_kg");
        double[,] y = Get<double[,]>(f, "young_SOM_in_transport_kg");
        double[,] o = Get<double[,]>(f, "old_SOM_in_transport_kg");
        double[,,,] lay = Get<double[,,,]>(f, "lay_sediment_in_transport_kg");
        double[,,] ly = Get<double[,,]>(f, "lay_young_SOM_in_transport_kg");
        double[,,] lo = Get<double[,,]>(f, "lay_old_SOM_in_transport_kg");
        double total = y[r,c] + o[r,c];
        for (int k = 0; k < sed.GetLength(2); k++) total += sed[r,c,k];
        for (int l = 0; l < lay.GetLength(2); l++)
        {
            for (int k = 0; k < lay.GetLength(3); k++) total += lay[r,c,l,k];
            total += ly[r,c,l] + lo[r,c,l];
        }
        return total;
    }

    static string F(double value)
    {
        return value.ToString("R", CultureInfo.InvariantCulture);
    }

    static double[,] ReadAsciiGrid(string path)
    {
        string[] lines = File.ReadAllLines(path);
        if (lines.Length < 7) throw new Exception("Invalid ESRI ASCII raster: " + path);
        string[] h0 = lines[0].Split((char[])null, StringSplitOptions.RemoveEmptyEntries);
        string[] h1 = lines[1].Split((char[])null, StringSplitOptions.RemoveEmptyEntries);
        int nc = Int32.Parse(h0[1], CultureInfo.InvariantCulture);
        int nr = Int32.Parse(h1[1], CultureInfo.InvariantCulture);
        if (lines.Length < 6 + nr) throw new Exception("Truncated ESRI ASCII raster: " + path);
        double[,] a = new double[nr,nc];
        for (int r = 0; r < nr; r++)
        {
            string[] p = lines[6 + r].Split((char[])null, StringSplitOptions.RemoveEmptyEntries);
            if (p.Length != nc) throw new Exception("ESRI ASCII column count mismatch: " + path);
            for (int col = 0; col < nc; col++)
                a[r,col] = Double.Parse(p[col], CultureInfo.InvariantCulture);
        }
        return a;
    }

    static void WriteAscii(string path, double[,] grid)
    {
        int nr = grid.GetLength(0);
        int nc = grid.GetLength(1);
        StringBuilder sb = new StringBuilder();
        sb.AppendLine("ncols         " + nc);
        sb.AppendLine("nrows         " + nr);
        sb.AppendLine("xllcorner     0");
        sb.AppendLine("yllcorner     0");
        sb.AppendLine("cellsize      10");
        sb.AppendLine("NODATA_value  -9999");
        for (int r = 0; r < nr; r++)
        {
            for (int c = 0; c < nc; c++)
            {
                if (c > 0) sb.Append(' ');
                double v = grid[r,c];
                sb.Append(Double.IsNaN(v) || Double.IsInfinity(v) ? "-9999" : F(v));
            }
            sb.AppendLine();
        }
        File.WriteAllText(path, sb.ToString());
    }

    static void WriteDiagnostics(
        string outputDir, Mother_form f, string scenario, double rootC, double criticalRain,
        int initiations, double erosionSum, double depositionSum,
        double massBefore, double massAfter, double transport, double closure)
    {
        int nr = Get<int>(f, "nr");
        int nc = Get<int>(f, "nc");
        double[,] soil = new double[nr,nc];
        double[,] moving = new double[nr,nc];
        for (int r = 0; r < nr; r++)
        for (int c = 0; c < nc; c++)
        {
            soil[r,c] = SoilMassAt(f, r, c);
            moving[r,c] = TransportMassAt(f, r, c);
        }

        WriteAscii(Path.Combine(outputDir, "soil_mass_kg.asc"), soil);
        WriteAscii(Path.Combine(outputDir, "transport_mass_kg.asc"), moving);
        WriteAscii(Path.Combine(outputDir, "soil_depth_m.asc"), Get<double[,]>(f, "soildepth_m"));
        WriteAscii(Path.Combine(outputDir, "slide_erosion_m.asc"), Get<double[,]>(f, "ero_slid_m"));
        WriteAscii(Path.Combine(outputDir, "slide_deposit_m.asc"), Get<double[,]>(f, "sed_slid_m"));
        WriteAscii(Path.Combine(outputDir, "root_cohesion_kPa.asc"), Get<double[,]>(f, "root_cohesion_kPa_new"));
        WriteAscii(Path.Combine(outputDir, "critical_rain_m_d.asc"), Get<double[,]>(f, "crrain_m_d"));
        WriteAscii(Path.Combine(outputDir, "dtm_m.asc"), Get<double[,]>(f, "dtm"));

        double closureAbs = Math.Abs(massBefore - massAfter - transport);
        string summary =
            "scenario,root_cohesion_kPa,critical_rain_m_day,initiations,erosion_thickness_sum_m,deposition_thickness_sum_m,soil_mass_before_kg,soil_mass_after_kg,transport_mass_after_kg,closure_abs_kg,closure_relative\n" +
            String.Join(",", new string[] {
                scenario, F(rootC), F(criticalRain), initiations.ToString(CultureInfo.InvariantCulture),
                F(erosionSum), F(depositionSum), F(massBefore), F(massAfter), F(transport),
                F(closureAbs), F(closure)
            }) + "\n";
        File.WriteAllText(Path.Combine(outputDir, "mass_balance.csv"), summary);

        StringBuilder cells = new StringBuilder();
        cells.AppendLine("row,col,soil_mass_kg,transport_mass_kg,soil_depth_m,erosion_m,deposition_m,root_cohesion_kPa,critical_rain_m_day");
        double[,] depth = Get<double[,]>(f, "soildepth_m");
        double[,] erosion = Get<double[,]>(f, "ero_slid_m");
        double[,] deposition = Get<double[,]>(f, "sed_slid_m");
        double[,] root = Get<double[,]>(f, "root_cohesion_kPa_new");
        double[,] critical = Get<double[,]>(f, "crrain_m_d");
        for (int r = 0; r < nr; r++)
        for (int c = 0; c < nc; c++)
        {
            cells.AppendLine(String.Join(",", new string[] {
                r.ToString(CultureInfo.InvariantCulture), c.ToString(CultureInfo.InvariantCulture),
                F(soil[r,c]), F(moving[r,c]), F(depth[r,c]), F(erosion[r,c]),
                F(deposition[r,c]), F(root[r,c]), F(critical[r,c])
            }));
        }
        File.WriteAllText(Path.Combine(outputDir, "cell_mass_ledger.csv"), cells.ToString());

        // Preserve the full vertical composition ledger so that the translation
        // mode can be checked for stratigraphic ordering, not only total mass.
        double[,,] layerThickness = Get<double[,,]>(f, "layerthickness_m");
        double[,,,] layerTexture = Get<double[,,,]>(f, "texture_kg");
        double[,,] layerYoung = Get<double[,,]>(f, "young_SOM_kg");
        double[,,] layerOld = Get<double[,,]>(f, "old_SOM_kg");
        double[,,,] layerTransport = Get<double[,,,]>(f, "lay_sediment_in_transport_kg");
        double[,,] layerYoungTransport = Get<double[,,]>(f, "lay_young_SOM_in_transport_kg");
        double[,,] layerOldTransport = Get<double[,,]>(f, "lay_old_SOM_in_transport_kg");
        StringBuilder layerLedger = new StringBuilder();
        layerLedger.AppendLine("row,col,layer,thickness_m,coarse_kg,sand_kg,silt_kg,clay_kg,fineclay_kg,young_SOM_kg,old_SOM_kg,transport_coarse_kg,transport_sand_kg,transport_silt_kg,transport_clay_kg,transport_fineclay_kg,transport_young_SOM_kg,transport_old_SOM_kg");
        for (int r = 0; r < nr; r++)
        for (int c = 0; c < nc; c++)
        for (int layer = 0; layer < layerThickness.GetLength(2); layer++)
        {
            layerLedger.AppendLine(String.Join(",", new string[] {
                r.ToString(CultureInfo.InvariantCulture),
                c.ToString(CultureInfo.InvariantCulture),
                layer.ToString(CultureInfo.InvariantCulture),
                F(layerThickness[r,c,layer]),
                F(layerTexture[r,c,layer,0]),
                F(layerTexture[r,c,layer,1]),
                F(layerTexture[r,c,layer,2]),
                F(layerTexture[r,c,layer,3]),
                F(layerTexture[r,c,layer,4]),
                F(layerYoung[r,c,layer]),
                F(layerOld[r,c,layer]),
                F(layerTransport[r,c,layer,0]),
                F(layerTransport[r,c,layer,1]),
                F(layerTransport[r,c,layer,2]),
                F(layerTransport[r,c,layer,3]),
                F(layerTransport[r,c,layer,4]),
                F(layerYoungTransport[r,c,layer]),
                F(layerOldTransport[r,c,layer])
            }));
        }
        File.WriteAllText(Path.Combine(outputDir, "layer_mass_ledger.csv"), layerLedger.ToString());
    }

    static Mother_form BuildCase(string workDir, double rootCohesionKPa, int mixingMode)
    {
        Mother_form f = new Mother_form();
        const int nr = 5, nc = 1, nodata = -9999, maxLayers = 10;
        Set(f, "nr", nr);
        Set(f, "nc", nc);
        Set(f, "dx", 10.0);
        Set(f, "nodata_value", nodata);
        Set(f, "t", 0);
        Set(f, "run_number", 9001);
        Set(f, "workdir", workDir);
        Set(f, "max_soil_layers", maxLayers);
        Set(f, "n_texture_classes", 5);
        Set(f, "number_of_data_cells", 5);
        Set(f, "conv_fac", 1.1);
        Set(f, "guiThread", TaskScheduler.Default);
        Set(f, "landslide_active", true);
        Set(f, "rain_value_m", 1.5);
        Set(f, "layer_z_surface", 0.1);
        Set(f, "layer_z_increase", 1.1);

        double[] expectedLayers = new double[maxLayers];
        for (int layer = 0; layer < maxLayers; layer++)
            expectedLayers[layer] = 0.1 * Math.Pow(1.1, layer);
        Set(f, "expected_lay_thick_m", expectedLayers);
        Set(f, "specific_area", new double[] { 10.0, 100.0, 1000.0, 50000.0, 100000.0 });

        double[,] dtm = new double[nr,nc];
        double[,] depth = new double[nr,nc];
        double[,] rain = new double[nr,nc];
        double[,] root = new double[nr,nc];
        double[,] change = new double[nr,nc];
        double[,,] layers = new double[nr,nc,maxLayers];
        double[,,] young = new double[nr,nc,maxLayers];
        double[,,] old = new double[nr,nc,maxLayers];
        double[,,] bd = new double[nr,nc,maxLayers];
        double[,,,] texture = new double[nr,nc,maxLayers,5];

        double[] z = new double[] { 100.0, 90.0, 80.0, 70.0, 69.9 };
        for (int r = 0; r < nr; r++)
        {
            dtm[r,0] = z[r];
            depth[r,0] = 1.0;
            rain[r,0] = 1.5;
            root[r,0] = rootCohesionKPa;

            // Build a PTF-consistent 1-m profile using LORICA's default
            // ten-layer geometric template (0.10 m, increasing by 1.1).
            // Mass in each layer is calculated from LORICA's own bulk-density
            // function, so thickness_calc() must reproduce the input depth.
            double remainingDepth = 1.0;
            double topDepth = 0.0;
            for (int layer = 0; layer < maxLayers && remainingDepth > 1e-12; layer++)
            {
                double layerThickness = Math.Min(expectedLayers[layer], remainingDepth);
                double bottomDepth = topDepth + layerThickness;
                // Deliberately vary texture by depth: the translation test
                // must preserve distinct source-layer signatures after routing.
                double sandFraction = 0.45 - 0.02 * layer;
                double siltFraction = 0.45 + 0.01 * layer;
                double clayFraction = 1.0 - sandFraction - siltFraction;
                double layerBd = CallDouble(
                    f, "bulk_density_calc_kg_m3",
                    0.0, sandFraction, siltFraction, clayFraction, 0.0, 0.0, 0.0,
                    topDepth, bottomDepth);
                double layerMass = layerBd * 100.0 * layerThickness;

                layers[r,0,layer] = layerThickness;
                bd[r,0,layer] = layerBd;
                texture[r,0,layer,0] = 0.0;
                texture[r,0,layer,1] = sandFraction * layerMass;
                texture[r,0,layer,2] = siltFraction * layerMass;
                texture[r,0,layer,3] = clayFraction * layerMass;
                texture[r,0,layer,4] = 0.0;

                topDepth = bottomDepth;
                remainingDepth -= layerThickness;
            }
            if (remainingDepth > 1e-8)
                throw new Exception("Ten-layer template did not cover the 1-m synthetic soil profile.");
        }

        Set(f, "dtm", dtm);
        Set(f, "soildepth_m", depth);
        Set(f, "rain_m", rain);
        Set(f, "root_cohesion_kPa_new", root);
        Set(f, "dtmchange_m", change);
        Set(f, "layerthickness_m", layers);
        Set(f, "young_SOM_kg", young);
        Set(f, "old_SOM_kg", old);
        Set(f, "bulkdensity", bd);
        Set(f, "texture_kg", texture);

        Set(f, "stslope_radians", new double[nr,nc]);
        Set(f, "crrain_m_d", new double[nr,nc]);
        Set(f, "contributing_cells", new double[nr,nc]);
        Set(f, "transmissiv_m2_d", new double[nr,nc]);
        Set(f, "Cohesion_factor", new double[nr,nc]);
        Set(f, "sat_bd_kg_m3", new double[nr,nc]);
        Set(f, "peak_friction_angle_radians", new double[nr,nc]);
        Set(f, "resid_friction_angle_radians", new double[nr,nc]);

        Set(f, "ero_slid_m", new double[nr,nc]);
        Set(f, "sed_slid_m", new double[nr,nc]);
        Set(f, "remaining_vertical_size_m", new double[nr,nc]);
        Set(f, "slidestatus", new short[nr,nc]);
        Set(f, "sediment_in_transport_kg", new double[nr,nc,5]);
        Set(f, "young_SOM_in_transport_kg", new double[nr,nc]);
        Set(f, "old_SOM_in_transport_kg", new double[nr,nc]);
        Set(f, "lay_sediment_in_transport_kg", new double[nr,nc,maxLayers,5]);
        Set(f, "lay_young_SOM_in_transport_kg", new double[nr,nc,maxLayers]);
        Set(f, "lay_old_SOM_in_transport_kg", new double[nr,nc,maxLayers]);

        Set(f, "row_index", new int[] { 4, 3, 2, 1, 0 });
        Set(f, "col_index", new int[] { 0, 0, 0, 0, 0 });
        Set(f, "inputheader", new string[] {
            "ncols         1", "nrows         5", "xllcorner     0",
            "yllcorner     0", "cellsize      10", "NODATA_value  -9999"
        });

        Get<TextBox>(f, "text_ls_rel_rain_intens").Text = "0.1";
        Get<TextBox>(f, "minimum_slope_for_movement_tan_textbox").Text = "0.7";
        Get<TextBox>(f, "runout_ratio_textbox").Text = "0.4";
        if (mixingMode != 1 && mixingMode != 2) throw new ArgumentOutOfRangeException("mixingMode");
        Get<RadioButton>(f, "ls_mix_radio_1").Checked = (mixingMode == 1);
        Get<RadioButton>(f, "ls_mix_radio_2").Checked = (mixingMode == 2);
        Console.WriteLine("LS_MODE_SELECTED=" + mixingMode);
        Directory.CreateDirectory(workDir);
        return f;
    }

    static void AssertLayerSequence(Mother_form f, int row, int col, int destinationLayer, int sourceLayerStart, int count)
    {
        double[,,,] texture = Get<double[,,,]>(f, "texture_kg");
        for (int i = 0; i < count; i++)
        {
            int layer = destinationLayer + i;
            int sourceLayer = sourceLayerStart + i;
            double mineralMass = 0.0;
            for (int tex = 0; tex < 5; tex++) mineralMass += texture[row,col,layer,tex];
            if (mineralMass <= 1e-8)
                throw new Exception("Expected deposited stratigraphic layer is empty at row " + row + ", layer " + layer);
            double observedSand = texture[row,col,layer,1] / mineralMass;
            double observedSilt = texture[row,col,layer,2] / mineralMass;
            double observedClay = texture[row,col,layer,3] / mineralMass;
            double expectedSand = 0.45 - 0.02 * sourceLayer;
            double expectedSilt = 0.45 + 0.01 * sourceLayer;
            double expectedClay = 1.0 - expectedSand - expectedSilt;
            if (Math.Abs(observedSand - expectedSand) > 1e-6 ||
                Math.Abs(observedSilt - expectedSilt) > 1e-6 ||
                Math.Abs(observedClay - expectedClay) > 1e-6)
                throw new Exception("Layer translation order/composition mismatch at row " + row +
                    ", destination layer " + layer + ", expected source layer " + sourceLayer +
                    ", observed sand fraction " + observedSand.ToString("R"));
        }
    }

    static Mother_form BuildConvergentCase(string workDir, int mixingMode, bool limitedCapacity = false)
    {
        Mother_form f = BuildCase(workDir, 0.0, mixingMode);
        const int nr = 5, nc = 5, maxLayers = 10;

        Set(f, "nr", nr);
        Set(f, "nc", nc);
        Set(f, "number_of_data_cells", nr * nc);

        double[,] dtm = new double[nr,nc];
        double[,] depth = new double[nr,nc];
        double[,] rain = new double[nr,nc];
        double[,] root = new double[nr,nc];
        double[,] change = new double[nr,nc];
        double[,,] layers = new double[nr,nc,maxLayers];
        double[,,] young = new double[nr,nc,maxLayers];
        double[,,] old = new double[nr,nc,maxLayers];
        double[,,] bd = new double[nr,nc,maxLayers];
        double[,,,] texture = new double[nr,nc,maxLayers,5];

        double[] expectedLayers = Get<double[]>(f, "expected_lay_thick_m");
        List<int> cellIds = new List<int>();
        for (int r = 0; r < nr; r++)
        for (int col = 0; col < nc; col++)
        {
            double dr = r - 2.0;
            double dc = col - 2.0;
            double distance = Math.Sqrt(dr * dr + dc * dc);
            double centerElevation = limitedCapacity ? 50.0 : 40.0;
            double elevation = centerElevation + 10.0 * distance;
            // Lower one rim cell to 57.5 m. The closed centre basin then has
            // 7.5 m of storage, slightly less than the 8 m source volume.
            if (limitedCapacity && r == 3 && col == 2)
                elevation = 57.5;
            dtm[r,col] = elevation;
            rain[r,col] = 1.5;

            // Eight cells surrounding the internal bowl are the failed source
            // ring. The centre and outer cells retain high root cohesion.
            bool ringSource = distance > 0.0 && distance <= Math.Sqrt(2.0) + 1e-9;
            bool closedSinkSaddle = limitedCapacity && r == 3 && col == 2;
            bool extraSource = limitedCapacity && r == 0 && col == 2;
            root[r,col] = ((ringSource && !closedSinkSaddle) || extraSource)
                ? 0.0 : 7.6;

            depth[r,col] = 1.0;
            double remainingDepth = 1.0;
            double topDepth = 0.0;
            for (int layer = 0; layer < maxLayers && remainingDepth > 1e-12; layer++)
            {
                double layerThickness = Math.Min(expectedLayers[layer], remainingDepth);
                double bottomDepth = topDepth + layerThickness;
                double sandFraction = 0.45 - 0.02 * layer;
                double siltFraction = 0.45 + 0.01 * layer;
                double clayFraction = 1.0 - sandFraction - siltFraction;
                double layerBd = CallDouble(
                    f, "bulk_density_calc_kg_m3",
                    0.0, sandFraction, siltFraction, clayFraction, 0.0, 0.0, 0.0,
                    topDepth, bottomDepth);
                double layerMass = layerBd * 100.0 * layerThickness;

                layers[r,col,layer] = layerThickness;
                bd[r,col,layer] = layerBd;
                texture[r,col,layer,0] = 0.0;
                texture[r,col,layer,1] = sandFraction * layerMass;
                texture[r,col,layer,2] = siltFraction * layerMass;
                texture[r,col,layer,3] = clayFraction * layerMass;
                texture[r,col,layer,4] = 0.0;

                topDepth = bottomDepth;
                remainingDepth -= layerThickness;
            }
            if (remainingDepth > 1e-8)
                throw new Exception("2-D ten-layer profile did not cover 1 m.");

            cellIds.Add(r * nc + col);
        }

        // LORICA processes cells from high to low elevation by reversing
        // row_index/col_index, so these arrays are sorted low-to-high.
        cellIds.Sort((a, b) =>
        {
            int ar = a / nc, ac = a % nc;
            int br = b / nc, bc = b % nc;
            int cmp = dtm[ar,ac].CompareTo(dtm[br,bc]);
            return cmp != 0 ? cmp : a.CompareTo(b);
        });
        int[] rowIndex = cellIds.Select(id => id / nc).ToArray();
        int[] colIndex = cellIds.Select(id => id % nc).ToArray();

        Set(f, "dtm", dtm);
        Set(f, "soildepth_m", depth);
        Set(f, "rain_m", rain);
        Set(f, "root_cohesion_kPa_new", root);
        Set(f, "dtmchange_m", change);
        Set(f, "layerthickness_m", layers);
        Set(f, "young_SOM_kg", young);
        Set(f, "old_SOM_kg", old);
        Set(f, "bulkdensity", bd);
        Set(f, "texture_kg", texture);

        Set(f, "stslope_radians", new double[nr,nc]);
        Set(f, "crrain_m_d", new double[nr,nc]);
        Set(f, "contributing_cells", new double[nr,nc]);
        Set(f, "transmissiv_m2_d", new double[nr,nc]);
        Set(f, "Cohesion_factor", new double[nr,nc]);
        Set(f, "sat_bd_kg_m3", new double[nr,nc]);
        Set(f, "peak_friction_angle_radians", new double[nr,nc]);
        Set(f, "resid_friction_angle_radians", new double[nr,nc]);

        Set(f, "ero_slid_m", new double[nr,nc]);
        Set(f, "sed_slid_m", new double[nr,nc]);
        Set(f, "remaining_vertical_size_m", new double[nr,nc]);
        Set(f, "slidestatus", new short[nr,nc]);
        Set(f, "sediment_in_transport_kg", new double[nr,nc,5]);
        Set(f, "young_SOM_in_transport_kg", new double[nr,nc]);
        Set(f, "old_SOM_in_transport_kg", new double[nr,nc]);
        Set(f, "lay_sediment_in_transport_kg", new double[nr,nc,maxLayers,5]);
        Set(f, "lay_young_SOM_in_transport_kg", new double[nr,nc,maxLayers]);
        Set(f, "lay_old_SOM_in_transport_kg", new double[nr,nc,maxLayers]);

        Set(f, "row_index", rowIndex);
        Set(f, "col_index", colIndex);
        Set(f, "inputheader", new string[] {
            "ncols         5", "nrows         5", "xllcorner     0",
            "yllcorner     0", "cellsize      10", "NODATA_value  -9999"
        });
        return f;
    }

    static void Test2DConvergentCase(string scenario, int mixingMode)
    {
        string root = Path.Combine(OutputRoot, scenario);
        if (Directory.Exists(root)) Directory.Delete(root, true);
        Directory.CreateDirectory(root);

        using (Mother_form f = BuildConvergentCase(root, mixingMode))
        {
            Dictionary<string,string> cfg = new Dictionary<string,string>();
            cfg["landslide_event_mode"] = "explicit_event";
            cfg["landslide_event_rainfall_mm"] = "60";
            cfg["landslide_event_duration_h"] = "6";
            Call(f, "configure_treed_landslide_event", cfg);

            double massBefore = TotalSoilMass(f);
            Call(f, "calc_and_write_ls_rasters");
            double[,] critical = Get<double[,]>(f, "crrain_m_d");

            // The eight-cell source ring has zero root cohesion and should
            // contain at least one zero-threshold unstable cell.
            int zeroThresholdCells = 0;
            for (int r = 1; r <= 3; r++)
            for (int col = 1; col <= 3; col++)
            {
                if (r == 2 && col == 2) continue;
                if (Math.Abs(critical[r,col]) <= 1e-10) zeroThresholdCells++;
            }
            if (zeroThresholdCells == 0)
                throw new Exception("2-D convergent source ring has no zero-threshold unstable cells.");

            Call(f, "calculate_slide_new");

            double[,] erosion = Get<double[,]>(f, "ero_slid_m");
            double[,] deposition = Get<double[,]>(f, "sed_slid_m");
            double erosionAbs = SumAbs(erosion);
            double depositionSum = 0.0;
            for (int r = 0; r < 5; r++)
            for (int col = 0; col < 5; col++)
                depositionSum += deposition[r,col];

            int initiations = Get<int>(f, "landslide_initiation_cells");
            double massAfter = TotalSoilMass(f);
            double transport = TotalTransportMass(f);
            double closure = Math.Abs(massBefore - massAfter - transport) / Math.Max(1.0, massBefore);
            WriteDiagnostics(root, f, scenario, 0.0, 0.0, initiations,
                erosionAbs, depositionSum, massBefore, massAfter, transport, closure);

            if (initiations != 8 || erosionAbs <= 0.0)
                throw new Exception("2-D convergent source ring should initiate in exactly eight cells.");
            for (int r = 0; r < 5; r++)
            for (int col = 0; col < 5; col++)
            {
                bool sourceRing = (r >= 1 && r <= 3 && col >= 1 && col <= 3 && !(r == 2 && col == 2));
                if (sourceRing && erosion[r,col] >= -1e-8)
                    throw new Exception("Expected erosion in the eight-cell source ring at " + r + "," + col);
                if (!sourceRing && Math.Abs(erosion[r,col]) > 1e-8)
                    throw new Exception("Unexpected erosion outside the source ring at " + r + "," + col);
                if (!(r == 2 && col == 2) && deposition[r,col] > 1e-8)
                    throw new Exception("Depositional material escaped the internal bowl at " + r + "," + col);
            }
            if (deposition[2,2] <= 0.0)
                throw new Exception("2-D convergent event did not deposit material in the internal bowl.");
            if (transport > 1e-6)
                throw new Exception("The internal bowl had sufficient capacity but left material in transport: " + transport.ToString("R"));
            double[,] finalDtm = Get<double[,]>(f, "dtm");
            if (finalDtm[2,2] >= 50.0)
                throw new Exception("Internal bowl deposit exceeded the 10-m spill elevation.");
            if (closure > 1e-6)
                throw new Exception("2-D convergent landslide mass closure failed: " + closure.ToString("R"));

            Console.WriteLine(
                "ROOT_CASE=" + scenario +
                " mixing_mode=" + mixingMode +
                " zero_threshold_cells=" + zeroThresholdCells +
                " initiations=" + initiations +
                " erosion_m=" + erosionAbs.ToString("R") +
                " deposition_m=" + depositionSum.ToString("R") +
                " mass_before_kg=" + massBefore.ToString("R") +
                " mass_after_kg=" + massAfter.ToString("R") +
                " transport_after_kg=" + transport.ToString("R") +
                " mass_closure=" + closure.ToString("R"));
        }
    }

    static void TestRainfallTimeSeries(string workDir)
    {
        using (Mother_form f = new Mother_form())
        {
            Set(f, "nr", 2);
            Set(f, "nc", 1);
            Set(f, "nodata_value", -9999);
            Set(f, "t", 1);
            Set(f, "rainfall_record", new int[] { 1000, 2000 });
            Set(f, "rain_value_m", 0.5);
            Set(f, "dtm", new double[,] { { 1.0 }, { 0.0 } });
            Set(f, "rain_m", new double[,] { { 0.5 }, { 0.5 } });
            Get<CheckBox>(f, "check_time_rain").Checked = true;
            Call(f, "update_time_varying_rainfall_for_current_timestep");
            double annual = Get<double>(f, "rain_value_m");
            double[,] raster = Get<double[,]>(f, "rain_m");
            if (Math.Abs(annual - 2.0) > 1e-12 || Math.Abs(raster[0,0] - 2.0) > 1e-12 ||
                Math.Abs(raster[1,0] - 2.0) > 1e-12)
                throw new Exception("Time-varying rainfall was not updated before hydrology.");
            Console.WriteLine("RAINFALL_TIMESERIES_PRE_HYDROLOGY_PASS");
        }
    }

    static void TestEventConfig()
    {
        using (Mother_form f = new Mother_form())
        {
            Dictionary<string,string> cfg = new Dictionary<string,string>();
            cfg["landslide_event_mode"] = "explicit_event";
            cfg["landslide_event_rainfall_mm"] = "60";
            cfg["landslide_event_duration_h"] = "6";
            Call(f, "configure_treed_landslide_event", cfg);
            double intensity = Get<double>(f, "treed_landslide_event_intensity_m_d");
            bool enabled = Get<bool>(f, "treed_landslide_event_override_enabled");
            if (!enabled || Math.Abs(intensity - 0.24) > 1e-12)
                throw new Exception("Explicit 60 mm / 6 h event conversion failed.");
            Console.WriteLine("EXPLICIT_EVENT_RAINFALL_CONFIG_PASS intensity_m_day=" + intensity.ToString("R"));
        }
    }

    static void TestRootCohesionCase(string rootName, double rootC, bool expectFailure, int mixingMode)
    {
        string root = Path.Combine(OutputRoot, rootName);
        if (Directory.Exists(root)) Directory.Delete(root, true);
        Directory.CreateDirectory(root);

        using (Mother_form f = BuildCase(root, rootC, mixingMode))
        {
            Dictionary<string,string> cfg = new Dictionary<string,string>();
            cfg["landslide_event_mode"] = "explicit_event";
            cfg["landslide_event_rainfall_mm"] = "60";
            cfg["landslide_event_duration_h"] = "6";
            Call(f, "configure_treed_landslide_event", cfg);

            double[] beforeDepth = new double[5];
            double[,] initialDepth = Get<double[,]>(f, "soildepth_m");
            for (int r = 0; r < 5; r++) beforeDepth[r] = initialDepth[r,0];
            double massBefore = TotalSoilMass(f);

            Call(f, "calc_and_write_ls_rasters");

            // The diagnostic writer must retain the TREED root-cohesion array.
            double[,] retainedRoot = Get<double[,]>(f, "root_cohesion_kPa_new");
            for (int r = 0; r < 5; r++)
                if (Math.Abs(retainedRoot[r,0] - rootC) > 1e-10)
                    throw new Exception("Diagnostic output erased root cohesion at row " + r);

            double[,] critical = Get<double[,]>(f, "crrain_m_d");
            double topCritical = critical[0,0];
            if (rootC == 0.0 && Math.Abs(topCritical) > 1e-10)
                throw new Exception("Expected zero critical rainfall for unconditionally unstable bare-root case; got " + topCritical);
            if (rootC > 0.0 && rootC < 7.0 && !(topCritical > 0.0 && topCritical < 11.0))
                throw new Exception("Expected finite positive critical rainfall for intermediate root cohesion; got " + topCritical);
            if (rootC >= 7.0 && topCritical != -9999.0)
                throw new Exception("Expected unconditionally stable slope for high root cohesion; got " + topCritical);

            Call(f, "calculate_slide_new");

            // In the bare-root translation case, the upper seven deposited
            // layers at row 3 should retain source-layer order 0..6. The
            // residual lower layers reach row 4 in order 6..7.
            if (mixingMode == 2 && rootC == 0.0)
            {
                AssertLayerSequence(f, 3, 0, 0, 0, 7);
                AssertLayerSequence(f, 4, 0, 0, 6, 2);
            }

            double[,] erosion = Get<double[,]>(f, "ero_slid_m");
            double[,] deposition = Get<double[,]>(f, "sed_slid_m");
            double[,] afterDepth = Get<double[,]>(f, "soildepth_m");
            double erosionAbs = SumAbs(erosion);
            double depositionSum = 0.0;
            for (int r = 0; r < 5; r++) depositionSum += deposition[r,0];
            int initiations = Get<int>(f, "landslide_initiation_cells");
            double massAfter = TotalSoilMass(f);
            double transport = TotalTransportMass(f);
            double massClosure = Math.Abs(massBefore - massAfter - transport) / Math.Max(1.0, massBefore);
            WriteDiagnostics(root, f, rootName, rootC, topCritical, initiations, erosionAbs, depositionSum, massBefore, massAfter, transport, massClosure);

            if (expectFailure)
            {
                if (initiations <= 0 || erosionAbs <= 0.0)
                    throw new Exception("Expected rainfall-triggered landslide initiation for " + rootName);
                if (afterDepth[0,0] >= beforeDepth[0])
                    throw new Exception("Expected shallow soil-depth reduction at the initiating cell for " + rootName);
                if (massClosure > 1e-6)
                    throw new Exception("Landslide mass closure failed: " + massClosure);
            }
            else
            {
                if (initiations != 0 || erosionAbs > 1e-10 || depositionSum > 1e-10)
                    throw new Exception("High root cohesion should suppress the synthetic event landslide.");
                if (Math.Abs(afterDepth[0,0] - beforeDepth[0]) > 1e-6)
                    throw new Exception("No-slide case changed soil depth; synthetic profile is not PTF-consistent.");
            }

            Console.WriteLine(
                "ROOT_CASE=" + rootName +
                " TrCr_kPa=" + rootC.ToString("R") +
                " mixing_mode=" + mixingMode +
                " critical_rain_m_day=" + topCritical.ToString("R") +
                " initiations=" + initiations +
                " erosion_m=" + erosionAbs.ToString("R") +
                " deposition_m=" + depositionSum.ToString("R") +
                " mass_before_kg=" + massBefore.ToString("R") +
                " mass_after_kg=" + massAfter.ToString("R") +
                " transport_after_kg=" + transport.ToString("R") +
                " mass_closure=" + massClosure.ToString("R"));
        }
    }

    static void Test2DClosedSinkResidualCase(string scenario, int mixingMode)
    {
        string root = Path.Combine(OutputRoot, scenario);
        if (Directory.Exists(root)) Directory.Delete(root, true);
        Directory.CreateDirectory(root);

        using (Mother_form f = BuildConvergentCase(root, mixingMode, true))
        {
            // Stress the terminal sink with a runout distance greater than one cell.
            Get<TextBox>(f, "runout_ratio_textbox").Text = "20.0";
            Dictionary<string,string> cfg = new Dictionary<string,string>();
            cfg["landslide_event_mode"] = "explicit_event";
            cfg["landslide_event_rainfall_mm"] = "60";
            cfg["landslide_event_duration_h"] = "6";
            Call(f, "configure_treed_landslide_event", cfg);

            double massBefore = TotalSoilMass(f);
            Call(f, "calc_and_write_ls_rasters");
            double[,] critical = Get<double[,]>(f, "crrain_m_d");
            int zeroThresholdCells = 0;
            double[,] rootMap = Get<double[,]>(f, "root_cohesion_kPa_new");
            for (int r = 0; r < 5; r++)
            for (int col = 0; col < 5; col++)
                if (rootMap[r,col] == 0.0 && Math.Abs(critical[r,col]) <= 1e-10)
                    zeroThresholdCells++;
            if (zeroThresholdCells != 8)
                throw new Exception("Closed-sink residual test must have eight zero-threshold source cells; found " + zeroThresholdCells);

            Call(f, "calculate_slide_new");

            double[,] erosion = Get<double[,]>(f, "ero_slid_m");
            double[,] deposition = Get<double[,]>(f, "sed_slid_m");
            double erosionAbs = SumAbs(erosion);
            double depositionSum = 0.0;
            for (int r = 0; r < 5; r++)
            for (int col = 0; col < 5; col++)
                depositionSum += deposition[r,col];

            int initiations = Get<int>(f, "landslide_initiation_cells");
            double massAfter = TotalSoilMass(f);
            double transport = TotalTransportMass(f);
            double closure = Math.Abs(massBefore - massAfter - transport) / Math.Max(1.0, massBefore);
            WriteDiagnostics(root, f, scenario, 0.0, 0.0, initiations,
                erosionAbs, depositionSum, massBefore, massAfter, transport, closure);

            if (initiations != 8 || erosionAbs <= 0.0)
                throw new Exception("Closed-sink residual test should receive eight failed source cells.");
            for (int r = 0; r < 5; r++)
            for (int col = 0; col < 5; col++)
            {
                double dr = r - 2.0;
                double dc = col - 2.0;
                double distance = Math.Sqrt(dr * dr + dc * dc);
                bool sourceCell = (distance > 0.0 && distance <= Math.Sqrt(2.0) + 1e-9 &&
                    !(r == 3 && col == 2)) || (r == 0 && col == 2);
                if (sourceCell && erosion[r,col] >= -1e-8)
                    throw new Exception("Expected erosion in closed-sink residual source cell at " + r + "," + col);
                if (!sourceCell && Math.Abs(erosion[r,col]) > 1e-8)
                    throw new Exception("Unexpected erosion outside closed-sink residual source cells at " + r + "," + col);
                if (!(r == 2 && col == 2) && deposition[r,col] > 1e-8)
                    throw new Exception("Limited-capacity deposit escaped the internal bowl at " + r + "," + col);
            }

            double[,] finalDtm = Get<double[,]>(f, "dtm");
            if (finalDtm[2,2] <= 50.0)
                throw new Exception("The closed sink should receive a positive deposit.");
            if (deposition[2,2] <= 0.0 || transport <= 1e-6)
                throw new Exception("The closed sink should retain undeposited material in transport storage.");
            if (closure > 1e-6)
                throw new Exception("Closed-sink residual test mass closure failed: " + closure.ToString("R"));

            Console.WriteLine(
                "ROOT_CASE=" + scenario +
                " mixing_mode=" + mixingMode +
                " initiations=" + initiations +
                " erosion_m=" + erosionAbs.ToString("R") +
                " deposition_m=" + depositionSum.ToString("R") +
                " mass_before_kg=" + massBefore.ToString("R") +
                " mass_after_kg=" + massAfter.ToString("R") +
                " transport_after_kg=" + transport.ToString("R") +
                " mass_closure=" + closure.ToString("R"));
        }
    }

    static void TestResidualPersistenceAcrossTimesteps(string scenario, int mixingMode)
    {
        string root = Path.Combine(OutputRoot, scenario);
        if (Directory.Exists(root)) Directory.Delete(root, true);
        Directory.CreateDirectory(root);

        using (Mother_form f = BuildConvergentCase(root, mixingMode, true))
        {
            const int nr = 5, nc = 5, days = 365;
            Get<TextBox>(f, "runout_ratio_textbox").Text = "20.0";
            Get<TextBox>(f, "text_ls_rel_rain_intens").Text = "1";
            Get<TextBox>(f, "daily_n").Text = "1";
            Get<CheckBox>(f, "Landslide_checkbox").Checked = true;
            Get<CheckBox>(f, "Water_ero_checkbox").Checked = true;
            Get<CheckBox>(f, "only_waterflow_checkbox").Checked = false;
            Get<CheckBox>(f, "daily_water").Checked = true;
            Get<CheckBox>(f, "check_scaling_daily_weather").Checked = false;
            Get<CheckBox>(f, "check_time_rain").Checked = false;
            Get<CheckBox>(f, "version_lux_checkbox").Checked = false;

            Set(f, "t", 1);
            Set(f, "t_intervene", 0);
            Set(f, "daily_weather_prepared_for_timestep", false);
            Set(f, "index", new double[nr * nc]);
            Set(f, "rowcol_index", new string[nr * nc]);
            Set(f, "rain_value_m", 0.01);
            Set(f, "temp_value_C", 10);
            Set(f, "evap_value_m", 0.0);
            Set(f, "infil_value_m", 0.0);

            // One controlled 10-mm / 6-h rainfall event in the 365-day
            // weather record. The remaining days are dry.
            int[] precipitation = new int[days];
            int[] duration = new int[days];
            int[] tmin = new int[days];
            int[] tavg = new int[days];
            int[] tmax = new int[days];
            precipitation[0] = 10;
            duration[0] = 6;
            for (int day = 0; day < days; day++)
            {
                tmin[day] = 5;
                tavg[day] = 10;
                tmax[day] = 15;
            }
            Set(f, "P_all", precipitation);
            Set(f, "D_all", duration);
            Set(f, "Tmin_all", tmin);
            Set(f, "Tavg_all", tavg);
            Set(f, "Tmax_all", tmax);

            Set(f, "OFy_m", new double[nr,nc,10]);
            Set(f, "waterflow_m3", new double[nr,nc]);
            Set(f, "Ks_topsoil_m_h", new double[nr,nc]);
            Set(f, "Ks_min_mh", 0.0001);
            Set(f, "Ra_rcm", new double[nr,nc,12]);
            Set(f, "veg_correction_factor", new double[nr,nc]);
            Set(f, "ETay", new double[nr,nc]);
            Set(f, "ET0y", new double[nr,nc]);
            Set(f, "Iy", new double[nr,nc]);
            Set(f, "pond_y", new double[nr,nc]);
            Set(f, "outflow_y", new double[nr,nc]);
            Set(f, "waterfactor", new double[nr,nc]);
            Set(f, "total_outflow_y", new double[nr,nc]);
            Set(f, "aridity_vegetation", new double[nr,nc]);
            Set(f, "evapotranspiration", new double[nr,nc]);
            Set(f, "infil", new double[nr,nc]);
            Set(f, "sum_water_erosion", new double[nr,nc]);
            Set(f, "dz_ero_m", new double[nr,nc]);
            Set(f, "dz_sed_m", new double[nr,nc]);
            Set(f, "lake_sed_m", new double[nr,nc]);
            Set(f, "K_fac", new double[nr,nc]);
            Set(f, "bio_protection", new double[nr,nc]);

            double[,] ks = Get<double[,]>(f, "Ks_topsoil_m_h");
            double[,] kfac = Get<double[,]>(f, "K_fac");
            double[,] veg = Get<double[,]>(f, "veg_correction_factor");
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
            {
                ks[r,col] = 0.01;       // all non-source cells absorb rainfall excess
                kfac[r,col] = 1e-6;
                veg[r,col] = 1.0;
            }
            ks[0,0] = 0.0;              // the stable NW cell generates runoff
            double[,,] radiation = Get<double[,,]>(f, "Ra_rcm");
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
            for (int mo = 0; mo < 12; mo++)
                radiation[r,col,mo] = 1e-6;

            Set(f, "upper_particle_size", new double[] { 0.01, 0.002, 0.00005, 0.000002, 0.0000001 });
            Set(f, "water_ero_active", true);
            Set(f, "erodibility_value_m", 1e-6);
            Set(f, "bio_protection_constant", 0.0);
            Set(f, "rock_protection_constant", 0.0);
            Set(f, "constant_selective_transcap", 0.0);
            Set(f, "erosion_threshold_kg", 0.0);
            Set(f, "m", 0.5);
            Set(f, "n", 1.0);

            Dictionary<string,string> cfg = new Dictionary<string,string>();
            cfg["landslide_event_mode"] = "explicit_event";
            cfg["landslide_event_rainfall_mm"] = "60";
            cfg["landslide_event_duration_h"] = "6";
            Call(f, "configure_treed_landslide_event", cfg);

            // Event 1 creates residual material at the closed central sink.
            // Follow the same layer-maintenance and stability sequence used
            // by every_timestep() before calculating the landslide event.
            double massBefore1 = TotalSoilMass(f);
            Call(f, "soil_update_split_and_combine_layers");
            Call(f, "comb_sort");
            Call(f, "ini_slope");
            Call(f, "calculate_critical_rain");
            Call(f, "calculate_slide_new");
            Call(f, "soil_update_split_and_combine_layers");
            double soilAfter1 = TotalSoilMass(f);
            double transportAfter1 = TotalPersistentLandslideMass(f);
            double totalAfter1 = soilAfter1 + transportAfter1;
            double closure1 = Math.Abs(massBefore1 - totalAfter1) / Math.Max(1.0, massBefore1);
            if (transportAfter1 <= 1e-6 || closure1 > 1e-6)
                throw new Exception("Event 1 did not produce a closed, mass-balanced residual store.");

            // Annual hydrology runs before initialise_every() in the actual
            // LORICA timestep. It generates OFy_m from the 365-day weather.
            Call(f, "water_balance");
            double[,,] annualFlow = Get<double[,,]>(f, "OFy_m");
            // At the NW corner, east/south/southeast are directions 5, 7, and 8.
            double sourceFlow = annualFlow[0,0,5] + annualFlow[0,0,7] + annualFlow[0,0,8];
            if (sourceFlow <= 0.0)
                throw new Exception("Annual water_balance() did not generate flow from the source cell.");

            // Match every_timestep(): water balance -> annual reset -> sort
            // -> daily erosion -> layer split/combine.
            Call(f, "initialise_every");
            Call(f, "comb_sort");
            double transportAfterReset = TotalPersistentLandslideMass(f);
            if (Math.Abs(transportAfterReset - transportAfter1) >
                Math.Max(1e-6, transportAfter1 * 1e-10))
                throw new Exception("Residual landslide material was lost by initialise_every().");

            double soilBeforeWater = TotalSoilMass(f);
            Call(f, "calculate_water_ero_sed_daily");
            double soilAfterWater = TotalSoilMass(f);
            double transportAfterWater = TotalPersistentLandslideMass(f);
            double[,] waterErosion = Get<double[,]>(f, "dz_ero_m");
            double[,] waterDeposition = Get<double[,]>(f, "dz_sed_m");
            double boundaryExport = TotalTransientWaterTransportMassAtBoundary(f);
            double soilLoss = soilBeforeWater - soilAfterWater;
            double waterErosionClosure = Math.Abs(soilLoss - boundaryExport) /
                Math.Max(1.0, soilBeforeWater);
            double staleWaterTransportArrays = TotalTransportMass(f) - transportAfterWater;

            if (waterErosion[0,0] >= 0.0 || waterDeposition[1,1] <= 0.0)
                throw new Exception("Annual hydrology did not produce source erosion and interior receiver deposition.");
            if (Math.Abs(transportAfterWater - transportAfterReset) >
                Math.Max(1e-6, transportAfterReset * 1e-10))
                throw new Exception("Daily water erosion changed the persistent landslide residual.");
            if (waterErosionClosure > 1e-6)
                throw new Exception("Annual water-erosion export failed soil-mass closure: " + waterErosionClosure.ToString("R"));

            // Match the two layer-maintenance calls in the main timestep
            // (after water erosion and immediately before landsliding).
            double soilBeforeLayerMaintenance = TotalSoilMass(f);
            Call(f, "soil_update_split_and_combine_layers");
            Call(f, "soil_update_split_and_combine_layers");
            double soilAfterLayerMaintenance = TotalSoilMass(f);
            double persistentAfterLayerMaintenance = TotalPersistentLandslideMass(f);
            double totalAfterLayerMaintenance = soilAfterLayerMaintenance + persistentAfterLayerMaintenance;
            double layerMaintenanceClosure = Math.Abs(soilBeforeLayerMaintenance - soilAfterLayerMaintenance) /
                Math.Max(1.0, soilBeforeLayerMaintenance);
            if (layerMaintenanceClosure > 1e-10)
                throw new Exception("Soil layer split/combine changed total soil mass: " + layerMaintenanceClosure.ToString("R"));
            if (Math.Abs(persistentAfterLayerMaintenance - transportAfter1) >
                Math.Max(1e-6, transportAfter1 * 1e-10))
                throw new Exception("Soil layer maintenance changed persistent landslide residual mass.");

            // Main timestep landslide order: sort, initialise slope parameters,
            // calculate critical rainfall, move the residual, then maintain layers.
            Call(f, "comb_sort");
            Call(f, "ini_slope");
            Call(f, "calculate_critical_rain");
            double massBefore2 = TotalSoilMass(f) + TotalPersistentLandslideMass(f);
            Call(f, "calculate_slide_new");
            Call(f, "soil_update_split_and_combine_layers");

            double soilAfter2 = TotalSoilMass(f);
            double transportAfter2 = TotalPersistentLandslideMass(f);
            double totalAfter2 = soilAfter2 + transportAfter2;
            double closure2 = Math.Abs(massBefore2 - totalAfter2) / Math.Max(1.0, massBefore2);
            double[,] deposition2 = Get<double[,]>(f, "sed_slid_m");
            double depositionSum2 = 0.0;
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
                depositionSum2 += deposition2[r,col];

            if (deposition2[2,2] <= 0.0 || depositionSum2 <= 0.0)
                throw new Exception("Stored residual was not reactivated and deposited in event 2.");
            if (transportAfter2 >= transportAfter1 - 1e-6)
                throw new Exception("Event 2 did not reduce the stored residual transport mass.");
            if (closure2 > 1e-6)
                throw new Exception("Event 2 residual remobilization failed mass closure: " + closure2.ToString("R"));

            string event2Dir = Path.Combine(root, "event2");
            Directory.CreateDirectory(event2Dir);
            WriteDiagnostics(event2Dir, f, scenario + "_event2", 0.0, 0.0,
                Get<int>(f, "landslide_initiation_cells"), SumAbs(Get<double[,]>(f, "ero_slid_m")),
                depositionSum2, massBefore2, soilAfter2, transportAfter2, closure2);

            string persistence =
                "stage,soil_mass_kg,persistent_landslide_mass_kg,boundary_water_export_kg,stale_water_transport_arrays_kg,total_physical_mass_kg,relative_closure\n" +
                "event1," + F(soilAfter1) + "," + F(transportAfter1) + ",0,0," + F(totalAfter1) + "," + F(closure1) + "\n" +
                "after_annual_reset," + F(soilAfter1) + "," + F(transportAfterReset) + ",0,0," + F(soilAfter1 + transportAfterReset) + "," + F(Math.Abs(totalAfter1 - (soilAfter1 + transportAfterReset)) / Math.Max(1.0,totalAfter1)) + "\n" +
                "after_annual_water_erosion," + F(soilAfterWater) + "," + F(transportAfterWater) + "," + F(boundaryExport) + "," + F(staleWaterTransportArrays) + "," + F(soilAfterWater + transportAfterWater) + "," + F(waterErosionClosure) + "\n" +
                "after_layer_maintenance," + F(soilAfterLayerMaintenance) + "," + F(persistentAfterLayerMaintenance) + "," + F(boundaryExport) + "," + F(staleWaterTransportArrays) + "," + F(totalAfterLayerMaintenance) + "," + F(layerMaintenanceClosure) + "\n" +
                "event2," + F(soilAfter2) + "," + F(transportAfter2) + ",0,0," + F(totalAfter2) + "," + F(closure2) + "\n";
            File.WriteAllText(Path.Combine(root, "residual_persistence.csv"), persistence);

            Console.WriteLine(
                "ROOT_CASE=" + scenario +
                " mixing_mode=" + mixingMode +
                " event1_residual_kg=" + transportAfter1.ToString("R") +
                " annual_flow_depth_m=" + sourceFlow.ToString("R") +
                " water_erosion_soil_loss_kg=" + soilLoss.ToString("R") +
                " boundary_export_kg=" + boundaryExport.ToString("R") +
                " source_erosion_m=" + waterErosion[0,0].ToString("R") +
                " interior_deposition_m=" + waterDeposition[1,1].ToString("R") +
                " persistent_after_water_kg=" + transportAfterWater.ToString("R") +
                " persistent_after_layer_maintenance_kg=" + persistentAfterLayerMaintenance.ToString("R") +
                " layer_maintenance_closure=" + layerMaintenanceClosure.ToString("R") +
                " event2_residual_kg=" + transportAfter2.ToString("R") +
                " event2_deposition_m=" + depositionSum2.ToString("R") +
                " water_closure=" + waterErosionClosure.ToString("R") +
                " event2_closure=" + closure2.ToString("R"));
        }
    }


    static void TestDailyflowGeneratedWaterErosion()
    {
        string root = Path.Combine(OutputRoot, "dailyflow_generated_water_erosion");
        if (Directory.Exists(root)) Directory.Delete(root, true);
        Directory.CreateDirectory(root);

        using (Mother_form f = BuildConvergentCase(root, 1, false))
        {
            const int nr = 5, nc = 5;
            double[,] dtm = new double[nr,nc];
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
                dtm[r,col] = 110.0;

            // A single source cell (1,1) has one lower neighbour (0,0),
            // which lies on the open model boundary. All other cells have
            // no rainfall excess, so the actual dailyflow routine generates
            // one controlled overland-flow path.
            dtm[1,1] = 100.0;
            dtm[0,0] = 90.0;
            Set(f, "dtm", dtm);
            Set(f, "t", 0);
            Set(f, "t_intervene", 0);
            Set(f, "index", new double[nr * nc]);
            Set(f, "rowcol_index", new string[nr * nc]);
            Call(f, "comb_sort");

            Set(f, "OFy_m", new double[nr,nc,10]);
            Set(f, "Ks_topsoil_m_h", new double[nr,nc]);
            Set(f, "Iy", new double[nr,nc]);
            Set(f, "pond_y", new double[nr,nc]);
            Set(f, "total_outflow_y", new double[nr,nc]);
            Set(f, "waterflow_m3", new double[nr,nc]);
            Set(f, "evapotranspiration", new double[nr,nc]);
            Set(f, "infil", new double[nr,nc]);
            Set(f, "sum_water_erosion", new double[nr,nc]);
            Set(f, "dz_ero_m", new double[nr,nc]);
            Set(f, "dz_sed_m", new double[nr,nc]);
            Set(f, "lake_sed_m", new double[nr,nc]);
            Set(f, "K_fac", new double[nr,nc]);
            Set(f, "bio_protection", new double[nr,nc]);

            double[,] ks = Get<double[,]>(f, "Ks_topsoil_m_h");
            double[,] kfac = Get<double[,]>(f, "K_fac");
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
            {
                ks[r,col] = 0.01;   // rainfall is absorbed in non-source cells
                kfac[r,col] = 1e-6;
            }
            ks[1,1] = 0.0;          // source generates runoff
            ks[0,0] = 0.0;          // boundary receiver carries inflow out

            Set(f, "upper_particle_size", new double[] { 0.01, 0.002, 0.00005, 0.000002, 0.0000001 });
            Set(f, "water_ero_active", true);
            Set(f, "erodibility_value_m", 1e-6);
            Set(f, "bio_protection_constant", 0.0);
            Set(f, "rock_protection_constant", 0.0);
            Set(f, "constant_selective_transcap", 0.0);
            Set(f, "erosion_threshold_kg", 0.0);
            Set(f, "m", 0.5);
            Set(f, "n", 1.0);
            Set(f, "rain_value_m", 0.01);
            Set(f, "evap_value_m", 0.0);
            Set(f, "infil_value_m", 0.0);
            Get<CheckBox>(f, "Water_ero_checkbox").Checked = true;
            Get<CheckBox>(f, "only_waterflow_checkbox").Checked = false;
            Get<CheckBox>(f, "daily_water").Checked = false;
            Get<CheckBox>(f, "version_lux_checkbox").Checked = false;

            double soilBefore = TotalSoilMass(f);

            // Actual LORICA runoff routing: 10 mm rainfall over 6 h.
            Call(f, "dailyflow", 0.01, 6.0, 0, 0, 0.0);
            double[,,] flow = Get<double[,,]>(f, "OFy_m");
            if (flow[1,1,1] <= 0.0)
                throw new Exception("dailyflow() did not generate the expected source-to-boundary flow direction.");

            // Actual daily water-erosion and sediment-routing kernel.
            Call(f, "calculate_water_ero_sed_daily");
            double soilAfter = TotalSoilMass(f);
            double transportAfter = TotalTransportMass(f);
            double soilLoss = soilBefore - soilAfter;
            double closure = Math.Abs(soilLoss - transportAfter) / Math.Max(1.0, soilBefore);
            double[,] erosion = Get<double[,]>(f, "dz_ero_m");
            if (erosion[1,1] >= 0.0)
                throw new Exception("dailyflow-generated water erosion did not erode its source cell.");
            if (transportAfter <= 0.0)
                throw new Exception("dailyflow-generated sediment did not reach the open boundary.");
            if (closure > 1e-6)
                throw new Exception("dailyflow-generated water-erosion export did not close mass: " + closure.ToString("R"));

            string summary =
                "source_flow_dir_1_m=" + flow[1,1,1].ToString("R") + Environment.NewLine +
                "soil_before_kg=" + soilBefore.ToString("R") + Environment.NewLine +
                "soil_after_kg=" + soilAfter.ToString("R") + Environment.NewLine +
                "soil_loss_kg=" + soilLoss.ToString("R") + Environment.NewLine +
                "boundary_transport_kg=" + transportAfter.ToString("R") + Environment.NewLine +
                "relative_mass_closure=" + closure.ToString("R") + Environment.NewLine +
                "source_erosion_m=" + erosion[1,1].ToString("R") + Environment.NewLine;
            File.WriteAllText(Path.Combine(root, "dailyflow_water_erosion_summary.txt"), summary);
            WriteAscii(Path.Combine(root, "dtm_m.asc"), Get<double[,]>(f, "dtm"));
            WriteAscii(Path.Combine(root, "flow_direction_1_m.asc"), new double[,] {
                { flow[0,0,1], flow[0,1,1], flow[0,2,1], flow[0,3,1], flow[0,4,1] },
                { flow[1,0,1], flow[1,1,1], flow[1,2,1], flow[1,3,1], flow[1,4,1] },
                { flow[2,0,1], flow[2,1,1], flow[2,2,1], flow[2,3,1], flow[2,4,1] },
                { flow[3,0,1], flow[3,1,1], flow[3,2,1], flow[3,3,1], flow[3,4,1] },
                { flow[4,0,1], flow[4,1,1], flow[4,2,1], flow[4,3,1], flow[4,4,1] }
            });
            WriteAscii(Path.Combine(root, "water_erosion_m.asc"), erosion);

            Console.WriteLine(
                "DAILYFLOW_WATER_EROSION_PASS source_flow_dir1_m=" + flow[1,1,1].ToString("R") +
                " soil_loss_kg=" + soilLoss.ToString("R") +
                " boundary_transport_kg=" + transportAfter.ToString("R") +
                " closure=" + closure.ToString("R"));
        }
    }


    static void TestAnnualWaterBalanceGeneratedWaterErosion()
    {
        string root = Path.Combine(OutputRoot, "annual_water_balance_generated_erosion");
        if (Directory.Exists(root)) Directory.Delete(root, true);
        Directory.CreateDirectory(root);

        using (Mother_form f = BuildConvergentCase(root, 1, false))
        {
            const int nr = 5, nc = 5, days = 365;
            double[,] dtm = new double[nr,nc];
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
                dtm[r,col] = 110.0;
            dtm[1,1] = 100.0;
            dtm[0,0] = 90.0;
            Set(f, "dtm", dtm);
            Set(f, "t", 1);                 // avoid annual solar/Ks recalculation in this isolated test
            Set(f, "t_intervene", 0);
            Set(f, "daily_weather_prepared_for_timestep", false);
            Set(f, "index", new double[nr * nc]);
            Set(f, "rowcol_index", new string[nr * nc]);
            Set(f, "rain_value_m", 0.01);
            Set(f, "temp_value_C", 10);

            int[] precipitation = new int[days];
            int[] duration = new int[days];
            int[] tmin = new int[days];
            int[] tavg = new int[days];
            int[] tmax = new int[days];
            precipitation[0] = 10;          // one 10-mm rainfall event
            duration[0] = 6;                // over six hours
            for (int day = 0; day < days; day++)
            {
                tmin[day] = 5;
                tavg[day] = 10;
                tmax[day] = 15;
            }
            Set(f, "P_all", precipitation);
            Set(f, "D_all", duration);
            Set(f, "Tmin_all", tmin);
            Set(f, "Tavg_all", tavg);
            Set(f, "Tmax_all", tmax);
            Get<TextBox>(f, "daily_n").Text = "1";
            Get<CheckBox>(f, "check_scaling_daily_weather").Checked = false;
            Get<CheckBox>(f, "check_time_rain").Checked = false;
            Get<CheckBox>(f, "daily_water").Checked = true;
            Get<CheckBox>(f, "Water_ero_checkbox").Checked = true;
            Get<CheckBox>(f, "Landslide_checkbox").Checked = true;
            Get<CheckBox>(f, "only_waterflow_checkbox").Checked = false;
            Get<CheckBox>(f, "version_lux_checkbox").Checked = false;

            Set(f, "OFy_m", new double[nr,nc,10]);
            Set(f, "waterflow_m3", new double[nr,nc]);
            Set(f, "Ks_topsoil_m_h", new double[nr,nc]);
            Set(f, "Ks_min_mh", 0.0001);
            Set(f, "Ra_rcm", new double[nr,nc,12]);
            Set(f, "veg_correction_factor", new double[nr,nc]);
            Set(f, "ETay", new double[nr,nc]);
            Set(f, "ET0y", new double[nr,nc]);
            Set(f, "Iy", new double[nr,nc]);
            Set(f, "pond_y", new double[nr,nc]);
            Set(f, "outflow_y", new double[nr,nc]);
            Set(f, "waterfactor", new double[nr,nc]);
            Set(f, "total_outflow_y", new double[nr,nc]);
            Set(f, "aridity_vegetation", new double[nr,nc]);
            Set(f, "evapotranspiration", new double[nr,nc]);
            Set(f, "infil", new double[nr,nc]);
            Set(f, "sum_water_erosion", new double[nr,nc]);
            Set(f, "dz_ero_m", new double[nr,nc]);
            Set(f, "dz_sed_m", new double[nr,nc]);
            Set(f, "lake_sed_m", new double[nr,nc]);
            Set(f, "K_fac", new double[nr,nc]);
            Set(f, "bio_protection", new double[nr,nc]);

            double[,] ks = Get<double[,]>(f, "Ks_topsoil_m_h");
            double[,] kfac = Get<double[,]>(f, "K_fac");
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
            {
                ks[r,col] = 0.01;           // non-source cells absorb the rainfall
                kfac[r,col] = 1e-6;
                Get<double[,]>(f, "veg_correction_factor")[r,col] = 1.0;
            }
            ks[1,1] = 0.0;                  // runoff source
            ks[0,0] = 0.0;                  // boundary receiver
            double[,,] radiation = Get<double[,,]>(f, "Ra_rcm");
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
            for (int mo = 0; mo < 12; mo++)
                radiation[r,col,mo] = 1e-6;

            Set(f, "upper_particle_size", new double[] { 0.01, 0.002, 0.00005, 0.000002, 0.0000001 });
            Set(f, "water_ero_active", true);
            Set(f, "erodibility_value_m", 1e-6);
            Set(f, "bio_protection_constant", 0.0);
            Set(f, "rock_protection_constant", 0.0);
            Set(f, "constant_selective_transcap", 0.0);
            Set(f, "erosion_threshold_kg", 0.0);
            Set(f, "m", 0.5);
            Set(f, "n", 1.0);

            // Actual annual water-balance routine prepares daily weather and
            // accumulates daily overland-flow directions into OFy_m.
            Call(f, "water_balance");
            double[,,] annualFlow = Get<double[,,]>(f, "OFy_m");
            double sourceFlow = annualFlow[1,1,1];
            if (sourceFlow <= 0.0)
                throw new Exception("water_balance() did not generate annual source-to-boundary overland flow.");

            // Match every_timestep(): annual hydrology first, then annual reset,
            // cell re-sort, and daily sediment-erosion kernel.
            Call(f, "initialise_every");
            Set(f, "index", new double[nr * nc]);
            Call(f, "comb_sort");
            double soilBefore = TotalSoilMass(f);
            Call(f, "calculate_water_ero_sed_daily");
            double soilAfter = TotalSoilMass(f);
            double transportAfter = TotalTransportMass(f);
            double soilLoss = soilBefore - soilAfter;
            double closure = Math.Abs(soilLoss - transportAfter) / Math.Max(1.0, soilBefore);
            double[,] erosion = Get<double[,]>(f, "dz_ero_m");

            if (erosion[1,1] >= 0.0)
                throw new Exception("Annual water-balance flow did not erode the source cell.");
            if (transportAfter <= 0.0)
                throw new Exception("Annual water-balance sediment did not reach the open boundary.");
            if (closure > 1e-6)
                throw new Exception("Annual water-balance water-erosion mass closure failed: " + closure.ToString("R"));

            string summary =
                "annual_rainfall_m=" + Get<double>(f, "rain_value_m").ToString("R") + Environment.NewLine +
                "source_flow_direction_m=" + sourceFlow.ToString("R") + Environment.NewLine +
                "soil_before_kg=" + soilBefore.ToString("R") + Environment.NewLine +
                "soil_after_kg=" + soilAfter.ToString("R") + Environment.NewLine +
                "soil_loss_kg=" + soilLoss.ToString("R") + Environment.NewLine +
                "boundary_transport_kg=" + transportAfter.ToString("R") + Environment.NewLine +
                "relative_mass_closure=" + closure.ToString("R") + Environment.NewLine +
                "source_erosion_m=" + erosion[1,1].ToString("R") + Environment.NewLine;
            File.WriteAllText(Path.Combine(root, "annual_water_balance_erosion_summary.txt"), summary);
            Console.WriteLine(
                "ANNUAL_WATER_BALANCE_EROSION_PASS source_flow_m=" + sourceFlow.ToString("R") +
                " soil_loss_kg=" + soilLoss.ToString("R") +
                " boundary_transport_kg=" + transportAfter.ToString("R") +
                " closure=" + closure.ToString("R"));
        }
    }


    static void TestTreedSameYearRootCohesion()
    {
        string couplingDir = Environment.GetEnvironmentVariable("LORICA_TREED_COUPLING_DIR");
        if (String.IsNullOrWhiteSpace(couplingDir) ||
            !File.Exists(Path.Combine(couplingDir, "TREED_coupling.cfg")))
            throw new Exception("Actual TREED coupling directory/config was not provided to the process test.");

        string root = Path.Combine(OutputRoot, "treed_same_year_rootcohesion");
        if (Directory.Exists(root)) Directory.Delete(root, true);
        Directory.CreateDirectory(root);

        using (Mother_form f = BuildConvergentCase(root, 1, false))
        {
            const int nr = 5, nc = 5, days = 365;
            Set(f, "t", 0);
            Set(f, "run_number", 9002);
            Set(f, "workdir", root);
            Set(f, "daily_weather_prepared_for_timestep", false);
            Set(f, "rain_value_m", 0.73);
            Set(f, "temp_value_C", 10);
            Set(f, "veg_correction_factor", new double[nr,nc]);
            Set(f, "aridity_vegetation", new double[nr,nc]);

            int[] precipitation = new int[days];
            int[] duration = new int[days];
            int[] tmin = new int[days];
            int[] tavg = new int[days];
            int[] tmax = new int[days];
            for (int day = 0; day < days; day++)
            {
                precipitation[day] = 2; // 2 mm/day; 730 mm/year
                duration[day] = 6;
                tmin[day] = 5;
                tavg[day] = 10;
                tmax[day] = 15;
            }
            Set(f, "P_all", precipitation);
            Set(f, "D_all", duration);
            Set(f, "Tmin_all", tmin);
            Set(f, "Tavg_all", tavg);
            Set(f, "Tmax_all", tmax);
            Get<TextBox>(f, "daily_n").Text = "1";
            Get<CheckBox>(f, "check_scaling_daily_weather").Checked = false;
            Get<CheckBox>(f, "check_time_rain").Checked = false;

            // Prepare the actual LORICA daily weather first. run_treed_coupling()
            // must export these same-year arrays to the TREED monthly climate file.
            Call(f, "prepare_daily_weather_for_current_timestep");
            double[] py = Get<double[]>(f, "Py");
            int[] tavgy = Get<int[]>(f, "Tavgy");
            int[] monthDays = Get<int[]>(f, "month");

            Call(f, "run_treed_coupling");

            string exchangeRoot = Path.Combine(root, "TREED_exchange_run_9002");
            string yearDir = Path.Combine(exchangeRoot, "0001");
            string inputDir = Path.Combine(yearDir, "input");
            string outputDir = Path.Combine(yearDir, "output");
            string rootCPath = Path.Combine(outputDir, "treed_rootC_areanorm_gC_m2.asc");
            string fpcPath = Path.Combine(outputDir, "treed_fpc.asc");
            string laiPath = Path.Combine(outputDir, "treed_lai.asc");
            string climatePath = Path.Combine(inputDir, "treed_climate_monthly.csv");
            string summaryPath = Path.Combine(outputDir, "treed_rootcohesion_summary.csv");
            if (!File.Exists(rootCPath) || !File.Exists(fpcPath) ||
                !File.Exists(laiPath) || !File.Exists(climatePath) ||
                !File.Exists(summaryPath))
                throw new Exception("Actual TREED roundtrip did not produce all required output rasters and audit files.");

            double[,] rootC = ReadAsciiGrid(rootCPath);
            double[,] fpc = ReadAsciiGrid(fpcPath);
            double[,] rootCohesion = Get<double[,]>(f, "root_cohesion_kPa_new");
            double[,] cover = Get<double[,]>(f, "aridity_vegetation");
            double[,] et = Get<double[,]>(f, "veg_correction_factor");
            const double TrMpa = 17.284220625;
            const double fCarbon = 0.47;
            const double rhoRoot = 435.3;
            const double K = 1.2;
            double maxFormulaError = 0.0;
            double maxCoverError = 0.0;
            double maxEtError = 0.0;
            double rootCMax = 0.0;
            double coverMax = 0.0;
            int validCells = 0;

            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
            {
                if (rootC[r,col] == -9999.0 || fpc[r,col] == -9999.0) continue;
                double expectedRootCohesion = Math.Max(0.0,
                    K * (TrMpa * 1e6) * ((Math.Max(0.0, rootC[r,col]) / (1000.0 * fCarbon)) / rhoRoot) / 1000.0);
                double expectedEt = 1.0 + Math.Max(0.0, Math.Min(1.0, fpc[r,col])) * (0.85 - 1.0);
                maxFormulaError = Math.Max(maxFormulaError, Math.Abs(rootCohesion[r,col] - expectedRootCohesion));
                maxCoverError = Math.Max(maxCoverError, Math.Abs(cover[r,col] - fpc[r,col]));
                maxEtError = Math.Max(maxEtError, Math.Abs(et[r,col] - expectedEt));
                rootCMax = Math.Max(rootCMax, rootC[r,col]);
                coverMax = Math.Max(coverMax, fpc[r,col]);
                validCells++;
            }

            if (validCells != nr * nc)
                throw new Exception("TREED output contains unexpected nodata cells in the local test domain.");
            if (rootCMax <= 0.0 || coverMax <= 0.0)
                throw new Exception("Actual TREED run returned no positive root carbon or vegetation cover.");
            if (maxFormulaError > 1e-8 || maxCoverError > 1e-8 || maxEtError > 1e-8)
                throw new Exception("TREED-to-LORICA root cohesion/FPC/ET transfer failed its numerical audit.");

            // Confirm that the monthly climate sent to TREED is the same-year
            // aggregation of LORICA's prepared daily arrays.
            string[] climateLines = File.ReadAllLines(climatePath);
            if (climateLines.Length != 13)
                throw new Exception("TREED same-year climate file must contain 12 monthly records.");
            int day0 = 0;
            double maxClimateError = 0.0;
            for (int mo = 0; mo < 12; mo++)
            {
                double pmm = 0.0, tmean = 0.0;
                for (int d = 0; d < monthDays[mo]; d++)
                {
                    pmm += py[day0 + d] * 1000.0;
                    tmean += tavgy[day0 + d];
                }
                tmean /= monthDays[mo];
                string[] fields = climateLines[mo + 1].Split(',');
                double actualT = Double.Parse(fields[1], CultureInfo.InvariantCulture);
                double actualP = Double.Parse(fields[2], CultureInfo.InvariantCulture);
                maxClimateError = Math.Max(maxClimateError, Math.Abs(actualT - tmean));
                maxClimateError = Math.Max(maxClimateError, Math.Abs(actualP - pmm));
                day0 += monthDays[mo];
            }
            if (maxClimateError > 1e-8)
                throw new Exception("TREED monthly climate does not match the same-year LORICA daily weather.");

            // Next integration gate: use the TREED-derived spatial root-cohesion
            // raster in LORICA's actual critical-rainfall and landslide routines.
            Dictionary<string,string> eventCfg = new Dictionary<string,string>();
            eventCfg["landslide_event_mode"] = "explicit_event";
            eventCfg["landslide_event_rainfall_mm"] = "60";
            eventCfg["landslide_event_duration_h"] = "6";
            Call(f, "configure_treed_landslide_event", eventCfg);

            double[,] treedRootMap = (double[,])rootCohesion.Clone();
            double rootMean = 0.0, rootMin = Double.PositiveInfinity, rootMax = Double.NegativeInfinity;
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
            {
                double v = treedRootMap[r,col];
                rootMean += v;
                rootMin = Math.Min(rootMin, v);
                rootMax = Math.Max(rootMax, v);
            }
            rootMean /= validCells;

            // Compare the actual TREED spatial map with a spatially uniform map
            // having the same mean. This isolates the contribution of spatial
            // variation from the effect of the overall root-cohesion magnitude.
            double[,] uniformRootMap = new double[nr,nc];
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
                uniformRootMap[r,col] = rootMean;
            Set(f, "root_cohesion_kPa_new", uniformRootMap);
            Call(f, "calc_and_write_ls_rasters");
            double[,] uniformCohesionFactor = (double[,])Get<double[,]>(f, "Cohesion_factor").Clone();
            double[,] uniformCriticalRain = (double[,])Get<double[,]>(f, "crrain_m_d").Clone();

            Set(f, "root_cohesion_kPa_new", treedRootMap);
            Call(f, "calc_and_write_ls_rasters");
            double[,] treedCohesionFactor = (double[,])Get<double[,]>(f, "Cohesion_factor").Clone();
            double[,] treedCriticalRain = (double[,])Get<double[,]>(f, "crrain_m_d").Clone();

            double maxSpatialFactorDifference = 0.0;
            int treedUnstableThresholdCells = 0;
            int uniformUnstableThresholdCells = 0;
            for (int r = 0; r < nr; r++)
            for (int col = 0; col < nc; col++)
            {
                maxSpatialFactorDifference = Math.Max(
                    maxSpatialFactorDifference,
                    Math.Abs(treedCohesionFactor[r,col] - uniformCohesionFactor[r,col]));
                if (treedCriticalRain[r,col] >= 0.0) treedUnstableThresholdCells++;
                if (uniformCriticalRain[r,col] >= 0.0) uniformUnstableThresholdCells++;
            }
            if (maxSpatialFactorDifference <= 0.0)
                throw new Exception("LORICA did not retain the spatial variation in TREED root cohesion.");

            // Run the actual event with the TREED root map.
            double treedMassBefore = TotalSoilMass(f);
            Call(f, "calculate_slide_new");
            int treedInitiations = Get<int>(f, "landslide_initiation_cells");
            double treedErosion = SumAbs(Get<double[,]>(f, "ero_slid_m"));
            double treedMassAfter = TotalSoilMass(f);
            double treedTransport = TotalTransportMass(f);
            double treedMassClosure = Math.Abs(treedMassBefore - treedMassAfter - treedTransport)
                                    / Math.Max(1.0, treedMassBefore);
            if (treedMassClosure > 1e-6)
                throw new Exception("TREED-root landslide event mass closure failed: " + treedMassClosure.ToString("R"));

            // Paired bare-root control: identical terrain, soil profile, event,
            // routing mode, and rainfall, changing only the root-cohesion map.
            int bareInitiations;
            double bareErosion, bareMassClosure;
            int bareUnstableThresholdCells;
            using (Mother_form bare = BuildConvergentCase(Path.Combine(root, "bare_root_control"), 1, false))
            {
                Set(bare, "root_cohesion_kPa_new", new double[nr,nc]);
                Call(bare, "configure_treed_landslide_event", eventCfg);
                double bareMassBefore = TotalSoilMass(bare);
                Call(bare, "calc_and_write_ls_rasters");
                double[,] bareCriticalRain = Get<double[,]>(bare, "crrain_m_d");
                bareUnstableThresholdCells = 0;
                for (int r = 0; r < nr; r++)
                for (int col = 0; col < nc; col++)
                    if (bareCriticalRain[r,col] >= 0.0) bareUnstableThresholdCells++;
                Call(bare, "calculate_slide_new");
                bareInitiations = Get<int>(bare, "landslide_initiation_cells");
                bareErosion = SumAbs(Get<double[,]>(bare, "ero_slid_m"));
                double bareMassAfter = TotalSoilMass(bare);
                double bareTransport = TotalTransportMass(bare);
                bareMassClosure = Math.Abs(bareMassBefore - bareMassAfter - bareTransport)
                                / Math.Max(1.0, bareMassBefore);
            }

            if (bareInitiations <= treedInitiations || bareErosion <= treedErosion)
                throw new Exception("TREED root cohesion did not reduce landslide initiation and erosion relative to the paired bare-root control.");
            if (bareMassClosure > 1e-6)
                throw new Exception("Bare-root control landslide mass closure failed: " + bareMassClosure.ToString("R"));

            string stabilitySummary =
                "TREED_ROOT_MAP_MEAN_KPA=" + rootMean.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "TREED_ROOT_MAP_MIN_KPA=" + rootMin.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "TREED_ROOT_MAP_MAX_KPA=" + rootMax.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "MAX_COHESION_FACTOR_DIFFERENCE_VS_UNIFORM=" + maxSpatialFactorDifference.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "TREED_UNSTABLE_THRESHOLD_CELLS=" + treedUnstableThresholdCells.ToString(CultureInfo.InvariantCulture) + Environment.NewLine +
                "UNIFORM_UNSTABLE_THRESHOLD_CELLS=" + uniformUnstableThresholdCells.ToString(CultureInfo.InvariantCulture) + Environment.NewLine +
                "BARE_UNSTABLE_THRESHOLD_CELLS=" + bareUnstableThresholdCells.ToString(CultureInfo.InvariantCulture) + Environment.NewLine +
                "EVENT_INTENSITY_M_DAY=" + Get<double>(f, "treed_landslide_event_intensity_m_d").ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "TREED_INITIATIONS=" + treedInitiations.ToString(CultureInfo.InvariantCulture) + Environment.NewLine +
                "BARE_INITIATIONS=" + bareInitiations.ToString(CultureInfo.InvariantCulture) + Environment.NewLine +
                "TREED_EROSION_M=" + treedErosion.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "BARE_EROSION_M=" + bareErosion.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "TREED_MASS_CLOSURE=" + treedMassClosure.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "BARE_MASS_CLOSURE=" + bareMassClosure.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine;
            File.WriteAllText(Path.Combine(root, "TREED_LANDSLIDE_STABILITY_PASS.txt"), stabilitySummary);
            Console.WriteLine("TREED_LANDSLIDE_STABILITY_PASS " + stabilitySummary.Replace(Environment.NewLine, " "));

            string marker = Path.Combine(root, "TREED_SAME_YEAR_ROOTCOHESION_PASS.txt");
            File.WriteAllText(marker,
                "TREED_ACTUAL_JULIA_TO_LORICA_CSHARP=PASS" + Environment.NewLine +
                "valid_cells=" + validCells.ToString(CultureInfo.InvariantCulture) + Environment.NewLine +
                "rootC_max_gC_m2=" + rootCMax.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "FPC_max=" + coverMax.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "max_Hwang_formula_error_kPa=" + maxFormulaError.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "max_FPC_transfer_error=" + maxCoverError.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "max_ET_factor_error=" + maxEtError.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine +
                "max_same_year_climate_error=" + maxClimateError.ToString("R", CultureInfo.InvariantCulture) + Environment.NewLine);
            Console.WriteLine("TREED_SAME_YEAR_ROOTCOHESION_PASS " + File.ReadAllText(marker).Replace(Environment.NewLine, " "));
        }
    }

    [STAThread]
    public static void Main(string[] args)
    {
        if (args.Length != 1) throw new Exception("Usage: LoricaTreedLandslideSmoke.exe OUTPUT_DIR");
        OutputRoot = Path.GetFullPath(args[0]);
        Directory.CreateDirectory(OutputRoot);
        TestRainfallTimeSeries(OutputRoot);
        TestEventConfig();

        // The 60 mm / 6 h storm is 10 mm/h = 0.24 m/day.
        // Root cohesion of 0 and 4.3 kPa should permit failure on the synthetic
        // 45-degree, 1-m soil slope; 7.6 kPa should stabilize it.
        TestRootCohesionCase("bare_complete", 0.0, true, 1);
        TestRootCohesionCase("intermediate_complete", 4.3, true, 1);
        TestRootCohesionCase("high_complete", 7.6, false, 1);

        // Active alternative: layer-preserving translation mode.
        TestRootCohesionCase("bare_translation", 0.0, true, 2);
        TestRootCohesionCase("intermediate_translation", 4.3, true, 2);
        TestRootCohesionCase("high_translation", 7.6, false, 2);

        // A 2-D radial bowl receives material from eight surrounding source
        // cells. Its internal depression has enough capacity to retain the
        // event material, so no open-boundary export is expected.
        Test2DConvergentCase("convergent_2d_complete", 1);
        Test2DConvergentCase("convergent_2d_translation", 2);
        Test2DClosedSinkResidualCase("closed_sink_residual_complete", 1);
        Test2DClosedSinkResidualCase("closed_sink_residual_translation", 2);
        TestResidualPersistenceAcrossTimesteps("residual_persistence_complete", 1);
        TestResidualPersistenceAcrossTimesteps("residual_persistence_translation", 2);
        TestDailyflowGeneratedWaterErosion();
        TestAnnualWaterBalanceGeneratedWaterErosion();
        TestTreedSameYearRootCohesion();

        File.WriteAllText(Path.Combine(OutputRoot, "LORICA_TREED_V09_LANDSLIDE_SMOKE_PASS.txt"),
            "LORICA_TREED_V09_LANDSLIDE_SMOKE_PASS" + Environment.NewLine);
        Console.WriteLine("LORICA_TREED_V09_LANDSLIDE_SMOKE_PASS");
    }
}
