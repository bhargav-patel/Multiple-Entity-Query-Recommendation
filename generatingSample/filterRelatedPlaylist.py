#step2 : extracting playliststs related to filterd tracks

import matplotlib.pyplot as plt
import numpy as np


playListsFile = "../Data/30MDataset/idomaar/entities/playlist.idomaar"
filterdTracksFile = "filteredDataset/filteredTracks.idomaar"
filterdPlaylistsFile = "filteredDataset/filteredPlaylists.idomaar"

#============ getting list of tracks in filterdTracksFile
tracks = set()

for line in open(filterdTracksFile):

	splittedLine = line.split('\t')
	trackNumber = int(splittedLine[1])

	tracks.add(trackNumber)

print("#tracks in filteredTracksFile : ",len(tracks))

#============ filtering playlists
outFile = open(filterdPlaylistsFile,"w")
count = 0
invalidLines = 0

for line in open(playListsFile):
	
	try:
		splittedLine = line.split('\t')

		playlistNumber = int(splittedLine[1])
		
		jsonData = splittedLine[4]
		playlistObject = eval(jsonData)

		tracksInPlaylist = playlistObject["objects"]
		tracksId = set([ track["id"] for track in tracksInPlaylist ])

		if len( tracks & tracksId )!=0:
			outFile.write(line)
			count +=1
	except:
		invalidLines += 1
		continue

print("#invalid lines in playlists file : ",invalidLines)
print("#playlists written in filterd file : ",count)