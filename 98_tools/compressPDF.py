import os

def saveJPEG(filename, pix, imagequality):
    from PIL import Image
    img=Image.frombytes("RGB",[pix.width, pix.height], pix.samples)
    img.save(filename, "JPEG", quality=imagequality)

def extractImagesJPG(filename, outfolder, verbose, imagequality):
    import fitz
    from PIL import Image

    imgList=[]

    if verbose: print('Extracting images')

    doc = fitz.open(filename)
    pages=len(doc)
    suffix=len(str(pages))+1

    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
        
            if pix.n > 5: pix= fitz.Pixmap(fitz.csRGB, pix)
            newname="{0}Page_{1}.jpg".format(outfolder,str(i).zfill(suffix))
            if verbose: print('Extracting Page {0}, Saving as {1}'.format(i,newname))
            saveJPEG(newname, pix, imagequality)
            imgList.append(newname)
            pix = None
    
    return imgList

def getFilesFolder(folder, verbose):
  import glob
  import os

  files=[]
  for file in glob.iglob(folder+'**/*',recursive=False):
    fn,extn=os.path.splitext(file)
    if extn=='.pdf':
      if verbose: print('Recongnizing PDF File {0}'.format(file))
      files.append(file)
  return files

def isValidImage(filename):
  import imghdr
  fileType=imghdr.what(filename)
  return fileType

def createPDF(imgList, outname, imageQuality, verbose):
  from PIL import Image

  imageList=[]
  foundImages=False
  imageNum=0

  for image in imgList:
    #validate image
    if isValidImage(image)=="jpeg":
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
    if verbose: print('Generating PDF {0}'.format(outname))
    img1.save(outname,save_all=True,append_images=imageList, quality=imageQuality)

def deleteImages(imgList, verbose):
  import os

  for image in imgList:
    if verbose: print('Removing File {0}'.format(image))
    os.remove(image)

class CompressPDF:
    def compressFile(infile, outfile, verbose, imagequality):
        if verbose: print(f'Compressing PDF File {infile} to {outfile}')

        #check if input file exists
        if not os.path.isfile(infile):
            print('Input File does not exist')
            return
        #check if output file exists
        if os.path.isfile(outfile):
            print('Output File already exist')
            return

        outfolder=os.path.split(outfile)[0]+"\\"
        prefix=os.path.split(outfile)[1].rstrip(".pdf")+"_"

        #extract images from pdf to a folder
        images=extractImagesJPG(infile,outfolder+prefix, verbose, imagequality)
        createPDF(images,outfile, imagequality, verbose)
        deleteImages(images, verbose)

    def compressFolder(infolder, outfolder, verbose, imagequality):
        if verbose: print(f'Compressing PDF Folder {infolder}')

        #check if input folder exists
        if not os.path.isdir(infolder):
            print('Input Folder does not exist')
            return
        #check if output folder exists
        if not os.path.isdir(outfolder):
            print('Output Folder does not exist')
            return

        files=getFilesFolder(infolder, verbose)
        for file in files:
          fname=os.path.split(file)[1]
          CompressPDF.compressFile(file, outfolder+str(fname), verbose, imagequality)
        
CompressPDF.compressFolder("c:/temp/ic","c:/temp/",True,10)