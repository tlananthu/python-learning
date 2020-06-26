import os
basepath="C:/Temp/ic/"
files=os.listdir(basepath)

for file in files:
    #print(file)
    seriesname="Indrajal Comics"
    data=file.lstrip("Indrajal ").split("-")
    #print(data)
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

    if author=="": author="Unknown"


    newname=f'{seriesname} - {series} - {tag} - {author} - {title} - {seriesname}.pdf'
    # if author=="Unknown":
    #     print(newname)
    if lowertag=="bahadur":
        os.remove(basepath+file)
    else:
        os.rename(basepath+file, basepath+newname)