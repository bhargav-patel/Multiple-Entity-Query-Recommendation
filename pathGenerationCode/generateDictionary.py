def getAdjList(fileName,forwardDict = None,inverseDict = None):
	with open(fileName) as file:
		
		if forwardDict is None:
			forwardDict = {}
		if inverseDict is None:
			inverseDict = {}
		
		for line in file:
			print(fileName,line)
			i,j = map(int,line.split(' '))

			try:
				forwardDict[i].append(j)
			except:
				forwardDict[i] = [j]

			try:
				inverseDict[j].append(i)
			except:
				inverseDict[j] = [i]

	return forwardDict,inverseDict

def buildGraph(graphDirPath,nodeTypes,edgeTypes):

	adjListMat = [ [ None for j in row ] for row in edgeTypes ]
	nodeListMat = [ list(set([ int(line.strip()) for line in open(graphDirPath+'nodes/'+file).readlines() ])) for file in nodeTypes ]

	for i in range(len(adjListMat)):
		for j in range(len(adjListMat)):
			if edgeTypes[i][j] is not None:
				if i!=j:
					adjListMat[i][j],adjListMat[j][i] = getAdjList(graphDirPath+'edges/'+edgeTypes[i][j],adjListMat[i][j],adjListMat[j][i])
				else:
					adjListMat[i][j],_ = getAdjList(graphDirPath+'edges/'+edgeTypes[i][j])

	# print(adjListMat)
	# print(nodeListMat)

	return nodeListMat,adjListMat
