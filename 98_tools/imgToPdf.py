"""
  Read arguments from command line:
  1. folder name containing images
  2. output file name (includes folder)
  3. Verbose mode enable/disable with -v
  4. Image quality

  imgToPdf -i c:/images -i c:/images/file.pdf -v -iq 10
"""

def parse_config():
  import argparse
  import os

  parser = argparse.ArgumentParser(description="Consolidates Image files and creates a PDF")
  parser.add_argument("-i", "--indir",required=True, help="Read images from specified directory")
  parser.add_argument("-iq", "--imagequality", help="Quality of each image added to PDF")
  parser.add_argument("-v", "--verbose", action='count', help="Enable Verbose mode")
  parser.add_argument("-o", "--outfile", required=True, help="Full path of pdf to be created, existing file will be overwritten")

  return parser.parse_args()

def getFilesFolder(folder, verbose):
  import glob
  import os

  files=[]
  for file in glob.iglob(folder+'**/*.jpg',recursive=False):
    #extn=str(os.path.split(file)).rsplit('.')
    if verbose: print('Recongnizing JPG File {0}'.format(file))
    files.append(file)
  return files

def createPDF(imgList, outname, imageQuality, verbose):
  from PIL import Image

  imageList=[]
  for i, image in enumerate(imgList):
    if verbose: print('Adding Page {0}'.format(i))
    if i==0:
      image1=Image.open(image)
      img1=image1.convert('RGB')
    else:
      tmpImage=Image.open(image)
      tmp1=tmpImage.convert('RGB')
      imageList.append(tmp1)
  if verbose: print('Generating PDF {0}'.format(outname))
  img1.save(outname,save_all=True,append_images=imageList, quality=imageQuality)

def main():
  import os
  config=parse_config()
  srcFolder=config.indir
  destFile=config.outfile
  destFolder=os.path.split(destFile)[0]

  verbose=True if config.verbose==1 else False
  imageQuality=100 if not config.imagequality else int(config.imagequality)

  files=getFilesFolder(srcFolder,verbose)
  createPDF(files, destFile,imageQuality, verbose)

main()