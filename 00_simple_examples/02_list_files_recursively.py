import sys

def printFiles(rootDir):
    import glob
    import os

    files={}
    for file in glob.iglob(rootDir+'**/*',recursive=True):
        if os.path.isfile(file):
            print(str(file))

printFiles('')