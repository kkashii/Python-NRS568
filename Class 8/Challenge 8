# I am creating a function that will identify all the necessary files needed for an NDVI (B4 and B5) by excluding all the other bands
# The data I used is from class 6, Step 3 data, choose any folder
# The result will print how many files are availible for NDVI (should always be 2) and what those files are ending in .tif

import arcpy

def checkNDVI(a, b):
    arcpy.env.workspace = a
    rasterList = arcpy.ListRasters("*", b)
    rasterList = [x for x in rasterList if "_B1.tif" not in x]
    rasterList = [x for x in rasterList if "_B2.tif" not in x]
    rasterList = [x for x in rasterList if "_B3.tif" not in x]
    rasterList = [x for x in rasterList if "_B6.tif" not in x]
    rasterList = [x for x in rasterList if "_B7.tif" not in x]
    rasterList = [x for x in rasterList if "_B8.tif" not in x]
    rasterList = [x for x in rasterList if "_B9.tif" not in x]
    rasterList = [x for x in rasterList if "_B10.tif" not in x]
    rasterList = [x for x in rasterList if "_B11.tif" not in x]
    rasterList = [x for x in rasterList if "_BQA.tif" not in x]
    print "There are " + str(len(rasterList)) + " files ready for NDVI"
    print "Files for NDVI processing: " + str(rasterList)


checkNDVI(ENTER WORKSPACE HERE, "TIF")
print "Function Complete"

# Not sure if there is an easier way to exclude all those bands. 
# If wrote rasterList = [x for x in rasterList if "_B4.tif" in x], the rasterList is empty. 

