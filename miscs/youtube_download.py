"""Use pytube library to download youtube video specified by url
pytube==11.0.1
Author: Kemin Li
2021-10-10
"""

from pytube import YouTube

#racoon_1 = "https://www.youtube.com/watch?v=7ElXCXN8mGA"
url = "https://www.youtube.com/watch?v=FTcjzaqL0pE"

# get info for all streams
try:
	yt = YouTube(url)
except:
	print(f"Failed to download {url}")

# filter for video (remove audio) and mp4 format
mp4_videos = yt.streams.filter(type="video",subtype="mp4")

# check for video stream in descending resolution
resolutions = ['720p', '480p', '360p']
for res in resolutions:
	if mp4_videos.get_by_resolution(res):
		print(f"Download {res}")
		mp4_videos.get_by_resolution(res).download()
		break

print(f"Cat not find video with resolution {resolutions}")
