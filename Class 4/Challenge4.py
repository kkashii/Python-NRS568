import arcpy

# These steps are part of a lab for my Advanced GIS Analysis class. Thought it would be cool to put it in
# practical use and try to do my homework by coding B-)

# Variables:
HUC12_RI_09_shp = "E:\\NRS522\\NRS_522\\HUC12_RI_09\\HUC12_RI_09.shp"
towns_shp = "E:\\NRS522\\NRS_522\\Data\\towns.shp"
wetland_clip_shp = "E:\\NRS522\\wetland_clip.shp"
wetland_dissolve_shp = "E:\\NRS522\\wetland_dissolve.shp"
wetland_dissolve_shp__2_ = wetland_dissolve_shp
wetland_dissolve_shp__3_ = wetland_dissolve_shp__2_

# Clip the wetland features to the RI boundary
arcpy.Clip_analysis(HUC12_RI_09_shp, towns_shp, wetland_clip_shp, "")

# Dissolve watershed features of the same ID number under field HUC_12
arcpy.Dissolve_management(wetland_clip_shp, wetland_dissolve_shp, "HUC_12", "", "MULTI_PART", "DISSOLVE_LINES")

# Add Field to the dissolved watershed shape file called 'Basin Area'
arcpy.AddField_management(wetland_dissolve_shp, "Basin_area", "FLOAT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Calculate area under 'Basin Area' in hectares
arcpy.CalculateField_management(wetland_dissolve_shp__2_, "Basin_area", "!Shape.area@hectares!", "VB", "")

