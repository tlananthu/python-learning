import sys
import codecs

def printFiles(rootDir,outname):
    import glob
    import os
    
    f=codecs.open(outname,'w','utf-8')

    files={}
    for file in glob.iglob(rootDir+'**/*',recursive=True):
        if os.path.isdir(file):
            print('Scanning {0}'.format(file))
        elif os.path.isfile(file):
            f.write(str(file)+'\n')
    f.close()

printFiles('c:/temp','temp/list_recursive/filelist.log')