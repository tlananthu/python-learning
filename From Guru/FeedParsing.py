import feedparser
import os
import requests

class FeedParsing:
    path="https://anchor.fm/s/cf2ac40/podcast/rss"
    outdir="C:/Users/ananthan/Documents/PYthonLearn/temp/podcast_download"
    chks_m4a=["m4a", "http"]
    chks_mp3=["mp3", "http"]
    def readRss(self):
        NewsFeed = feedparser.parse(self.path)
        for entry in NewsFeed.entries:
            for val in entry.values():
                value=str(val)
                #print (" Value is :"+ value)
                
                if all(x in value for x in self.chks_m4a):
                    #print(" Link is :"+ value)
                    self.download(val, ".m4a", "Sivagamiyin-Sabatham-Part-2")
                if all(x in value for x in self.chks_mp3):
                    #print(" Link is :"+ value)
                    self.download(val, ".mp3", "Sivagamiyin-Sabatham-Part-2")
    
    def download(self, link, ext, matchstr):
        #print(" Downloading ..."+ str(link))
        nm=link[0]
        name= nm.get('href')
        name=os.path.basename(name)+ext
        val=link[1]
        value=val.get('href')
        #print(" Name is : "+name+" val is "+ value)
        if matchstr in link:
            print('Download')
            #myfile = requests.get(value)
            #open(os.path.join(self.outdir, name), 'wb').write(myfile.content)
            
def main():
    fp = FeedParsing()
    fp.readRss()

main()
