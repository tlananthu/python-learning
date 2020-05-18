#This program downloads jpgs from the website and creates a pdf out of it
#https://www.gandhiheritageportal.org/datalink/files/allbooks/en/archive/book675/book_675_en_001.jpg to 152.jpg

def download(fullurl, downloadname):
    import os
    import requests

    from urllib.parse import urlparse
    from pathlib import Path

    a = urlparse(fullurl)
    fn=downloadname

    if os.path.isfile(fn):
        print('Skipping download, file exists {0}'.format(fn))
    else:
        print('Downloading file {0}'.format(fn))
        r=requests.get(fullurl, stream=True)
        with open(fn,'wb') as f:
            f.write(r.content)

def downloadallJPGS():
    for i in range(152):
        page=str(i+1)
        ifn='book_675_en_{0}.jpg'.format(page)
        ofn='book_675_en_{0}.jpg'.format(page.zfill(3))
        download("https://www.gandhiheritageportal.org/datalink/files/allbooks/en/archive/book675/"+ifn,"temp/download_jpgs/"+ofn)

def createPDF(foldername):
    from PIL import Image
    import os
    files=os.listdir(foldername)
    files.sort()
    
    imageList=[]
    for i,file in enumerate(files):
        if i==0:
            i1=Image.open(foldername+'/'+file)
            i2=i1.convert('RGB')
        else:
            print('Adding {0}'.format(file))
            image1=Image.open(foldername+'/'+file)
            im1=image1.convert('RGB')
            imageList.append(im1)

    i2.save(foldername+'/book_675_en.pdf',save_all=True, append_images=imageList)

downloadallJPGS()
createPDF("temp/download_jpgs")
