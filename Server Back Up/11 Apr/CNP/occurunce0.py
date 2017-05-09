#step1 : extracting tracks with frequency in playlist with some threshold and take their one hop neighbours

# import matplotlib.pyplot as plt
import numpy as np


playListsFile = "filteredDataset/filteredPlaylists.idomaar"
file = open(playListsFile)


#============= creating track index with their appearence in playlist as value
playListIndex = {}
trackIndex = {}
invalidLines = 0
lineNum = 0

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
				playListIndex[track["id"]].add(playlistNumber)
			except:
				playListIndex[track["id"]] = set([playlistNumber])
				
		lineNum += 1
		print(lineNum)

	except Exception as e:
		invalidLines += 1
		print(invalidLines	)
		pass

file.close()
#============= filtering tracks with threshold

OneHopNeighbours = []
numTracks = []


THRESHOLD = 25
topTracks = [ k for (k,v) in playListIndex.items() if len(v)>=THRESHOLD ]

print("top tracks with threshold",THRESHOLD,"is :",len(topTracks))


upTo = 1000
files = []
for i in range(upTo+1):
	files.append(open("training/coOccurunce"+str(i)+".txt","w"))
trackList = topTracks
totalPairs = (len(trackList)*(len(trackList)-1))/2
pairCount = 0
print("COUNTING COOCCURENCE",totalPairs)
for i in range(len(trackList)):
	for j in range(i):
		#coOccurunce[ (i,j) ] = len(playListIndex[trackList[i]]&playListIndex[trackList[j]])
		count = len(playListIndex[trackList[i]]&playListIndex[trackList[j]])
		if count<upTo:
			files[count].write(str(trackList[i])+'\t'+str(trackList[j])+'\t'+str(count)+'\n')
		else:
			files[upTo].write(str(trackList[i])+'\t'+str(trackList[j])+'\t'+str(count)+'\n')
		pairCount += 1
		if pairCount%100000==0:
			print (pairCount/(totalPairs*1.0))," : ",pairCount,"/",totalPairs
			for file in files:
				file.flush()
# file.close()
print "DONE"

'''
print "MAXIMUM CO-OCCURUNCE COUNT :",max(coOccurunce.values())
	
#save_obj(coOccurunce, "coOccurunce" )

THRESHOLD = 2
pairs = [ x for x in coOccurunce.keys() if coOccurunce[x]>=THRESHOLD ]
print "#PAIRS WITH CO-OCCURUNCE MORE THAN",THRESHOLD,":",len(pairs)
'''
