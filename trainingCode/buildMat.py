import numpy as np
from scipy.sparse import csc_matrix

def pageRank(G, s = .85, maxerr = .0001):
    """
    Computes the pagerank for each of the n states
    Parameters
    ----------
    G: matrix representing state transitions
       Gij is a binary value representing a transition from state i to j.
    s: probability of following a transition. 1-s probability of teleporting
       to another state.
    maxerr: if the sum of pageranks between iterations is bellow this we will
            have converged.
    """
    n = G.shape[0]

    # transform G into markov matrix A
    A = csc_matrix(G,dtype=np.float)
    rsums = np.array(A.sum(1))[:,0]
    ri, ci = A.nonzero()
    A.data /= rsums[ri]

    # bool array of sink states
    sink = rsums==0

    # Compute pagerank r until we converge
    ro, r = np.zeros(n), np.ones(n)
    while np.sum(np.abs(r-ro)) > maxerr:
    	# print(np.sum(np.abs(r-ro)))
        ro = r.copy()
        # calculate each pagerank at a time
        for i in xrange(0,n):
            # inlinks of state i
            Ai = np.array(A[:,i].todense())[:,0]
            # account for sink states
            Di = sink / float(n)
            # account for teleportation to state i
            Ei = np.ones(n) / float(n)

            r[i] = ro.dot( Ai*s + Di*s + Ei*(1-s) )

    # return normalized pagerank
    return r/float(sum(r))

#=========================

posOld = [ line.strip().split(',') for line in open("posFeature.txt").readlines()]
negOld = [ line.strip().split(',') for line in open("negFeature.txt").readlines()]

pos = [ l for l in posOld if len(l)==11 ]
neg = [ l[:-1]+['0'] for l in negOld if len(l)==11 ]

print(len(pos),len(posOld))
print(len(neg),len(negOld))

data = pos+neg

np.random.shuffle(data)

tracks = list(set(list(set([ x[0] for x in data ])) + list(set([ x[1] for x in data ]))))
print(len(tracks))

tracksDict = { tracks[k] : k for k in range(len(tracks)) }
print(len(tracksDict))

minProb = 0.001
G = np.array([ np.array([ minProb for col in range(len(tracks)) ]) for row in range(len(tracksDict)) ])
for ex in pos:
	G[tracksDict[ex[0]]][tracksDict[ex[1]]] = 1
	G[tracksDict[ex[1]]][tracksDict[ex[0]]] = 1


print(G[0])
print("Graph Constructed.")


ranks = pageRank(G,s=.86)
print(np.histogram(ranks))
print(len(ranks))
print(ranks[0])