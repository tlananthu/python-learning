def downloadURL(url,outname):
    import urllib.request
    print('Downloading URL:',url)
    urllib.request.urlretrieve(url,outname)

def findURL(string):
    import re
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url

def findIsbn(word):
    result=word.find('isbn=')
    if result>0:
        return word[result+5:]
    else:
        return ''

def getPDFURL(isbn):
    pdfURL='https://link.springer.com/content/pdf/10.1007%2F'+isbn+'.pdf'
    return pdfURL

def openPDFFile(pdfFilename, downloadFolder):
    import PyPDF2
    pdfFileObj = open(pdfFilename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print('Opened File: ',pdfFilename)

    allPages=range(pdfReader.numPages)
    print('Total Pages: ',pdfReader.numPages)
    #loop through all pages
    for pageIdx in allPages:
        print('Page Num: ',pageIdx+1)
        currentPage=pdfReader.getPage(pageIdx)
        currentPageText=currentPage.extractText()
        urlsInPage=findURL(currentPageText)

        #loop through all URLs in the page and find isbn
        for url in urlsInPage:
            isbn=findIsbn(url)
            fileUrl=getPDFURL(isbn)
            ourUrl=downloadFolder+isbn+'.pdf'
            print(fileUrl)
            #download the file
            downloadURL(fileUrl,ourUrl)

openPDFFile('resources/06/SpringerEbooks.pdf','temp/read_pdf_download_links/')