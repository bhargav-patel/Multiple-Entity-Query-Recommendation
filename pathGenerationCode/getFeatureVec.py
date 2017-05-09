import generatePathTypes as gpt
import generateDictionary as gd


def getFilteredPathTypes(PATH_LEN):
	#setting graph files
	graphDirPath = 'graph/'
	nodeTypes = [
					'artist',
					'album',
					'track',
					'tag'
				]
	edgeTypes = [
					[ 	'artist_artist'	,	'artist_album'	,		None	,	'artist_tag'	],
					[ 		None		,	'album_album'	,		None	,	None		],
					[ 	'track_artist'	,	'track_album'	,		None	,	'track_tag'		],
					[ 	'tag_album'		,		None		,		None	,	'tag_tag'		],
				]

	#setting path length
	# PATH_LEN = 6

	#generating adj lists
	nodeListMat,adjListMat = gd.buildGraph(graphDirPath,nodeTypes,edgeTypes)

	#generating path types of PATH_LEN-2
	pathTypes = gpt.genPathTypes(nodeTypes,PATH_LEN-2)
	# print("Num path types : ",len(pathTypes),pathTypes[:2])

	#appending track at begining and end of pathType
	pathTypes = [ [2]+pt+[2] for pt in pathTypes ]
	print("Num path types : ",len(pathTypes),pathTypes[:2])	

	#filtering paths with invalid eges by using adjListMat
	filteredPathTypes = gpt.filterPathTypes(pathTypes,adjListMat)
	print("Num filtered path types : ",len(filteredPathTypes),filteredPathTypes[:2])

	return filteredPathTypes,nodeListMat,adjListMat

#recursive function which performs dfs from node and returns path
def findPathsFromNode(path,pathType,endNode,nodeListMat,adjListMat,prob=1.0,depth=1):
	
	if depth==len(pathType) and path[depth-1]==endNode:
		return [(path,prob)]

	paths = []

	try:
		adjNeighbours = adjListMat[pathType[depth-1]][pathType[depth]][path[-1]]
	except Exception as e:
		# print(e,path,depth)
		return paths

	outDegree = len(adjNeighbours)

	# print(depth,pathType,outDegree,path,prob)

	for nbr in adjNeighbours:
		if ( (nbr in path) and (pathType[path.index(nbr)]==pathType[depth]) ):
			continue
		paths.extend(
			findPathsFromNode(
				path+[nbr],
				pathType,
				endNode,
				nodeListMat,
				adjListMat,
				prob*(1.0/outDegree),
				depth+1
			)
		)

	return paths

def getFeatureVec(pathTypes,startTrack,endTrack,nodeListMat,adjListMat):
	featureVec = []
	for pt in pathTypes:
		paths = findPathsFromNode([startTrack],pt,endTrack,nodeListMat,adjListMat)
		probSum = sum([ p[1] for p in paths ])
		# print(pt,paths,probSum)
		#check
		if probSum>1:
			raise Exception
		featureVec.append(probSum)
	return featureVec

# fv = getFeatureVec(getFilteredPathTypes(6),1,2)#nodeListMat[2][0],nodeListMat[2][1])
# print(fv)
# print(len(fv))
'''
def getFeatureMat(trackPairs,PATH_LEN):
	featureMat = []
	pathTypes,nodeListMat,adjListMat = getFilteredPathTypes(PATH_LEN)

	for pair in trackPairs:
		featureMat.append(
				getFeatureVec(
						pathTypes,pair[0],pair[1],nodeListMat,adjListMat
					)
			)
	return featureMat

fm = getFeatureMat([(1,2),(2,1)],7)
print(fm)
print(len(fm),'X',len(fm[0]))
print(sum(fm[0]),sum(fm[1]))

'''
PATH_LEN = 4
pathTypes,nodeListMat,adjListMat = getFilteredPathTypes(PATH_LEN)
print("numPathTypes : ", len(pathTypes))

file = open("positive.txt")
out = open("outPositive.txt","w")
count = 0
for line in file:
	count += 1
	print(count)
	sl = line.split()
	fv = getFeatureVec(
					pathTypes,int(sl[0]),int(sl[1]),nodeListMat,adjListMat
				)
	out.write(sl[0]+','+sl[1]+','+(','.join(list(map(str,fv))))+','+'1\n')
