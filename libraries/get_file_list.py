def getAllFiles(rootDir, wildcardsearch):
    import glob
    import os

    files=[]
    for file in glob.glob(rootDir+'**/'+wildcardsearch,recursive=True):
        if os.path.isfile(file):
            files.append(str(file))

    return files

#files=getAllFiles('c://users//ananthan//pictures//','*.jpg')
