import fitz

def saveJPEG(filename, pix):
    from PIL import Image
    img=Image.frombytes("RGB",[pix.width, pix.height], pix.samples)
    img.save(filename, "JPEG")

def extractImagesJPG(filename, outfolder):
    from PIL import Image

    print('Extracting images')
    doc = fitz.open('resources/05/സർക്കസ്.pdf')
    pages=len(doc)
    suffix=len(str(pages))+1

    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
        
            if pix.n > 5:
                pix= fitz.Pixmap(fitz.csRGB, pix)
            newname="{0}Page_{1}.jpg".format(outfolder,str(i).zfill(suffix))
            print(newname)
            saveJPEG(newname, pix)
            pix = None

def cleanup(folder):
    import os

    print('Cleaning up')
    files=os.listdir(folder)
    for file in files:
        os.remove(folder+file)

def main():
    outfolder='temp/pdf2image/'
    #extract images from pdf to a folder
    extractImagesJPG('resources/05/സർക്കസ്.pdf',outfolder)
    
    #deleting extracted files after conversion
    #cleanup(outfolder)

main()
