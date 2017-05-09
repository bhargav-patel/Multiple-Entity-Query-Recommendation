#step3 : extracting tags related to filterd tracks

tagsFile = "../Data/30MDataset/idomaar/entities/tags.idomaar"
filterdTracksFile = "filteredDataset/filteredTracks.idomaar"
filterdTagsFile = "filteredDataset/filteredTags.idomaar"

#============ getting list of tags in filterdTracksFile
tags = set()
invalidLines = 0

for line in open(filterdTracksFile):
	try:
		splittedLine = line.split('\t')
		
		jsonData = splittedLine[4]
		playlistObject = eval(jsonData)

		tagsInTrack = playlistObject["tags"]
		tagsId = set([ track["id"] for track in tagsInTrack ])

		for t in tagsId:
			tags.add(t)

	except:
		invalidLines += 1
		continue

print("#invalid lines in filteredTracksFile : ",invalidLines)
print("#tags related to filteredTracksFile : ",len(tags))

#============ filtering tags
outFile = open(filterdTagsFile,"w")
count = 0
invalidLines = 0

for line in open(tagsFile):
	
	splittedLine = line.split('\t')
	tagNumber = int(splittedLine[1])

	if tagNumber in tags:
		outFile.write(line)
		count +=1

print("#tags written in filterd file : ",count)