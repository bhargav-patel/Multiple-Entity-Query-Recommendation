import numpy as np


trackNodes = set(map(int,open('track').readlines()))

playListsFile = "filteredPlaylists.idomaar"
outFile = open('mulTrain.txt',"w")
invalidLines = 0
count = 0

for line in open(playListsFile):
	try:
		splittedLine = line.split('\t')

		playlistNumber = int(splittedLine[1])
		
		jsonData = splittedLine[4]
		playlistObject = eval(jsonData)

		tracksInPlaylist = playlistObject["objects"]
		tracksId = [ track["id"] for track in tracksInPlaylist ]

		isGood = True

		for t in tracksId:
			if not t in trackNodes:
				isGood = False
				break

		tracksId = [ str(x) for x in tracksId ]
		if isGood:
			y = np.random.randint(len(tracksId))
			outFile.write(','.join(tracksId[:y]+tracksId[y+1:])+','+tracksId[y]+'\n')
			count += 1
			print(count)

	except Exception as e:
		print(e)
		invalidLines += 1
		continue

print("#invalid lines in playlists file : ",invalidLines)
print("#playlists written in filterd file : ",count)