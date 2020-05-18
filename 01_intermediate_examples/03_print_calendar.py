#following returns an image with specified text, can be treated as a separate library
def getImage(size, bgColour, text, textLocn, textColour):
    from PIL import Image, ImageDraw
    img=Image.new('RGB',size, bgColour)
    drawing=ImageDraw.Draw(img)
    drawing.text(textLocn, text, textColour)
    return img

#class calendar which has methods to generate and customize the calendar
class calendar():
    def __init__(self):
        self.month=5    #month to be printed
        self.year=2020  #year to be printed
        self.weekdays={0:'Sunday', 1:'Monday', 2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}

        self.headerCell=(100,30)#dimension, width, height
        self.headerColour=(255,255,0)#rgb
        self.headerBgColour=(73, 109, 137)#rgb

        self.dayCell=(100, 100)#dimension, width, height
        self.colour=(255,255,255)#rgb #black
        self.bgColour=(0,0,0)#rgb #white

        self.daysInMonth=0      #total days in the processing month will be updated
        self.headerImages=[]    #weekdays images in one row as a list
        self.dates=[]           #dates in the processing month
        self.dateImages=[]      #date images in list, will be used to delete temporary files
        self.rowImages=[]       #row images in list, will be used to join rows and delete temporary files
        self.outputfolder=''    #output folder where png files will be created
        self.extn='.png'        #tested with png only

    #method to set Header attributes
    def setHeader(self, dimension, colour, bgColour):
        self.headerCell=dimension
        self.headerColour=colour
        self.headerBgColour=bgColour

    #method to set date column attributes
    def setCell(self, dimension, colour, bgColour):
        self.dayCell=dimension
        self.colour=colour
        self.bgColour=bgColour    

    #method to set year and month to be processed
    def setYearMonth(self, year, month):
        self.year=year
        self.month=month

    #method to set output folder
    def setDestFolder(self, folder):
        self.outputfolder=folder

    #method that returns formatted date file name 01.png etc 
    def getFileNameDate(self, day):
        return str(day).zfill(2)+'.png'

    #method that returns first day of the processing month
    def getFirstDayDay(self):
        import datetime
        d=datetime.date(self.year, self.month, 1)
        return d.strftime('%A')

    #method that joins the row images to form a calendar
    def joinImageV(self, imgs, outname):
        from PIL import Image
        images=[Image.open(x) for x in imgs]
        widths, heights = zip(*(i.size for i in images))
        maxWidth=max(widths)
        totalHeight=sum(heights)
        newImage=Image.new('RGB', (maxWidth, totalHeight))
        y_offset=0
        for im in images:
            newImage.paste(im, (0,y_offset))
            y_offset+=im.height
        newImage.save(outname)

    #method that joins each header, date images to form a row
    def joinImageH(self, imgs, outname):
        from PIL import Image
        images=[Image.open(x) for x in imgs]
        widths, heights = zip(*(i.size for i in images))
        totalWidth=sum(widths)
        maxHeight=max(heights)
        newImage=Image.new('RGB', (totalWidth, maxHeight))
        x_offset=0
        for im in images:
            newImage.paste(im, (x_offset,0))
            x_offset+=im.size[0]
        newImage.save(outname)
        return str(outname)

    #method that creates png files for each weekday header (Sun..Sat)
    def saveHeaderPNG(self):
        import os
        for key, value in sorted(self.weekdays.items()):
            i=getImage(self.headerCell, self.headerColour, value, (10,10), self.headerBgColour)
            i.save(self.outputfolder+str(value)+self.extn)
            self.headerImages.append(self.outputfolder+str(value)+self.extn)
        self.rowImages=[]
        self.rowImages.append(self.joinImageH(self.headerImages, self.outputfolder+'Row_1.png'))
        
    #method that creates png files for each day {1..31)
    def saveDatesPNG(self):
        from calendar import monthrange
        import os
        days=monthrange(self.year,self.month)[1]
        self.daysInMonth=days

        #fill dates array
        for day in range(days):
            d=str(day+1).zfill(2)
            self.dates.append(d)
        
        #loop through dates array and create image for each day
        for date in self.dates:
            i=getImage(self.dayCell,  self.colour, date, (10,10), self.bgColour)
            i.save(self.outputfolder+date+self.extn)
            self.dateImages.append(self.outputfolder+str(date)+self.extn)
        
        #create a blank day for filling
        i=getImage(self.dayCell,  self.colour, '', (10,10), self.bgColour)
        i.save(self.outputfolder+'00'+self.extn)

    #creates row for date
    def saveDatesRow(self):
        fd=self.getFirstDayDay()
        fr=[]
        row=[]
        endBlank=False
        printedDates=1
        #fill first row
        for k,v in self.weekdays.items():
            if v != fd and not endBlank:
                row.append(self.outputfolder+'00.png')
            else:
                endBlank=True
                row.append(self.outputfolder+self.getFileNameDate(printedDates))
                printedDates+=1
        fr.append(row)
        #fill all 2+ rows
        for d in range(printedDates, self.daysInMonth+1):
            row=[]
            for k,v in self.weekdays.items():
                row.append(self.outputfolder+self.getFileNameDate(printedDates))
                printedDates+=1
                if printedDates>self.daysInMonth:
                    break
            fr.append(row)
            if printedDates>self.daysInMonth:
                break
        
        lastRow=len(fr[len(fr)-1])
        if lastRow<7:
            for i in range(0,7-lastRow):
                fr[len(fr)-1].append(self.outputfolder+'00.png')
        
        #create row images
        for i,r in enumerate(fr):
            self.rowImages.append(self.joinImageH(fr[i], self.outputfolder+'Row_{0}.png'.format(i+2)))

    #method that cleansup/removes temporary files
    def cleanup(self):
        import os
        for h in self.headerImages:
            os.remove(h)
        for r in self.rowImages:
            os.remove(r)
        for d in self.dateImages:
            os.remove(d)
        os.remove(self.outputfolder+'month.png')
        os.remove(self.outputfolder+'month__.png')
        os.remove(self.outputfolder+'00.png')

    #the joining piece that runs in sequential order
    def generateCalendar(self, outfolder):
        import datetime
        
        self.saveHeaderPNG()
        self.saveDatesPNG()
        self.saveDatesRow()

        #creates month heading row
        row=[]
        m=getImage((self.headerCell[0]*3,self.headerCell[1]), self.headerColour, '',(10,10),self.headerBgColour)
        m.save(self.outputfolder+str('month__')+self.extn)
        row.append(self.outputfolder+str('month__')+self.extn)
        month=datetime.date(self.year, self.month, 1).strftime('%B {0}'.format(self.year))
        m=getImage(self.headerCell, self.headerColour, month,(10,10),self.headerBgColour)
        m.save(self.outputfolder+str('month')+self.extn)
        row.append(self.outputfolder+str('month')+self.extn)
        row.append(self.outputfolder+str('month__')+self.extn)
        
        r=self.joinImageH(row, self.outputfolder+'Row_0.png')
        #joins with all existing row images
        self.rowImages=[r]+self.rowImages

        #the final calendar view
        self.joinImageV(self.rowImages, outfolder)
        self.cleanup()

    def saveImage(self, year, month, outname, outfolder):
        self.setYearMonth(year, month)
        self.setDestFolder(outfolder)
        self.setCell((100,100),'darkred','white')
        self.setHeader((100,30),'black','white')
        print(f'Generating Calendar image of month {self.month}, year {self.year}')
        self.generateCalendar(outfolder+outname)


for i in range(1,13):
    c=calendar()
    c.saveImage(2020, i, "2020{0}.png".format(str(i).zfill(2)), 'temp/print_calendar/')

#References:
#https://code-maven.com/create-images-with-python-pil-pillow
#https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python

#calendar has methods to print text/html calendar
#import calendar
#obj=calendar.TextCalendar(1)
#calendar.prcal(2020)