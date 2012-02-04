import os
import glob

path = r'C:\Temp\_Curso-Analisis-Espacial-Raster\docs\images'
for infile in glob.glob( os.path.join(path, 'd*.png') ):
    print ".. figure:: images/" + os.path.basename(infile)
    print ""
    print "   " + os.path.basename(infile)
    print ""
