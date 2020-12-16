import os

def clearlog():
    import os
    os.remove('temp/rename_file/process_log.txt')

def writelog(message):
    import codecs

    f=codecs.open('temp/rename_file/process_log.txt','a','utf-8')
    f.write(message+'\n')
    f.close()
    
clearlog()
basepath="C:/Temp/ic/"
files=os.listdir(basepath)

# for file in files:
#     fn=str(file)
#     nn=fn.replace("Indrajal_","Indrajal ").replace("The_","The ").replace("Mandrake_The","Mandrake").replace("Flash_Gordon","Flash Gordon").replace("Bahadur_The","Bahadur")
#     nn=nn.replace("Phil_Corrigan","Phil Corrigan").replace("_"," - ")
#     #print(nn)
#     os.rename(basepath+fn,basepath+nn)

count=0
for file in files:
    #print(file)
    seriesname="Indrajal Comics"
    data=file.lstrip("Indrajal ").split("-")
    print(data)
    series=data[0].lstrip(" ").lstrip(" ").rstrip(" ")
    title=data[2].replace(".pdf","").lstrip(" ").rstrip(" ")
    tag=data[1].replace("The","").lstrip(" ").rstrip(" ")

    lowertag=tag.lower().replace(" ","").replace("'","")
    author=""
    
    if lowertag=="phantom" or lowertag=="mandrake": author="Lee Falk"
    if lowertag=="waltdisneys": author="Walt Disney"
    if lowertag=="flashgordon" or lowertag=="ripkirby" or lowertag=="philcorrigan": author="Alex Raymond"
    if lowertag=="bahadur": author="Abid Surti"
    if lowertag=="buzsawyer": author="Roy Crane"
    if lowertag=="garth": author="Steve Dowling"
    if lowertag=="dara": author="Kamini Uppal"
    if lowertag=="bahubali" or lowertag=="tendays": 
        author="Rajmal Jain"
        tag="Miscellaneous"
    if lowertag=="nomansland":
        author="Lt. Col. D.G.L.Joseph"
        tag="Miscellaneous"
    if lowertag=="sukhanallah" or lowertag=="curseofgoddess" or lowertag=="jig3" or lowertag=="bridgebusters" or lowertag=="eachhisown": 
        author="Col. C. L. Proudfoot (Retd)"
        tag="Miscellaneous"
    if lowertag=="sultana": 
        author="John Dantes"
        tag="Miscellaneous"
    if lowertag=="sandsoftime": 
        author="Jayawant Dalvi"
        tag="Miscellaneous"
    if lowertag=="kunhalimarakkar":
        author="P.K.Ravindranath"
        tag="Miscellaneous"
    if lowertag=="tulasidas":
        author="Tulasidas"
        tag="Miscellaneous"

    newname=f'{seriesname} - {series} - {tag} - {author} - {title} - {seriesname}.pdf'
    # newname=str(file).replace('@വായനശാല','').replace('_',' ').replace('by',' - ').replace('  ',' ')
    # newname=newname.replace('&','and').replace('(malayalam)','').replace('‘','').replace('’','').replace('(നോവൽ)','')
    # newname=newname.replace('വോള്യം','വോള്യം ').replace(' vol ',' വോള്യം ')
    # newname=newname.rstrip(' ')
    # writelog(newname)
    # os.rename(basepath+file, basepath+newname)
    if author=="Unknown":
        print(newname)
        count+=1

    if lowertag=="bahadur":
        os.remove(basepath+file)
    else:
        os.rename(basepath+file, basepath+newname)

print(count)
