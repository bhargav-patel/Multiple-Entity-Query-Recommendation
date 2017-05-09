#step1 : extracting tracks with frequency in playlist with some threshold and take their one hop neighbours

import matplotlib.pyplot as plt
import numpy as np


playListsFile = "../Data/30MDataset/idomaar/entities/playlist.idomaar"
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
THRESHOLD = 2

topTracks = [ k for (k,v) in playListIndex.items() if len(v)>=THRESHOLD ]

print("top tracks with threshold",THRESHOLD,"is :",len(topTracks))


#=========== plotting histogram of tracks frequency in playlist
trackFrequency = [ len(x) for x in playListIndex.values() ]
maxFrequenency = max(trackFrequency)

plt.hist(trackFrequency,log=True,bins=maxFrequenency)
plt.title("Number of tracks with particular frequency in playlist")
plt.xlabel("frequency of track in playlist")
plt.ylabel("Number of tracks")
plt.show()

#========= taking one hop neighbours of filterd tracks
oneHopTracks = set()
for track in topTracks:
	for playlist in playListIndex[track]:
		for playlist_track in trackIndex[playlist]:
			oneHopTracks.add(playlist_track)

print("One hop neighbours ",len(oneHopTracks))

#filter out one hop neighbours which appear in only one playlist
filteredOneHopTracks = set([ track for track in oneHopTracks if len(playListIndex[track])>1])
print("Filtered One hop neighbours ",len(filteredOneHopTracks))

#creating file with one hop neighbours
tracksFile = "../Data/30MDataset/idomaar/entities/tracks.idomaar"
filterdTracksFile = "filteredDataset/filteredTracks.idomaar"

file = open(tracksFile)
outFile = open(filterdTracksFile,"w")
count = 0

for line in file:
	
	splittedLine = line.split('\t')
	trackNumber = int(splittedLine[1])

	if trackNumber in filteredOneHopTracks:
		outFile.write(line)
		count +=1
		# print(count)

print("# tracks written in filterd file : ",count)	