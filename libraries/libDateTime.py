class Debug:
    debugFlag=False

def enableDebug():
    Debug.debugFlag=True
def disableDebug():
    Debug.debugFlag=False

def debugPrint(printData):
    if Debug.debugFlag == True:
        print(printData)

def getOSCreateDateTime(fileName):
    import os
    import platform
    import datetime

    if platform.system() == 'Windows':
        return datetime.datetime.fromtimestamp(os.path.getctime(fileName))
    else:
        stat = os.stat(fileName)
        try:
            return datetime.datetime.fromtimestamp(stat.st_birthtime)
        except AttributeError:
            return datetime.datetime.fromtimestamp(stat.st_mtime)

def getExifDateTime(imageFileName):
    from PIL import Image
    from PIL import ExifTags
    import datetime

    exifData = {}
    try:
        img = Image.open(imageFileName)
    except:
        debugPrint('Image {0} doesn''t exist'.format(imageFileName))
        return

    exifDataRaw = img._getexif()
    if exifDataRaw is not None:
        for tag, value in exifDataRaw.items():
            decodedTag = ExifTags.TAGS.get(tag, tag)
            exifData[decodedTag] = value

    try:
        exifDateTime=exifData['DateTime']
        exifDateTime=datetime.datetime.strptime(exifDateTime, '%Y:%m:%d %H:%M:%S')
        return exifDateTime
    except:
        return None

def getDateTime(fileName):
    debugPrint('Getting Date Time for {0}'.format(fileName))
    exifDateTime=getExifDateTime(fileName)
    osDateTime=getOSCreateDateTime(fileName)
    if exifDateTime is not None:
        debugPrint('Returning Exif Time')
        return exifDateTime
    else:
        debugPrint('Returning OS Time')
        return osDateTime

#enableDebug()
#print(getDateTime('.//resources/01//01.jpg'))
#disableDebug()
#print(getDateTime('.//resources/01//02.jpg'))
#print(getDateTime('.//resources/01//03.jpg'))