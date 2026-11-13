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

    static void Test2DLimitedCapacityCase(string scenario, int mixingMode)
    {
        string root = Path.Combine(OutputRoot, scenario);
        if (Directory.Exists(root)) Directory.Delete(root, true);
        Directory.CreateDirectory(root);

        using (Mother_form f = BuildConvergentCase(root, mixingMode, true))
        {
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
                throw new Exception("Limited-capacity basin must have eight zero-threshold source cells; found " + zeroThresholdCells);

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
                throw new Exception("Limited-capacity basin should receive eight failed source cells.");
            for (int r = 0; r < 5; r++)
            for (int col = 0; col < 5; col++)
            {
                double dr = r - 2.0;
                double dc = col - 2.0;
                double distance = Math.Sqrt(dr * dr + dc * dc);
                bool sourceCell = (distance > 0.0 && distance <= Math.Sqrt(2.0) + 1e-9 &&
                    !(r == 3 && col == 2)) || (r == 0 && col == 2);
                if (sourceCell && erosion[r,col] >= -1e-8)
                    throw new Exception("Expected erosion in limited-capacity source cell at " + r + "," + col);
                if (!sourceCell && Math.Abs(erosion[r,col]) > 1e-8)
                    throw new Exception("Unexpected erosion outside limited-capacity source cells at " + r + "," + col);
                if (!(r == 2 && col == 2) && deposition[r,col] > 1e-8)
                    throw new Exception("Limited-capacity deposit escaped the internal bowl at " + r + "," + col);
            }

            double[,] finalDtm = Get<double[,]>(f, "dtm");
            if (Math.Abs(finalDtm[2,2] - 57.5) > 1e-5)
                throw new Exception("The internal basin should fill exactly to its 57.5-m spill elevation; got " + finalDtm[2,2].ToString("R"));
            if (deposition[2,2] <= 0.0 || transport <= 1e-6)
                throw new Exception("The limited-capacity basin should retain residual material in transport storage.");
            if (closure > 1e-6)
                throw new Exception("Limited-capacity basin mass closure failed: " + closure.ToString("R"));

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
        Test2DLimitedCapacityCase("limited_basin_complete", 1);
        Test2DLimitedCapacityCase("limited_basin_translation", 2);

        File.WriteAllText(Path.Combine(OutputRoot, "LORICA_TREED_V09_LANDSLIDE_SMOKE_PASS.txt"),
            "LORICA_TREED_V09_LANDSLIDE_SMOKE_PASS" + Environment.NewLine);
        Console.WriteLine("LORICA_TREED_V09_LANDSLIDE_SMOKE_PASS");
    }
}
