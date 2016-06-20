#!/usr/bin/python
import sys
import math
from subprocess import Popen, PIPE
#init_centroid = '/mda/c1.txt'  #randomly choosen points
#init_centroid = "c2.txt" #points scattered as far as possible

def getEuclideanDistance(v1,v2):
	dist = [(a - b)**2 for a, b in zip(v1, v2)]
	dist = math.sqrt(sum(dist))
	return dist
centroid_dict = dict()
def getSquaredDistance(v1,v2):
	sqdist = [(a-b)**2 for a,b in zip(v1,v2)]
	sqdist = sum(sqdist)
	return sqdist
def readCentroidFiles():
	proc = Popen(['hdfs','dfs','-cat','/mda/c1.txt'], stdout=PIPE)
	countLine = 1
	for line in proc.stdout:
		data = map(float, line.strip().split(' '))
		if data[0] > 10000.0:
			continue
		centroid_dict[countLine] = data
		countLine+=1
cluster = dict()
readCentroidFiles()
sumofdist = 0
for line in sys.stdin:
	smallest_dist = 1000000.0
	x = map(float, line.strip().split(' '))
	for i in centroid_dict.iterkeys():
		if smallest_dist > getEuclideanDistance(centroid_dict[i],x):
			smallest_dist = getEuclideanDistance(centroid_dict[i],x)
			sqdist = getSquaredDistance(centroid_dict[i],x)
			clusterID = i
	sumofdist += sqdist
	print clusterID, " ".join( repr(e) for e in x)
print sumofdist
