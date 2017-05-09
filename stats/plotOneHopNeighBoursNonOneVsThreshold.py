#step1 : extracting tracks with frequency in playlist with some threshold and take their one hop neighbours

import matplotlib.pyplot as plt
import numpy as np


playListsFile = "../../Data/30MDataset/idomaar/entities/playlist.idomaar"
file = open(playListsFile)


#============= creating track index with their appearence in playlist as value
playListIndex = {}
trackIndex = {}
invalidLines = 0

for line in file:

	try:
		splittedLine = line.split('\t')

		playlistNumber = int(splittedLine[1])
		jsonData = splittedLine[4]

		playlistObject = eval(jsonData)

		tracks = playlistObject["objects"]

		trackIndex[playlistNumber] = []

		for track in tracks:
			trackIndex[playlistNumber] += [track["id"]]
			try:
				playListIndex[track["id"]] += [playlistNumber]
			except:
				playListIndex[track["id"]] = [playlistNumber]

	except Exception as e:
		invalidLines += 1
		pass

file.close()
#============= filtering tracks with threshold

OneHopNeighbours = []
OneHopNeighboursNonOne = []
numTracks = []


topTracks = [ (k,v) for (k,v) in playListIndex.items() if len(v)>=100 ]
for THRESHOLD in range(101,500):
#THRESHOLD = 40
	topTracks = [ (k,v) for (k,v) in topTracks if len(v)>=THRESHOLD ]

	print("top tracks with threshold",THRESHOLD,"is :",len(topTracks))

	#========= taking one hop neighbours of filterd tracks
	oneHopTracks = set()
	oneHopTracksNonOne = set()
	for (track,_) in topTracks:
		for playlist in playListIndex[track]:
			for playlist_track in trackIndex[playlist]:
				oneHopTracks.add(playlist_track)
				if len(playListIndex[playlist_track])>1:
					oneHopTracksNonOne.add(playlist_track)
				
	OneHopNeighbours.append(len(oneHopTracks))
	OneHopNeighboursNonOne.append(len(oneHopTracksNonOne))
	numTracks.append(len(topTracks))

	print("One hop neighbours ",len(oneHopTracks))
	print("One hop neighbours Non One",len(oneHopTracksNonOne))
	
oh = plt.plot(OneHopNeighbours)
tr = plt.plot(numTracks)
plt.legend([oh, tr], ['OneHopNeighbours', 'numTracks'])
plt.show()
