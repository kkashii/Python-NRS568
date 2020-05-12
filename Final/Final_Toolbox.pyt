import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "KOS_Final_Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [DEM, NDVI, Buffer]


class DEM(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "LAS Dataset to DEM"
        self.description = "This tool will convert an LAS Dataset to a Digital Elevation Model (DEM)"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_LAS = arcpy.Parameter(name="input_LAS",
                                     displayName="Input Ground Return LAS",
                                     datatype="DELasDataset",
                                     parameterType="Required",
                                     direction="Input")
        params.append(input_LAS)
        output = arcpy.Parameter(name="output",
                                 displayName="Output DEM",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",
                                 direction="Output")
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_LAS = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.LasDatasetToRaster_conversion(
            in_las_dataset=input_LAS,
            out_raster=output, value_field="ELEVATION",
            interpolation_type="BINNING AVERAGE LINEAR", data_type="FLOAT", sampling_type="CELLSIZE",
            sampling_value="1", z_factor="1")
        arcpy.AddMessage("DEM created!")
        return


class NDVI(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "NDVI"
        self.description = "This tool will create an NDVI by simply inputting the location of the folder containing the band rasters."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_files = arcpy.Parameter(name="input_files",
                                     displayName="Input Folder Destination",
                                     datatype="DEFolder",
                                     parameterType="Required",
                                     direction="Input")
        params.append(input_files)
        output_ndvi = arcpy.Parameter(name="output_ndvi",
                                 displayName="Output NDVI Raster",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",
                                 direction="Output")
        params.append(output_ndvi)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_files = parameters[0].valueAsText
        output_ndvi = parameters[1].valueAsText

        arcpy.env.workspace = input_files
        B4 = arcpy.ListRasters("*", "TIF")
        B4 = [x for x in B4 if "B4" in x]
        B5 = arcpy.ListRasters("*", "TIF")
        B5 = [x for x in B5 if "B5" in x]

        equation = 'Float("' + B5[0] + '" - "' + B4[0] + '") / Float("' + B5[0] + '" + "' + B4[0] + '")'

        arcpy.gp.RasterCalculator_sa(equation, output_ndvi)
        arcpy.AddMessage("NDVI created!")
        return


class Buffer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buffer and Extent"
        self.description = "This tool will create a full round buffer for 1 feature class. Under Buffer Distance use both linear unit and field values. For example '20 MILES', '10 METERS', etc."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input1 = arcpy.Parameter(name="Input1",
                                     displayName="Input Feature Class",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")
        params.append(input1)
        dist1 = arcpy.Parameter(name="distance",
                                     displayName="Buffer Distance (Linear Unit; Field)",
                                     datatype="GPString",
                                     parameterType="Required",
                                     direction="Input")
        params.append(dist1)
        output1 = arcpy.Parameter(name="Output1",
                                  displayName="Output Buffer",
                                  datatype="DEFeatureClass",
                                  parameterType="Required",
                                  direction="Output")
        params.append(output1)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input1 = parameters[0].valueAsText
        dist1 = parameters[1].valueAsText
        output1 = parameters[2].valueAsText


        arcpy.Buffer_analysis(input1, output1, dist1, "FULL",
                                  "ROUND", "NONE", "", "PLANAR")

        arcpy.AddMessage("Buffer created!")
        arcpy.AddMessage("Output extent:\n YMin: {0},\n YMax: {1},\n XMin: {2},\n XMax: {3}".format(arcpy.Describe(output1).extent.YMin, arcpy.Describe(output1).extent.YMax, arcpy.Describe(output1).extent.XMin, arcpy.Describe(output1).extent.XMax))

        return