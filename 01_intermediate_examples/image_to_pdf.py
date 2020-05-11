# from PIL import Image

# image1 = Image.open(r'.//resources/01/01.jpg')
# image2 = Image.open(r'.//resources/01/02.jpg')
# image3 = Image.open(r'.//resources/01/03.jpg')
 
# im1 = image1.convert('RGB')
# im2 = image2.convert('RGB')
# im3 = image3.convert('RGB')

# imagelist = [im2,im3]

# im1.save(r'.//temp//test.pdf',save_all=True, append_images=imagelist)

from PIL import Image

def getFilesList(folder):
    import os

    if folder=='.':
        #if folder name was dot, get current folder dir
        filesList=os.listdir()
    else:
        #if a folder name was passed, get folder dir of that parameter
        filesList=os.listdir(folder)

    #return the resultant list
    return filesList

basepath='.//resources//01/'
images=getFilesList(basepath)
imagelist=[]

for image in images:
    i1=Image.open(basepath+image)
    i2=i1.convert('RGB')
    imagelist.append(i2)

#NOTE: The last image is added twice because of the loop and i2.save
#This is just a demo, so ignoring that

i2.save('.//temp/image_to_pdf.pdf',save_all=True,append_images=imagelist)
