import zipfile
import os

#CBZ is a ZIP file in disguise

def extractFile(filename, outputdir):
    #Check if file exists
    if os.path.isfile(filename):
        #Check if outputdir exists, if not create
        if not os.path.isdir(outputdir):
            os.mkdir(outputdir)
        
        #extract zip files to the outputdir
        with zipfile.ZipFile(filename,'r') as f:
            f.extractall(outputdir)
    else:
        print('File {0} does not exist.'.format(filename))

#extractFile('.//resources//02//01.cbz','.//temp/extract-cbz//')