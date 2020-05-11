import os

def getFilesList(folder):
    if folder=='.':
        #if folder name was dot, get current folder dir
        filesList=os.listdir()
    else:
        #if a folder name was passed, get folder dir of that parameter
        filesList=os.listdir(folder)

    #return the resultant list
    return filesList


#print(getFilesList('.'))
#print(getFilesList('c://'))