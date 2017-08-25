#!/usr/bin/python

#  Write a MapReduce program which will display the number of hits for each different file on the Web site.
import sys

salesTotal = 0
oldKey = None
higestPath = ""
higestHits = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
    # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data

    if oldKey and  oldKey != thisKey:
      	#print oldKey, "\t", salesTotal
      	salesTotal = 0
    oldKey = thisKey
    salesTotal += float(thisSale)
    if higestHits < salesTotal:
	higestHits = salesTotal
	higestPath = thisKey

    #if oldKey != None:
print higestPath, "\t", higestHits
