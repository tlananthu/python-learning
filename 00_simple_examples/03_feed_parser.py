def download(url, file):
    import os, requests

    if not os.path.isfile(file):
        r=requests.get(url, stream=True)
        with open(file, 'wb') as f:
            f.write(r.content)
    
def readFeed(url, downloadMatch):
    import feedparser
    import json

    NewsFeed=feedparser.parse(url)
    entries=NewsFeed.entries

    for entry in entries:
        for key in entry.keys():
            title=str(entry['title']).replace(':','')
            ext="m"+str(entry['links'][1]['href']).rsplit('.m')[1]
            href=entry['links'][1]['href']
            print(ext)
            print(title)
            # if downloadMatch in title:
            #     download(href, title)

readFeed('https://anchor.fm/s/cf2ac40/podcast/rss', 'Sivagamiyin Sabatham Part 1')