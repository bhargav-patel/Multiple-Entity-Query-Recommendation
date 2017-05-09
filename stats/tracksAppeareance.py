import matplotlib.pyplot as plt
import numpy as np

file = open("../Data/30MDataset/idomaar/entities/playlist.idomaar")


total = 0
numPlaylists = 0

playListIndex = {}
invalidLines = 0

for line in file:

	try:
		splittedLine = line.split('\t')

		playlistNumber = int(splittedLine[1])
		jsonData = splittedLine[4]

		playlistObject = eval(jsonData)

		tracks = playlistObject["objects"]

		for track in tracks:
			try:
				playListIndex[track["id"]] += [playlistNumber]
			except:
				playListIndex[track["id"]] = [playlistNumber]

	except Exception as e:
		invalidLines += 1
		pass

#np.save("playListIndex.npy",playListIndex)

#print(playListIndex)
#print(invalidLines)

trackFrequency = [ len(x) for x in playListIndex.values() ]
maxFrequenency = max(trackFrequency)

# plotX = xrange(1,maxFrequenxy)
# plotY = [ trackFrequency.count(freq) for freq in plotX ]

#print(maxFrequenency)
plt.hist(trackFrequency,bins=maxFrequenency)
plt.show()
