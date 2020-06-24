"""
  Read arguments from command line:
  1. Input PDF Name
  2. Output folder name
  3. Verbose mode enable/disable with -v
  4. Prefix to image files
  5. Image quality

  pdfToImg -i full_path_to_pdf -o output_folder_name -v
"""

def parse_config():
  import argparse
  import os

  parser = argparse.ArgumentParser(description="Extracts Images from PDF File and saves to a folder")
  parser.add_argument("-i", "--infile",required=True, help="Full Path to PDF File")
  parser.add_argument("-v", "--verbose", action='count', help="Enable Verbose mode")
  parser.add_argument("-o", "--outfolder", required=True, help="Full path of folder, which should exist already")
  parser.add_argument("-f", "--fileprefix", required=True, help="Prefix attached to all image files created")
  parser.add_argument("-iq", "--imagequality", help="Quality of each image added to PDF")

  return parser.parse_args()

def saveJPEG(filename, pix, imagequality):
    from PIL import Image
    img=Image.frombytes("RGB",[pix.width, pix.height], pix.samples)
    img.save(filename, "JPEG", quality=imagequality)

def extractImagesJPG(filename, outfolder, verbose, imagequality):
    import fitz
    from PIL import Image

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
            pix = None

def main():
    import os

    config=parse_config()
    outfolder=config.outfolder
    #check if output folder exists
    if not os.path.isdir(outfolder):
        print('Output Folder does not exist')
        return

    infile=config.infile
    #check if PDF file exists
    if not os.path.isfile(infile):
        print('Input File does not exist')
        return

    prefix=config.fileprefix
    verbose=True if config.verbose==1 else False
    imageQuality=75 if not config.imagequality else int(config.imagequality)

    #extract images from pdf to a folder
    extractImagesJPG(infile,outfolder+prefix, verbose, imageQuality)

main()
