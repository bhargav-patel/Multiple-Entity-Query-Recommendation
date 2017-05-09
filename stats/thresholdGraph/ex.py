import matplotlib.pyplot as plt
import numpy

f = open("op")
i = 0
OneHopNeighbours = []
numTracks = []
for line in f:
	i+=1
	if i%2==1:
		#print(int(line.split()[-1][:-1]))
		OneHopNeighbours.append(int(line.split()[-1][:-1]))
	else:
		#print(int(line.split()[-1][:-1]))
		numTracks.append(int(line.split()[-1][:-1]))
		
#print(len(OneHopNeighbours))
#print(len(numTracks))

oh = plt.plot(OneHopNeighbours[:50])
tr = plt.plot(numTracks[:50])
plt.legend([oh, tr], ['numTracks','OneHopNeighbours'])


#fig = plt.figure()
#ax = fig.gca()
#plt.scatter(OneHopNeighbours,numTracks)
#ax.set_xticks(numpy.arange(0, len(OneHopNeighbours), 1))
#ax.set_yticks(numpy.arange(0, max(OneHopNeighbours), 10000))

plt.grid()

#plt.yscale('log')
plt.show()
