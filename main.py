from pytube import YouTube
link = "Video link What you want to downbload"
YT = YouTube(link)
YT.streams.first().download()