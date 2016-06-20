#!/usr/bin/python
import sys
from itertools import izip
sumofpoints = dict()
clusteroccurences = []
cost = 0.0
for line in sys.stdin:
	count = 0
	data = map(float, line.strip().split(' '))
	clusteroccurences.append(int(data[0]))
	if data[0] > 1000.0:
		cost += data[0]
	elif int(data[0]) in sumofpoints:
		sumofpoints[int(data[0])] = [a + b for a, b in izip(sumofpoints[int(data[0])],data[1:])]
	else:
		sumofpoints[int(data[0])] = data[1:]
		count = 1
for i in range(1,11):
	sumofpoints[i] = [x/clusteroccurences.count(i) for x in sumofpoints[i]]
for k, v in sumofpoints.iteritems():
	print " ".join( repr(e) for e in v)
print cost
