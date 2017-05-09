import generatePathTypes as gpt
import generateDictionary as gd

#setting graph files
graphDirPath = 'graph/'
nodeTypes = [
				'artist',
				'album',
				'track',
				'tag'
			]
edgeTypes = [
				[ 	'artist_artist'	,	'artist_album'	,	None	,	'artist_tag'	],
				[ 		None		,		None		,	None	,	'album_tag'		],
				[ 	'track_artist'	,	'track_album'	,	None	,	'track_tag'		],
				[ 		None		,		None		,	None	,	'tag_tag'		],
			]

#setting path length
PATH_LEN = 6

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

#recursive function which performs dfs from node and returns path
def findPathsFromNode(path,pathType,depth=1):
	if depth==len(pathType):
		return [path]

	paths = []

	try:
		adjNeighbours = adjListMat[pathType[depth-1]][pathType[depth]][path[-1]]
	except Exception as e:
		return paths

	for nbr in adjNeighbours:
		if ( (nbr in path) and (pathType[path.index(nbr)]==pathType[depth]) ):
			continue
		paths.extend(findPathsFromNode(path+[nbr],pathType,depth+1))

	return paths

#generating all paths for particular path type
def getPaths(pathType,nodeListMat,adjListMat):

	paths = []
	for node in nodeListMat[pathType[0]]:
		paths += findPathsFromNode([node],pathType)

	uniquePaths = [ list(newPath) for newPath in list(set([ tuple(path) for path in paths ])) ]

	return uniquePaths

for pt in filteredPathTypes:
	print('\n\n===\n',pt,'\n',getPaths(pt,nodeListMat,adjListMat))

