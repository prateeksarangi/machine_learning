import numpy as np
from statistics import mean
import math
import csv
import random


randomnumber = np.array([0,0,0])
randomdata = np.array( [[0.0 for j in range(4)] for i in range(3)] )
centroid1 = np.array([0.0,0.0,0.0,0.0])
centroid2 = np.array([0.0,0.0,0.0,0.0])
centroid3 = np.array([0.0,0.0,0.0,0.0])
meancluster = np.array([0,0,0,0])
nextcentroid1 = np.array([0.0,0.0,0.0,0.0])
nextcentroid2 = np.array([0.0,0.0,0.0,0.0])
nextcentroid3 = np.array([0.0,0.0,0.0,0.0])
data = np.array( [[0.0 for j in range(4)] for i in range(150)] )
d1 = np.array( [0.0 for i in range(4)] )
d2 = np.array( [0.0 for i in range(4)] )
xd = np.array( [0.0 for i in range(4)] )
ed = np.array( [[0.0 for j in range(3)] for i in range(150)] )
shortested = np.array( [0.0 for i in range(150)] )
cluster1 = np.array( [[0.0 for j in range(4)] for i in range(150)] )
cluster2 = np.array( [[0.0 for j in range(4)] for i in range(150)] )
cluster3 = np.array( [[0.0 for j in range(4)] for i in range(150)] )





def Generaterandom(a, b):
	x = random.randint(a, b)
	return x

def Geteuclidiandistance(d1, d2):
	ed = 0
	for i in range(4):
		xd[i] = d1[i]-d2[i]
		
	for i in range(4):
		ed += (xd[i]**2)
		
	ed = math.sqrt(ed)
	return ed
	

	
	
def Getdata():
	file = open( 'irisflower.csv' )
	reader = csv.reader(file)
	i = 0
	for k, line in enumerate(reader):
		data[k] = line
		
def Getrandomdata():
	for i in range(3):
		x = Generaterandom(0, 149)
		print(x)
		for j in range(150):
			if x == j:
				randomdata[i] = data[j]
				
	print(randomdata)
	
def Getinitialcluster():
	for i in range(150):
		for j in range(3):
			ed[i][j] = Geteuclidiandistance(data[i], randomdata[j])
	
	for i in range(150):
		shortested[i] = ed[i][0]
		
	for i in range(150):
		for j in range(3):
			if shortested[i] > ed[i][j]:
				shortested[i] = ed[i][j]
	k1 = 0
	k2 = 0
	k3 = 0
	
	for i in range(150):
		if shortested[i] == ed[i][0]:
			cluster1[k1] = data[i]
			k1 = k1+1
			
		elif shortested[i] == ed[i][1]:
			cluster2[k2] = data[i]
			k2 = k2+1
			
		elif shortested[i] == ed[i][2]:
			cluster3[k3] = data[i]
			k3 = k3+1
	
	
def Getcentroid():
	
	centroid1 = np.array([0.0,0.0,0.0,0.0])
	centroid2 = np.array([0.0,0.0,0.0,0.0])
	centroid3 = np.array([0.0,0.0,0.0,0.0])
	
	for i in range(4):
		for j in range(150):
			centroid1[i] += cluster1[j][i]
		centroid1[i] = centroid1[i]/150
		
	for i in range(4):
		for j in range(150):
			centroid2[i] += cluster2[j][i]
		centroid2[i] = centroid2[i]/150
		
	for i in range(4):
		for j in range(150):
			centroid2[i] += cluster2[j][i]
		centroid2[i] = centroid2[i]/150
		
	


def GetCluster():
	cluster1 = np.array( [[0.0 for j in range(4)] for i in range(150)] )
	cluster2 = np.array( [[0.0 for j in range(4)] for i in range(150)] )
	cluster3 = np.array( [[0.0 for j in range(4)] for i in range(150)] )
	for i in range(150):
		ed[i][0] = Geteuclidiandistance(data[i], centroid1)
		ed[i][1] = Geteuclidiandistance(data[i], centroid2)
		ed[i][2] = Geteuclidiandistance(data[i], centroid3)
		
	for i in range(150):
		shortested[i] = ed[i][0]
		
	for i in range(150):
		for j in range(3):
			if shortested[i] > ed[i][j]:
				shortested[i] = ed[i][j]
	k1 = 0
	k2 = 0
	k3 = 0
	
	for i in range(150):
		if shortested[i] == ed[i][0]:
			cluster1[k1] = data[i]
			k1 = k1+1
			
		elif shortested[i] == ed[i][1]:
			cluster2[k2] = data[i]
			k2 = k2+1
			
		elif shortested[i] == ed[i][2]:
			cluster3[k3] = data[i]
			k3 = k3+1
			
		
		
		

Getdata()
Getrandomdata()
Getinitialcluster()
Getcentroid()

#print(randomdata)

while(1):
	GetCluster()
	
	for i in range(3):
		s = 0
		nextcentroid1[i] = centroid1[i]
		nextcentroid2[i] = centroid2[i]
		nextcentroid3[i] = centroid3[i]
	
	Getcentroid()
	
	for i in range(3):
		if nextcentroid1[i] == centroid1[i] and nextcentroid2[i] == centroid2[i] and nextcentroid3[i] == centroid3[i]:
			s = 1
			
	if s!=0:
		break


		
print('Cluster1\n', cluster1)
print('Cluster2\n', cluster2)
print('Cluster3\n', cluster3)
'''print(centroid1)
print(centroid2)
print(centroid3)'''