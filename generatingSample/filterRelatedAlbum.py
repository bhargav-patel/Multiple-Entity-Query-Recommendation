#step5 : extracting albums related to filterd tracks ( filterRelatedAlbum.py )

albumsFile = "../Data/30MDataset/idomaar/entities/albums.idomaar"
filterdTracksFile = "filteredDataset/filteredTracks.idomaar"
filterdAlbumsFile = "filteredDataset/filteredAlbums.idomaar"

#============ getting list of artists in filterdTracksFile
albums = set()
invalidLines = 0

for line in open(filterdTracksFile):
	try:
		splittedLine = line.split('\t')
		
		jsonData = splittedLine[4]
		playlistObject = eval(jsonData)

		albumsInTrack = playlistObject["albums"]
		albumsId = set([ album["id"] for album in albumsInTrack ])

		for a in albumsId:
			albums.add(a)

	except Exception as e:
		invalidLines += 1
		continue

print("#invalid lines in filteredTracksFile : ",invalidLines)
print("#artists related to filteredTracksFile : ",len(albums))

#============ filtering tags
outFile = open(filterdAlbumsFile,"w")
count = 0

for line in open(albumsFile):
	
	splittedLine = line.split('\t')
	albumNumber = int(splittedLine[1])

	if albumNumber in albums:
		outFile.write(line)
		count +=1

print("#albums written in filterd file : ",count)