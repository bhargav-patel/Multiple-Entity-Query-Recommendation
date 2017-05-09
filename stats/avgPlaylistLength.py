file = open("../Data/30MDataset/idomaar/entities/playlist.idomaar")


total = 0
numPlaylists = 0

for line in file:

	try:
		#jsonData = line.split('\t')[3]
		jsonData = line.split('\t')[4]

		playlistObject = eval(jsonData)

		#total += playlistObject["numtracks"]
		total += len(playlistObject["objects"])


		numPlaylists += 1
	except Exception as e:
		pass

print(total,numPlaylists)
print("Average Playlist Length : ",total/numPlaylists)