from pyunpack import Archive
import os

#CBR is a RAR file in disguise

def extractFile(filename, outputdir):
    if os.path.isfile(filename):    
        #Check if outputdir exists, if not create
        if not os.path.isdir(outputdir):
            os.mkdir(outputdir)
        Archive(filename).extractall(outputdir)
    else:
        print('File {0} does not exist.'.format(filename))

extractFile('.//resources//03//03.cbr','.//temp/extract-cbr//')