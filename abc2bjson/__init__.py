#!/usr/bin/env hython

"""
Description:
	This package automates the conversion of an Alembic file to the BJSON format
	in Houdini.  It was created and used in Houdini 12.1, before Mantra was
	updated to support the Alembic format natively.  The contents of main() were
	originally used as a shelf_tool script.

Original Authors: Morgan Strong, Taylor Sorenson, Elizabeth Brayton
Date: December 2012
"""

import abc2bjson_hou as a2b
import chasmgeo as cg

def main():
	try:
		# Choose Object to Import
		cg.getObjectToImport()

		# Get Alembic file from user.
		inputFile = a2b.getInputFile()
		
		# Get Alembic file namespace from user.
		a2b.setAlembicNamespace(a2b.getNamespace())

		# Get Output Directory. User selects from list of options
		outDir = a2b.getOutputDir(cg.getChasmShotList())
		
		# Get Frame Range from user.
		start, end, step = a2b.getFrameRange()
		a2b.setFrameRange(start,end,step)
		
		# Set the Geometry Dictionary
		a2b.setGeoDict(cg.getGeoDict())
		
		# Generate geometry sequences    
		a2b.abc2bjson(inputFile, outDir)

		hou.ui.displayMessage("Finished conversion!")
	
	except Exception as e:
		print "Exiting: " + str(e)
	
if __name__ == 'main':
	main()