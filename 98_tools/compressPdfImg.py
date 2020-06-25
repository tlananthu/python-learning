"""
  Read arguments from command line:
  1. Full Path Input PDF Name
  2. Full Path Output PDF name
  3. Verbose mode enable/disable with -v
  4. Image quality

  compressPdfImg -i full_path_pdf_input -o full_path_pdf_output -v -iq 25
"""

def parse_config():
  import argparse
  import os

  parser = argparse.ArgumentParser(description="Extracts Images from PDF File and saves to a folder")
  parser.add_argument("-i", "--infile",required=True, help="Full Path Input PDF Name")
  parser.add_argument("-o", "--outfile", required=True, help="Full Path Output PDF Name")
  parser.add_argument("-v", "--verbose", action='count', help="Enable Verbose mode")
  parser.add_argument("-iq", "--imagequality", help="Quality of each image added to PDF")

  return parser.parse_args()

def saveJPEG(filename, pix, imagequality):
    from PIL import Image
    img=Image.frombytes("RGB",[pix.width, pix.height], pix.samples)
    img.save(filename, "JPEG", quality=imagequality)

def extractImagesJPG(filename, outfolder, verbose, imagequality):
    import fitz
    from PIL import Image

    imgList=[]

    if verbose:
        print('Extracting images')

    doc = fitz.open(filename)
    pages=len(doc)
    suffix=len(str(pages))+1

    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
        
            if pix.n > 5:
                pix= fitz.Pixmap(fitz.csRGB, pix)
            newname="{0}Page_{1}.jpg".format(outfolder,str(i).zfill(suffix))
            if verbose:
                print('Extracting Page {0}, Saving as {1}'.format(i,newname))
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
    if extn=='.jpg' or extn=='.jpeg':
      if verbose: print('Recongnizing JPG File {0}'.format(file))
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

def main():
    import os

    config=parse_config()
    outfile=config.outfile
    #check if output folder exists
    if os.path.isfile(outfile):
        print('Output File already exist')
        return

    infile=config.infile
    outfolder=os.path.split(outfile)[0]+"\\"
    verbose=True if config.verbose==1 else False
    imageQuality=75 if not config.imagequality else int(config.imagequality)
    prefix=os.path.split(outfile)[1].rstrip(".pdf")+"_"

    # infiles=[]

    # #check if PDF file exists or is it a folder passed
    # if os.path.isdir(infile):
    #   for file in os.listdir(infile):
    #     if file.endswith('.pdf'):
    #       infiles.append(file)
    # else:
    #   if not os.path.isfile(infile):
    #     print('Input File does not exist')
    #     return
    #   infiles.append(infile)
    
    if not os.path.isfile(infile):
      print('Input File does not exist')
      return

    #extract images from pdf to a folder
    images=extractImagesJPG(infile,outfolder+prefix, verbose, imageQuality)
    createPDF(images,outfile, imageQuality, verbose)
    deleteImages(images, verbose)

main()
