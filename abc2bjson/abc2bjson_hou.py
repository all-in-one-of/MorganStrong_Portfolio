"""
File:        abc2bjson_hou.py
Author:      Taylor Sorenson, Morgan Strong, Elizabeth Brayton
Date:        11/26/12. Modified: 2/8/13
Project:     BYU Senior Animation: Chasm

This module is designed to automate the process of exporting animated geometry
from the Alembic file format to a series of geometry sequences using Houdini's
Object Model to do the heavy lifting of interpreting the Alembic file. We assume
that the hou module has already been imported. The driving shelf tool code is
contained in abc2bjson.__init__. Tested with H12.1.125.
"""

import hou
import _alembic_hom_extensions
import os
import shutil

################################################################################
#
# DATA
#
################################################################################

_namespace = "stable"
_geo_dict = {}
_frame_start = 1
_frame_end = 240
_frame_step = 1


################################################################################
#
# FUNCTIONS
#
################################################################################

#
# Sub-routines
#

def _prependNamespace(pcs):
    """
    Prepend the namespace to each level of a GeoDict.
    """

    if not _namespace:
        return pcs
    for key in pcs.keys():
        path_list = pcs[key]
        new_path_list = []
        for geo_path in path_list:
            new_path = ""
            for x in geo_path.split("/"):
                if not x:
                    continue
                new_path += "/" + _namespace + "_" + x
            new_path_list.append(new_path)
        pcs[key] = new_path_list
    return pcs
    
def _isValidAlembic(p):
    ext = p[-4:]
    if ext.lower() == ".abc":
        return True
    else:
        hou.ui.displayMessage("Please Select an Alembic (.abc) file.")
        return False
 
def _generateOutput(iSOP, outDir, name):
  """
  Write out the geometry sequence to the specified folder, adjusting frame
  numbers to account for 100 frame pre-roll on all shots.
  """
  
    # Ensure Output Directory Exists
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    
    # Create a geometry ROP in the "out" context
    geoROP = hou.node("/out").createNode('geometry')

    # Set Geometry ROP Parameters
    ROPdict = {}
    ROPdict['soppath'] = iSOP.path()
    ROPdict['sopoutput'] = outDir + name + '.`padzero(3, $F-' + str(int(_frame_start)-1+100) + ')`.bjson.gz'
    ROPdict['savebackground']= True
    ROPdict['trange'] = 1 # Render Frame Range
    ROPdict['f1'] = _frame_start
    ROPdict['f2'] = _frame_end
    ROPdict['f3'] = _frame_step
    geoROP.setParms(ROPdict)

    # Render ROP with our frame range
    geoROP.render()
    geoROP.destroy()

def _cleanOutputDir(outdir):
    #cleanup output folder
    for root, dirs, files in os.walk(outdir):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

#
# Setters
#

def setAlembicNamespace(n):
    global _namespace
    _namespace = n
	
def setGeoDict(d):
  """
	Define the Geometry Dictionary where key-value pairs are equivalent to:
    bjson_output -> [abc_group_path*]
    (str)        -> [(str)*]
    Examples: Car exported as single mesh: {"Car":["/car_model"]}
              Car exported in pieces:      {"Car_Body":["/car_model/body],\
                                            "Car_Tires":["/car_model/tire1",\
                                                         "/car_model/tire2",\
                                                         "/car_model/tire3",\
                                                         "/car_model/tire4"]}
  """
	global _geo_dict
    _geo_dict = d
	
def setFrameRange(s, e, p=1):
    global _frame_start
    global _frame_end
    global _frame_step
    _frame_start = s
    _frame_end = e
    _frame_step = p

#
# Core
#

def abc2bjson(infile, outdir='$TEMP/'):
    """
    Use Alembic SOPs to output chunks of geometry from the Alembic file as bjson
    geometry sequences.
    """

    # Clean outdir for fresh write
    #_cleanOutputDir(outdir)

    # Create a temporary Geometry Node
    temp_geo = hou.node("/obj").createNode('geo')
    
    # Generate .bjson.gz sequences in folders that correspond to the keys of the
    # geo_dict.
    for key in _geo_dict.keys():
        # Skip key if no object paths listed.
        if not _geo_dict[key]:
            continue
        
        # Tell us what key we're working on
        print key + ": " + " ".join(_geo_dict[key])
        
        # Clean out temp_geo Node
        for n in temp_geo.children():
            n.destroy()
        
        # Create a merge node to merge all abcSOPs
        temp_merge = temp_geo.createNode("merge")
        
        # Create an Alembic SOP for each object path and connect to temp_merge
        for p in _geo_dict[key]:
            abcSOP = temp_geo.createNode("alembic")
            abcSOP.setParms({'fileName': infile, 'objectPath': p})
            temp_merge.setNextInput(abcSOP)
        
        # Generate Output to a separate directory for this geometry sequence.
        seqDir = os.path.join(outdir,key) + os.sep
        _generateOutput(temp_merge, hou.expandString(seqDir), key)
    
    # Clean Up
    temp_geo.destroy()


################################################################################
#
# HOUDINI DIALOGS
#
################################################################################

def getInputFile():
    """
    Open a Houdini File Select Dialog and return the path to the Alembic file to
    be read. Raises an Exception if no file is chosen.
    """
    
    inputFile = ''
    while(not _isValidAlembic(inputFile)):
        inputFile = hou.ui.selectFile(start_directory=None,\
                                      title="Select Alembic (.abc) File",\
                                      collapse_sequences=False,\
                                      pattern=('*.abc'),\
                                      multiple_select=False,\
                                      chooser_mode=hou.fileChooserMode.Read)
        if inputFile == '':
            raise Exception("No input file chosen. Exiting...")
    return hou.expandString(inputFile)

def getOutputDir(choices=None):
    """
    Open a Houdini Dialog and return a path to the export directory.  Allows for
    either a list of choices to be displayed or a file select dialog.
    """

    if choices:
        c = hou.ui.selectFromList(choices,\
                                  exclusive = True,\
                                  title = 'Choose Directory',\
                                  num_visible_rows = 10)
        if not c:
            raise Exception("No Output Folder Selected. Exiting...")
        return hou.expandString(_interpretChoice(choices[c[0]]))
    else:
        outDir = ""
        while(not os.path.isdir(hou.expandString(outDir))):
            outDir = hou.ui.selectFile(start_directory = None,\
                                       title = "Select Output Folder",\
                                       collapse_sequences = False,\
                                       pattern = ('*'),\
                                       multiple_select = False,\
                                       chooser_mode = hou.fileChooserMode.Read)
            if outDir == '':
                return outDir
        return hou.expandString(outDir)

def getFrameRange():
    """
    Use a Houdini Dialog to get from the user and return a 3-tuple in the form:
    
        (Start Frame, End Frame, Step)

    Raise an Exception if no selection is made.
    """

    rfstart = hou.expandString("$RFSTART")
    rfend = hou.expandString("$RFEND")
    ui = hou.ui.readMultiInput("Input Frame Range.",\
                               ["Start Frame","End Frame","Step"],\
                               buttons=["OK","Cancel"],\
                               default_choice=0,\
                               close_choice=1,\
                               help="Enter the Frame Range that you exported.\n\
                                     (Ex: If you exported frames 92 to 305 from Maya, input 92 and 305).",\
                               title="Input Frame Range.",\
                               initial_contents=[str(rfstart),str(rfend),str("1")])
    if ui[0]:
        raise Exception("Cancelling...")
    return (ui[1][0], ui[1][1], ui[1][2])

def getNamespace():
    """
    Use a Houdini Dialog to return a namespace to be prepended to the object
    paths during conversion. Raise an exception if "Cancel" is selected.
    """

    ui = hou.ui.readInput("Please provide the namespace used when \nthe .abc file was exported.  \
                           (Ex: If your animation file \nreferenced the 'stable' link, the namespace is 'stable').",\
                        buttons=["OK","Cancel"],
                        default_choice=0,\
                        close_choice=1,\
                        initial_contents="stable")
    if ui[0]:
        raise Exception("Cancelling...")
    return ui[1]
