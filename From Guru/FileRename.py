import argparse
import os
from datetime import datetime
import shutil
import sys, traceback
#from PIL import Image

class FileRename:
    VALID_IMG_EXTN=(".jpg", ".jpeg")
    paths=[]
    outdir=""
    newfilesDictionary = {}
    dateformat="%Y-%m-%d %H.%M.%S"
    
    def __init__(self, config):

        self.paths = config.path
        self.outdir = config.outdir
        print(" Initialising ..."+str(self.paths)+" And out dir :"+self.outdir)
        if not os.path.exists(self.outdir):
            print(self.outdir+" Out dir doesnt exist, will use current dir")
            self.outdir=os.getcwd()
        
        self.readOutdir()
        
    def readOutdir(self):
        print(" Reading existing files of outdir ")
        os.chdir(self.outdir)
        filelist = os.listdir( self.outdir )
        filelist.sort(key=lambda x: os.path.getctime(x))
        for file in filelist:
            filename, extension = os.path.splitext(file)
            if ( extension in self.VALID_IMG_EXTN ):
                print(" Working on file :"+ filename)    
                tmpFname=filename
                idx=0
                strLen=len(filename)
                dashLen=filename.rindex("-")
                
                if((strLen-dashLen)<7):
                    tmpFname=filename[:dashLen]
                    idx=int(filename[dashLen+1:])
                    
                else:
                    print(" No index found")
                
                print(" tmpFname =>"+ tmpFname+ " idx "+ str(idx))
                    
                try:
                    tmptime=datetime.strptime(tmpFname, self.dateformat)
                    print(" TMP time is :"+str(tmptime)+" hence adding to dict")
                    
                    if (tmpFname in self.newfilesDictionary.keys()):
                        tmpidx= self.newfilesDictionary[tmpFname]
                    else:
                        tmpidx=0
                    
                    if (tmpidx>idx):
                        print(" Since existing index is higher ...doing nothing "+str(tmpidx)+" > "+ str(idx))
                    else:
                        self.newfilesDictionary[tmpFname] = idx
                    
                except:
                    traceback. print_exc()
                    print(tmpFname+" is not time value...Moving on...")

        print(" Finally New dictionary initialised to "+ str(self.newfilesDictionary))

    def findFiles(self):
        count = 0
        
        for directory in self.paths:
            print("Finding in directory :"+ directory)
            os.chdir(directory)
            filelist = os.listdir( directory )
            for file in filelist:
                # split the file into filename and extension
                print(" Working on file : "+file)
                filename, extension = os.path.splitext(file)
                # if the extension is a valid extension
                if ( extension in self.VALID_IMG_EXTN ):
                    # Get the create time of the file
                    create_time = os.path.getctime( file )
                    # get the readable timestamp format 
                    format_time = datetime.fromtimestamp( create_time )
                    # convert time into string
                    format_time_string = format_time.strftime(self.dateformat) 
                    print(" Formatted time string is :"+ format_time_string)
                    # Contruct the new name of the file
                    newfile = format_time_string + extension; 

                    # If there is other files created at the same timestamp
                    if ( newfile in self.newfilesDictionary.keys() ):
                        index = self.newfilesDictionary[newfile] + 1;
                        self.newfilesDictionary[newfile] = index; 
                        newfile = format_time_string + '-' + str(index) + extension;
                    else:
                        self.newfilesDictionary[newfile] = 0; 
                    
                    oldFullFile=os.path.join(directory, file)
                    newFullFile=os.path.join(self.outdir, newfile)
                    
                    print(" Moving "+oldFullFile+" to "+ newFullFile)
                    
                    shutil.move( oldFullFile, newFullFile );
                    count = count + 1
                    


def parse_config():
    parser = argparse.ArgumentParser(description="Consolidates Image files and renames as per timestamp")
    parser.add_argument("path", nargs="+", help="paths to process")
    parser.add_argument("-o", "--outdir", default=os.getcwd(), help="directory to place generated files")

    return parser.parse_args()

def main():

        config = parse_config()
        fc = FileRename(config)
        fc.findFiles()

if __name__ == "__main__":
    main()
