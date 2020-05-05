# First I am importing the necessary modules and creating a list that defines the variables I will be working with

import os, arcpy
arcpy.CheckOutExtension("Spatial")
listMonths = ["02", "04", "05", "07", "10", "11"]


# CHANGE DIRECTORY HERE, I am also making an output directory for all the NDVI files to be stored. 

directory = r"Z:\Downloads\KMK_Python\KMK_Python\Class6\Step_3_data_lfs"
outputDirectory = os.path.join(directory, "NDVIoutput")
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)


# I am creating a loop that will go through each month folder and isolate the the B4 and B5 band files into lists

for month in listMonths:
    print "Creating NDVI for " + month
    arcpy.env.workspace = os.path.join(directory, "2015" + month)
    B4 = arcpy.ListRasters("*", "TIF")
    B4 = [x for x in B4 if "B4" in x]
    B5 = arcpy.ListRasters("*", "TIF")
    B5 = [x for x in B5 if "B5" in x]
    print B5
    print B4
    
# Under the same loop, I am using the raster calculator tool to perform the NDVI calculation by referencing the B4 and B5 lists    

    input = 'Float("' + B5[0] + '" - "' + B4[0] + '") / Float("' + B5[0] + '" + "' + B4[0] + '")'
    print input
    arcpy.gp.RasterCalculator_sa(input, os.path.join(outputDirectory, "NDVI2015" + month + ".tif"))
    
print "NDVIs completed"
