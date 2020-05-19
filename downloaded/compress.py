#run this in any directory add -v for verbose 
#get Pillow (fork of PIL) from pip before running --> pip install Pillow

import os
import sys
from PIL import Image

def compressMe(folder, file, verbose=False):
    filepath=os.path.join(folder,file)
    oldsize=os.stat(filepath).st_size
    picture=Image.open(filepath)
    dim=picture.size
    newfile=os.path.join(folder,"Compressed_"+file)
    picture.save(newfile,"JPEG",optimize=True,quality=50)
    newsize=os.stat(newfile).st_size
    percent=(oldsize-newsize)/float(oldsize)*100
    print("File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent))
    return percent

def main():
    verbose = False
    #checks for verbose flag
    if (len(sys.argv)>1):
        if (sys.argv[1].lower()=="-v"):
            verbose = True
        
    #finds present working dir
    pwd = "temp/download_jpgs/"
    tot = 0
    num = 0
    for file in os.listdir(pwd):
        if os.path.splitext(file)[1].lower() in ('.jpg','.jpeg'):
            num+=1
            tot+=compressMe(pwd, file,verbose)
    if num>0:
        print("Average Compression: %d" % (float(tot)/num))
    print("Done")

main()
