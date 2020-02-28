# 1. The two input species data must be in a SINGLE CSV file, you must process the input data to separate out the species
# (Hint: You can a slightly edited version of our CSV code from a previous session to do this), I recommend downloading
# the species data from the same source so the columns match.
# 2. Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer, and you
# provide the species data along with your Python code.
# 3. The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
# 4. You leave no trace of execution, except the resulting heatmap files.
# 5. You provide print statements that explain what the code is doing, e.g. Fishnet file generated.


# First I am importing my languages and setting my environment as well as overriding any output files that
# are duplicates from running the program multiple times.
import arcpy
import csv
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"E:\KMK_Python\Challenge5"
workspace = r"E:\KMK_Python\Challenge5"

# Creating an empty species list to populate with a loop clause from imported csv.
species_list = []

with open("Crab_Species.csv") as species_csv:
    csv_reader = csv.reader(species_csv, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count != 0:
            if row[0] not in species_list:
                species_list.append(row[0])
        if line_count == 0:
            print "Columns: " + str(row)
            line_count += 1
        line_count += 1

print species_list
print("Processed " + str(line_count) + " lines.")


# I am looping the csv through the species list and if the species name is the same the program will split the csv
# into as many files as species present.
for x in species_list:
    with open("Crab_Species.csv") as species_csv:
        csv_reader = csv.reader(species_csv, delimiter=',')
        file = open(x[0:4] + ".csv", "w")
        file.write("scientificName,decimalLongitude,decimalLatitude\n")
        for row in csv_reader:
            if row[0] == x:

                string = ",".join(row)
                string = string + "\n"
                file.write(string)


# While still under the initial species loop, I am creating a shp file for each of the split species csv files.
for x in species_list:
    in_Table = x[0:4] + ".csv"
    x_coords = "decimalLongitude"
    y_coords = "decimalLatitude"
    z_coords = ""
    out_Layer = x[0:4] + "_data"
    saved_Layer = x[0:4] + ".shp"

    spRef = arcpy.SpatialReference(4326)
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
    arcpy.CopyFeatures_management(lyr, saved_Layer)

    if arcpy.Exists(saved_Layer):
        print "Created shape file successfully!"
    else:
        print "Error"


# Next, identify the spatial coordinates of each shp file in order to produce fishnets
    desc = arcpy.Describe(x[0:4] + ".shp")
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

    print("Extent:\n YMin: {0},\n YMax: {1},\n XMin: {2},\n XMax: {3}".format(desc.extent.YMin, desc.extent.YMax,
                                                                              desc.extent.XMin, desc.extent.XMax))


# Creating fishnets still within the initial loop therefore for each shape file there will be a fishnet.
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

    outFeatureClass = x[0:4] + "_Fishnet.shp"

    originCoordinate = str(XMin) + " " + str(YMin)
    yAxisCoordinate = str(XMin) + " " + str(YMin + 10)
    cellSizeWidth = "2"
    cellSizeHeight = "2"
    numRows = ""
    numColumns = ""
    oppositeCorner = str(XMax) + " " + str(YMax)
    labels = "NO_LABELS"
    templateExtent = "#"
    geometryType = "POLYGON"

    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                                   cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                   oppositeCorner, labels, templateExtent, geometryType)

# Making sure the files were created
    if arcpy.Exists(outFeatureClass):
        print "Created Fishnet file successfully!"

# Join the fishnet with the distribution in order to produce a heatmap again all under the same loop so that the
# program will run through twice for each species.
    target_features = x[0:4] + "_Fishnet.shp"
    join_features = x[0:4] + ".shp"
    out_feature_class = x[0:4] + "_heatmap.shp"
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

# To make sure the heatmap was created
    if arcpy.Exists(out_feature_class):
        print "Created Heatmap file successfully!"

# Deleting the intermediate files with proof that they were created by the if acpy.exists commands.
     print "Deleting intermediate files"
     arcpy.Delete_management(target_features)
     arcpy.Delete_management(join_features)