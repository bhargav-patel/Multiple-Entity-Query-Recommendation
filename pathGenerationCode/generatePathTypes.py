import itertools

# nodeTypes = [ 'Track','Artist','Tag','Album' ]

def genPathTypes(nodeTypes,PATH_LEN):
	numNodeTypes = len(nodeTypes)

	id_to_nodeType = dict(enumerate(nodeTypes))
	nodeType_to_id = dict([ (_2,_1) for _1,_2 in enumerate(nodeTypes) ])

	choices = range(numNodeTypes)
	choicesList = [ choices for i in range(PATH_LEN) ]

	pathTypes = list(itertools.product(*choicesList))
	workingSet = [ pt for pt in pathTypes ]

	while len(pathTypes[-1])!=1:
		workingSet = set([ pt[:-1] for pt in workingSet ])
		pathTypes += workingSet

	# print(len(pathTypes))

	nonReversedPathTypes = []
	for pt in pathTypes:
		if not tuple(reversed(pt) ) in nonReversedPathTypes:
			 nonReversedPathTypes.append(pt)

	# for pt in nonReversedPathTypes:
	#     print( ' -> '.join([ id_to_nodeType[t] for t in pt ])  )

	# print("Unique(non reverse) path types with atmost\n\tPATH_LEN",PATH_LEN,":",len(nonReversedPathTypes))

	return list(map(list,nonReversedPathTypes))

# genPathTypes(nodeTypes)

def filterPathTypes(pathTypes,adjListMat):
	filteredPathTypes = []

	for pt in pathTypes:
		valid = True
		for i in range(len(pt)-1):
			if adjListMat[pt[i]][pt[i+1]] is None:
				valid = False
				break
		if valid:
			filteredPathTypes.append(pt)

	return filteredPathTypes