#generating the training set

# import matplotlib.pyplot as plt
import numpy as np
import pickle


#dictionry saving and loading functions
def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        print "SAVED TO",'obj/'+ name + '.pkl'

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
        


playListsFile = "filteredDataset/filteredPlaylists.idomaar"
file = open(playListsFile)


#============= creating track index with their appearence in playlist as value
playListIndex = {}
trackIndex = {}
invalidLines = 0
lines = 0

for line in file:
	lines += 1
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

	except Exception as e:
		invalidLines += 1
		pass
		
	print lines
	#if lines > 10:
		#break
		

file.close()

#============= coOccurunce count of tracks
#coOccurunce = dict([  ((i,j),len(playListIndex[i]&playListIndex[j])) for i in playListIndex.keys() for j in playListIndex.keys() if i!=j])
#coOccurunce = {}
upTo = 1000
files = []
for i in range(upTo+1):
	files.append(open("training/coOccurunce"+str(i)+".txt","w"))
trackList = playListIndex.keys()
totalPairs = (len(trackList)*(len(trackList)-1))/2
pairCount = 0
print("COUNTING COOCCURENCE",totalPairs)
for i in range(len(trackList)):
	for j in range(i):
		#coOccurunce[ (i,j) ] = len(playListIndex[trackList[i]]&playListIndex[trackList[j]])
		count = len(playListIndex[trackList[i]]&playListIndex[trackList[j]])
		if count==0:
			pass
		elif count<upTo:
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
