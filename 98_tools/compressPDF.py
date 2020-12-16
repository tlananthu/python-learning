import os

def writelog(message, verbose):
  import codecs

  f=codecs.open("temp/compressPDF/compressPDF.log","a","utf-8")
  f.write(str(message)+'\n')
  f.close()

  if verbose:print(message)

def saveJPEG(filename, pix, verbose, imagequality):
    from PIL import Image
    try:
      img=Image.frombytes("RGB",[pix.width, pix.height], pix.samples)
    except ValueError:
      writelog(f'Exporting Image as Black & White {filename}', verbose)
      img=Image.frombytes("L",[pix.width, pix.height], pix.samples)
    img.save(filename, "JPEG", quality=imagequality)

def extractImagesJPG(filename, outfolder, verbose, imagequality):
    import fitz
    from PIL import Image

    imgList=[]

    writelog('Extracting images', verbose)

    doc = fitz.open(filename)
    pages=len(doc)
    suffix=len(str(pages))+1

    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
        
            if pix.n > 5: pix= fitz.Pixmap(fitz.csRGB, pix)
            newname="{0}Page_{1}.jpg".format(outfolder,str(i).zfill(suffix))
            writelog('Extracting Page {0}, Saving as {1}'.format(i,newname), verbose)
            saveJPEG(newname, pix, verbose, imagequality)
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
      writelog('Recongnizing PDF File {0}'.format(file), verbose)
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
      writelog('Adding Page {0}'.format(imageNum), verbose)
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
    writelog('Generating PDF {0}'.format(outname), verbose)
    img1.save(outname,save_all=True,append_images=imageList, quality=imageQuality)

def deleteImages(imgList, verbose):
  import os

  for image in imgList:
    writelog('Removing File {0}'.format(image), verbose)
    os.remove(image)

class CompressPDF:
    def compressFile(infile, outfile, verbose, imagequality):
        writelog(f'Compressing PDF File {infile} to {outfile}', verbose)

        #check if input file exists
        if not os.path.isfile(infile):
            writelog('Input File does not exist', True)
            return
        #check if output file exists
        if os.path.isfile(outfile):
            writelog('Output File already exist', True)
            return

        outfolder=os.path.split(outfile)[0]+"\\"
        prefix=os.path.split(outfile)[1].rstrip(".pdf")+"_"

        #extract images from pdf to a folder
        images=extractImagesJPG(infile,outfolder+prefix, verbose, imagequality)
        createPDF(images,outfile, imagequality, verbose)
        deleteImages(images, verbose)

    def compressFolder(infolder, outfolder, verbose, imagequality):
        writelog(f'Compressing PDF Folder {infolder}', verbose)

        #check if input folder exists
        if not os.path.isdir(infolder):
            writelog('Input Folder does not exist', True)
            return
        #check if output folder exists
        if not os.path.isdir(outfolder):
            writelog('Output Folder does not exist', True)
            return

        files=getFilesFolder(infolder, verbose)
        for file in files:
          fname=os.path.split(file)[1]
          writelog(f'Compressing {file}',True)
          CompressPDF.compressFile(file, outfolder+str(fname), verbose, imagequality)
        
CompressPDF.compressFolder("c:/temp/ic","c:/temp/",False,10)