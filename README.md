30Nama Downloader
```python
from cinema_helper import Cinema
downloader = Cinema('USER TOKEN HERE')
post = downloader.find_post_by_id('ID HERE')

# general info : 
print("POST ID : %s", post.id)
print("POST TYPE : %s", post.type) # Series or Movie
print("POST NAME : %s", post.name)

# get playlists :

# if post is movie :
for quality in post.downloads:
    print("PLAYLIST DOWNLOAD LINK / QUALITY : %s / %s", quality.link, quality.label)
    # for download :
    quality.download()
print("SUBTITLE DOWNLOAD LINK : %s", post.subtitle.fa) # post.subtitle.fa/en

# if post is a series:
for season in post.seasons:
    for episode in season.episodes:
        for quality in episode.downloads:
            print("PLAYLIST DOWNLOAD LINK / QUALITY : %s / %s", quality.link, quality.label)
            # for download :
            quality.download()
        print("SUBTITLE DOWNLOAD LINK : %s", episode.subtitle.fa) # post.subtitle.fa/en
```
