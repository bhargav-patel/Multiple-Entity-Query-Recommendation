#step4 : extracting artists related to filterd tracks

artistsFile = "../Data/30MDataset/idomaar/entities/persons.idomaar"
filterdTracksFile = "filteredDataset/filteredTracks.idomaar"
filterdArtistsFile = "filteredDataset/filteredPersons.idomaar"

#============ getting list of artists in filterdTracksFile
artists = set()
invalidLines = 0

for line in open(filterdTracksFile):
	try:
		splittedLine = line.split('\t')
		
		jsonData = splittedLine[4]
		playlistObject = eval(jsonData)

		artistsInTrack = playlistObject["artists"]
		artistsId = set([ artist["id"] for artist in artistsInTrack ])

		for a in artistsId:
			artists.add(a)

	except Exception as e:
		invalidLines += 1
		continue

print("#invalid lines in filteredTracksFile : ",invalidLines)
print("#artists related to filteredTracksFile : ",len(artists))

#============ filtering tags
outFile = open(filterdArtistsFile,"w")
count = 0

for line in open(artistsFile):
	
	splittedLine = line.split('\t')
	artistNumber = int(splittedLine[1])

	if artistNumber in artists:
		outFile.write(line)
		count +=1

print("#artists written in filterd file : ",count)