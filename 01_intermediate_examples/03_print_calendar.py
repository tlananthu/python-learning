def getImage(size, bgColour, text, textLocn, textColour):
    from PIL import Image, ImageDraw
    img=Image.new('RGB',size, bgColour)
    drawing=ImageDraw.Draw(img)
    drawing.text(textLocn, text, textColour)
    return img

class calendar():
    def __init__(self):
        self.month=5
        self.year=2020
        self.weekdays={0:'Sunday', 1:'Monday', 2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}

        self.headerCell=(100,30)#dimension, width, height
        self.headerColour=(255,255,0)#rgb
        self.headerBgColour=(73, 109, 137)#rgb

        self.dayCell=(100, 100)#dimension, width, height
        self.colour=(0,0,0)#rgb
        self.bgColour=(255,255,255)#rgb

        self.dates=[]
        self.outputfolder=''
        self.extn='.png'

    def setHeader(self, dimension, colour, bgColour):
        self.headerCell=dimension
        self.headerColour=colour
        self.headerBgColour=bgColour

    def setCell(self, dimension, colour, bgColour):
        self.dayCell=dimension
        self.colour=colour
        self.bgColour=bgColour    

    def setYearMonth(self, year, month):
        self.year=year
        self.month=month

    def setDestFolder(self, folder):
        self.outputfolder=folder

    def saveHeaderPNG(self):
        for key, value in sorted(self.weekdays.items()):
            i=getImage(self.headerCell,  self.headerBgColour, value, (10,10), self.headerColour)
            i.save(self.outputfolder+str(value)+self.extn)
        
    def saveDatesPNG(self):
        from calendar import monthrange
        days=monthrange(self.year,self.month)[1]

        #fill dates array
        for day in range(days):
            d=str(day+1).zfill(2)
            self.dates.append(d)
        
        #loop through dates array and create image for each day
        for date in self.dates:
            i=getImage(self.dayCell,  self.colour, date, (10,10), self.bgColour)
            i.save(self.outputfolder+date+self.extn)
        
        #create a blank day for filling
        i=getImage(self.dayCell,  self.colour, '', (10,10), self.bgColour)
        i.save(self.outputfolder+'00'+self.extn)

    def saveImage(self, year, month, outname, outfolder):
        print(f'Saves Calendar image of month {self.month}, year {self.year}')
        self.setYearMonth(year, month)
        self.setDestFolder(outfolder)
        self.saveHeaderPNG()
        self.saveDatesPNG()

c=calendar()
c.saveImage(2020, 5, "202010.png", 'temp/print_calendar/')

#References:
#https://code-maven.com/create-images-with-python-pil-pillow
#https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
#import calendar
#obj=calendar.TextCalendar(1)
#calendar.prcal(2020)
