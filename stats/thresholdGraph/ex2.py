import matplotlib.pyplot as plt
import numpy

f = open("op2")
i = 0
OneHopNeighbours = []
FilteredOneHopNeighbours = []
numTracks = []

for line in f:
	if i%3==1:
		#print(int(line.split()[-1][:-1]))
		OneHopNeighbours.append(int(line.split()[-1][:-1]))
	elif i%3==2:
		FilteredOneHopNeighbours.append(int(line.split()[-1][:-1]))
	else:
		#print(int(line.split()[-1][:-1]))
		numTracks.append(int(line.split()[-1][:-1]))
	i+=1
		
# print(len(OneHopNeighbours))
# print(len(numTracks))
# print(len(FilteredOneHopNeighbours))

oh = plt.plot(OneHopNeighbours)
tr = plt.plot(numTracks)
foh = plt.plot(FilteredOneHopNeighbours)
plt.legend([oh, tr, foh], ['OneHopNeighbours','numTracks', 'FilteredOneHopNeighbours'])


#fig = plt.figure()
#ax = fig.gca()
#plt.scatter(OneHopNeighbours,numTracks)
#ax.set_xticks(numpy.arange(0, len(OneHopNeighbours), 1))
#ax.set_yticks(numpy.arange(0, max(OneHopNeighbours), 10000))
plt.minorticks_on()
plt.grid(which='minor')
plt.grid(which='major')
# plt.grid(b=True, which='major',linestyle='-')

# plt.grid(b=True, which='minor', color='r', linestyle='--')

#plt.yscale('log')
plt.show()
