# In this coding challenge, your objective is to utilize the radiating lines code used in class "9_Cursors" to take an
# input of sites from a provided Shapefile (Site_Locations.zip), use the radiating lines code to calculate "fetch
# distances" for each 10 degree bearing in a manner that originated from Davies & Johnson (2006). Finally, clip the
# resulting fetch lines by the NB_Coastline.zip shapefile, and report the mean plus standard deviation of the fetch
# distance for each site: 9 sites, A1....C3 in meters. We don't have wind data so can't calculate the estimate as
# accurately as in Davies & Johnson (2006).

import arcpy, os
from math import radians, sin, cos
arcpy.env.workspace = r"C:\Course_ArcGIS_Python_Students\Python-NRS568\Class 9"
arcpy.env.overwriteOutput = True


# Extract coordinates from point shp file
input_shp = 'Site_Locations.shp'
fields = ['SHAPE@XY', 'Site_Code']

input_locations = []
with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    for row in cursor:
        input_locations.append(row)
print input_locations


# Find spref of site location file in order to create radiating line with same coordinate system
sp_ref = arcpy.Describe(input_shp).spatialReference.factoryCode
print sp_ref

stats_list = []

# Radiating line new shape file code
for i in input_locations:
    out_path = arcpy.env.workspace
    out_name = "radiating_lines_" + i[1] + ".shp"
    geometry_type = "POLYLINE"
    template = "#"
    has_m = "DISABLED"
    has_z = "DISABLED"

    spatial_ref = 32130

    arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                        has_m, has_z, spatial_ref)

    origin_x, origin_y = i[0][0], i[0][1]
    distance = 100000
    angle = 10

    OutputFeature = os.path.join(out_path, out_name)
    OutFeat = out_name

    angles = range(0, 360, angle)

    for ang in angles:
        # calculate offsets with  trig
        angle = float(int(ang))
        (disp_x, disp_y) = (distance * sin(radians(angle)), distance * cos(radians(angle)))
        (end_x, end_y) = (origin_x + disp_x, origin_y + disp_y)
        (end2_x, end2_y) = (origin_x + disp_x, origin_y + disp_y)

        cur = arcpy.InsertCursor(OutFeat)
        lineArray = arcpy.Array()

        start = arcpy.Point()
        (start.ID, start.X, start.Y) = (1, origin_x, origin_y)
        lineArray.add(start)

        end = arcpy.Point()
        (end.ID, end.X, end.Y) = (2, end_x, end_y)
        lineArray.add(end)

        feat = cur.newRow()
        feat.shape = lineArray
        cur.insertRow(feat)

        lineArray.removeAll()
        del cur

        print "Radiating Lines shapefile created successfully"


    # Clip radiating line to coast
    in_features = OutFeat
    clip_features = "NB_Coastline.shp"
    out_feature_class = os.path.join(out_path, "RadLines_clip" + i[1] + ".shp")
    xy_tolerance = ""

    arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)
    print "Clip features complete for " + i[1]


    # Split broken up radiating lines into individual lines
    multi_input = out_feature_class
    multi_output = os.path.join(out_path, "Fetch_Lines_" + i[1] + ".shp")

    arcpy.MultipartToSinglepart_management(multi_input, multi_output)
    print "Radiating lines split"


    # Creating buffer around each point in order to include lines only intersecting with points
    sites = arcpy.MakeFeatureLayer_management("Site_Locations.shp")

    query = '"Site_Code"' + " = " + "'" + i[1] + "'"
    print query

    arcpy.SelectLayerByAttribute_management(sites, "NEW_SELECTION", query)

    in_feature_class = sites
    out_feature_class = os.path.join(out_path, "Buffer_" + i[1] + ".shp")
    buffer_distance = "10 Meters"
    line_side = "FULL"
    line_end_type = "ROUND"
    dissolve_option = "NONE"
    dissolve_field = ""
    method = "PLANAR"

    arcpy.Buffer_analysis(in_feature_class, out_feature_class, buffer_distance, line_side, line_end_type,
                          dissolve_option, dissolve_field, method)
    print "Buffer features created"


    # Select fetch lines interesting with site point buffer
    arcpy.MakeFeatureLayer_management(multi_output, "fetch_lines")
    arcpy.MakeFeatureLayer_management(out_feature_class, "pt_buffer")

    arcpy.SelectLayerByLocation_management("fetch_lines", "INTERSECT", "pt_buffer", "", "NEW_SELECTION", "NOT_INVERT")

    arcpy.CopyFeatures_management("fetch_lines", "Final_FetchLines_" + i[1] + ".shp")


    # Add geometry attribute to fetch lines in order to calculate distance
    in_geo = "Final_FetchLines_" + i[1] + ".shp"
    properties = "LENGTH"
    length_unit = ""
    area_unit = ""
    coordinate_system = ""

    arcpy.AddGeometryAttributes_management(in_geo, properties, length_unit, area_unit, coordinate_system)


    # Create stats table using search cursor
    in_table = in_geo
    out_table = "stats_table" + i[1] + ".dbf"
    stat_fields = [['LENGTH', 'SUM'], ['LENGTH', 'STD']]

    arcpy.Statistics_analysis(in_table, out_table, stat_fields, '')

    stats_list.append("stats_table" + i[1] + ".dbf")

# Generate Stats
for item in stats_list:
    with arcpy.da.SearchCursor(item, ['FREQUENCY', 'SUM_LENGTH', 'STD_LENGTH']) as cursor:
        print item
        for row in cursor:
            print(row)
