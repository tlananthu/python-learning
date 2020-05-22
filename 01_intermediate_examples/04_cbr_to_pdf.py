from pyunpack import Archive
import os

folder="resources/03/"
cbrFile=folder+"03.cbr"
outfolder=folder+'out/'

if not os.path.isdir(outfolder):
    os.mkdir(outfolder)

Archive(cbrFile).extractall(outfolder)
