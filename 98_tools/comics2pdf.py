"""
  Read arguments from command line:
  1. -i accepts image folder which contains cbr/cbz or individual cbr/cbz files
  2. -o output file name
  3. -v verbose of operations performed
  4. -iq adjust image quality, default 75

  comics2pdf -i c:/images -i c:/images/file.pdf -v -iq 10
"""

def parse_config():
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Creates a PDF from either set of images/cbr file or cbz file")
    parser.add_argument("-i", "--indir",required=True, help="Source images (Folder name/cbr file name/cbz filename")
    parser.add_argument("-iq", "--imagequality", help="Quality of each image added to PDF")
    parser.add_argument("-v", "--verbose", action='count', help="Enable Verbose mode")
    parser.add_argument("-o", "--outfile", required=True, help="Full path of pdf to be created, existing file will be overwritten")

    return parser.parse_args()

def verbosePrint(message, flag):
    if flag: print(message)

def printError(message):
    print(message)

def isValidImage(filename):
  import imghdr
  return imghdr.what(filename)

def removeTempDir(folder):
    import glob
    import os

    for file in glob.iglob(folder+'/**/*',recursive=True):
        if os.path.isfile(folder+'/'+file): os.remove(folder+'/'+file)

    for file in glob.iglob(folder+'/**/*',recursive=True):
        if os.path.isdir(folder+'/'+file): os.rmdir(folder)

def createPDF(imgList, outname, imageQuality, verbose):
    from PIL import Image

    imageList=[]
    foundImages=False
    imageNum=0

    for image in imgList:
        #validate image
        imageType=isValidImage(image)
        if verbose: print('Adding Page {0}'.format(imageNum))
        if imageNum==0:
            image1=Image.open(image)
            img1=image1.convert('RGB')
            foundImages=True
        else:
            tmpImage=Image.open(image)
            tmp1=tmpImage.convert('RGB')
            imageList.append(tmp1)
        imageNum+=1

    if foundImages: 
        print('Generating PDF {0}'.format(outname))
        img1.save(outname,save_all=True,append_images=imageList, quality=imageQuality)

class cbz():
    def __init__(self,filename):
        import os
        self.srcFile=filename
        self.extractFolder, extn=os.path.splitext(filename)
        self.verbose=False

        self.srcFolder=os.path.split(filename)[0]
        if not os.path.isfile(filename): self.error('Invalid File specified')
        if extn.lower() != '.cbz': self.error('Invalid CBZ File specified')

    def enableVerbose(self):
        self.verbose=True

    def disableVerbose(self):
        self.verbose=False
    
    def error(self, message):
        print(message)

    def printVerbose(self, message):
        if self.verbose: print(message)

    def extractall(self):
        import os
        import zipfile

        if not os.path.isdir(self.extractFolder):
            os.mkdir(self.extractFolder)
        #extract zip files to the outputdir
        self.printVerbose("Extracting {0} to {1}".format(self.srcFile, self.extractFolder))
        with zipfile.ZipFile(self.srcFile,'r') as f:
            f.extractall(self.extractFolder)

    def generatePDF(self, outname, imageQuality):
        import glob
        import os

        #extract images first
        self.extractall()

        #pass images and get a PDF
        self.printVerbose('Extracted Folder {0}'.format(self.extractFolder))
        imgList=[]
        for file in glob.iglob(self.extractFolder+'**/*', recursive=True):
            if os.path.isfile(file):
                imgList.append(file)
        createPDF(imgList, outname, imageQuality, self.verbose)
        removeTempDir(self.extractFolder)

class cbr():
    def __init__(self,filename):
        import os
        self.srcFile=filename
        self.extractFolder, extn=os.path.splitext(filename)
        self.verbose=False

        self.srcFolder=os.path.split(filename)[0]
        if not os.path.isfile(filename): self.error('Invalid File specified')
        if extn.lower() != '.cbr': self.error('Invalid CBR File specified')

    def enableVerbose(self):
        self.verbose=True

    def disableVerbose(self):
        self.verbose=False
    
    def error(self, message):
        print(message)

    def printVerbose(self, message):
        if self.verbose: print(message)

    def extractall(self):
        from pyunpack import Archive
        import os

        if not os.path.isdir(self.extractFolder):
            os.mkdir(self.extractFolder)

        self.printVerbose("Extracting {0} to {1}".format(self.srcFile, self.extractFolder))
        Archive(self.srcFile).extractall(self.extractFolder)
        self.printVerbose(f"Extracted {self.srcFile}")

    def generatePDF(self, outname, imageQuality):
        import glob
        import os
        
        #extract images first
        self.extractall()

        #pass images and get a PDF
        self.printVerbose('Extracted Folder {0}'.format(self.extractFolder))
        imgList=[]
        for file in glob.iglob(self.extractFolder+'/**/*',recursive=True):
            if os.path.isfile(file):
                imageType=isValidImage(file)
                if imageType=="jpeg":
                    self.printVerbose('Adding File {0}'.format(file))
                    imgList.append(file)
        
        createPDF(imgList, outname, imageQuality, self.verbose)
        removeTempDir(self.extractFolder)

def  processFile(srcFolder, imageQuality, destFile, verbose):
    import os

    #check whether its a cbr/cbz
    fn, extn=os.path.splitext(srcFolder)
    srcType=extn.replace('.','').upper()

    verbosePrint(f"Input is a file, Type is {srcType}", verbose)
    if srcType=="CBR":
        c=cbr(srcFolder)
        if verbose: c.enableVerbose()
        c.generatePDF(destFile, imageQuality)
    elif srcType=="CBZ":
        d=cbz(srcFolder)
        if verbose: d.enableVerbose()
        d.generatePDF(destFile, imageQuality)
    else:
        verbosePrint('Ignoring non recognized file {0}'.format(srcType), verbose)

def main():
    import os
    import glob

    config=parse_config()
    srcFolder=config.indir
    destFile=config.outfile
    destFolder=os.path.split(destFile)[0]

    verbose=True if config.verbose==1 else False
    imageQuality=75 if not config.imagequality else int(config.imagequality)

    if os.path.isdir(srcFolder):
        srcType="FOLDER"
        verbosePrint('Input is a folder, scanning CBR/CBZ files inside', verbose)
        for file in glob.iglob(srcFolder+'**/*'):
            fn=os.path.split(file)[1]+'.pdf'
            processFile(file, imageQuality, destFolder+'/'+fn, verbose)
    elif os.path.isfile(srcFolder):
        fn=os.path.split(srcFolder)[1]+'.pdf'
        processFile( srcFolder, imageQuality, destFile+'/'+fn, verbose)
    else:
        printError('Invalid input specified')
        return

main()