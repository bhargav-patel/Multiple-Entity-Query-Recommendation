import numpy as np


trackNodes = open('track').readlines()
l = len(trackNodes)

posFile = "mulTrain.txt"
negFile = open("mulTrainNeg.txt","w")
invalidLines = 0
count = 0

for line in open(posFile):
	sl = line.split(',')
	negFile.write(','.join(sl[:-1])+','+trackNodes[np.random.randint(l)])
	

print("#invalid lines in playlists file : ",invalidLines)
print("#playlists written in filterd file : ",count)