import pytube
vid = pytube.YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')
stream = vid.streams.get_by_itag(251)
stream.download()