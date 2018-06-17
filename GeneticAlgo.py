'''

pm = Probability of mutation
pc = Probability of crossing
r = Crossing point

'''

import numpy as np
import random


r = float()
pm = float()
pc = float()
s = 0

population = np.array( [[0 for j in range(10)] for i in range(50)] )
chromosome = np.array( [0 for i in range(50)] )

childpopulation = np.array( [[0 for j in range(10)] for i in range(40)] )
childchromosome = np.array( [0 for i in range(40)] )

fitpopulation = np.array( [[0 for j in range(10)] for i in range(50)] )
fitchromosome = np.array( [0 for k in range(50)] )

copyfitchromosome = np.array( [0 for k in range(50)] )
	
mutatepopulation = np.array( [[0 for j in range(10)] for i in range(18)] )
mutatechromosome = np.array( [0 for i in range(18)] )

interchromosome = np.array( [0 for i in range(108)] )

bestpopulation = np.array( [0 for i in range(10)] )
bestchromosome = 0



def GenerateRendom(a, b):
	x = random.uniform(a, b)
	return x



def encoding():
	
	for i in range(50):
		for j in range(10):
			Rendom = GenerateRendom(0, 1)
			
			if Rendom > 0.5:
				population[i][j] = 1
			else:
				population[i][j] = 0
	

	for i in range(50):
		for j in range(10):
			chromosome[i] += population[i][j] * ( 2**(9-j) )
			


def selection():

	for k in range(50):
		x1 = int( GenerateRendom(0, 50) )
		x2 = int( GenerateRendom(0, 50) )
		
		if chromosome[x1] > chromosome[x2]:
			fitchromosome[k] = chromosome[x2]
			
		else:
			fitchromosome[k] = chromosome[x1]
			
	
	for i in range(50):
		copyfitchromosome[i] = fitchromosome[i]
		
	for i in range(50):
		for j in range(9, -1, -1):
			fitpopulation[i][j] = copyfitchromosome[i]%2
			copyfitchromosome[i] = copyfitchromosome[i]/2
	


def crossing():
	pc = int(0.8*50)
	r = int( GenerateRendom(0, 1) )
	
	for i in range(0, pc, 2):
		k1 = int( GenerateRendom(0, pc) )
		k2 = int( GenerateRendom(0, pc) )
		
		for j in range(10):
			if j<r:
				childpopulation[i][j] = fitpopulation[k1][j]
				childpopulation[i+1][j] = fitpopulation[k2][j]
				
			else:
				childpopulation[i][j] = fitpopulation[k2][j]
				childpopulation[i+1][j] = fitpopulation[k1][j]
				
				
	for i in range(pc):
		for j in range(10):
			childchromosome[i] += childpopulation[i][j] * (2**(9-j))
			

			
def mutation():
	pm = int(0.2 * 90)
	
	for i in range(pm):
		
		r = int( GenerateRendom(0, pm) )
		for j in range(10):
			if childpopulation[r][j] == 0:
				mutatepopulation[i][j] = 1
				
			else:
				mutatepopulation[i][j] = 0
		
	for i in range(pm):
		for j in range(10):
			mutatechromosome[i] += mutatepopulation[i][j] * (2**(9-j))
	

	
def nextgeneration():
	
	k = 0
	
	interchromosome = np.array( [0 for i in range(108)] )
	
	for i in range(50):
		interchromosome[k] = fitchromosome[i]
		k = k+1
		
	for i in range(40):
		interchromosome[k] = childchromosome[i]
		k = k+1
		
	for i in range(18):
		interchromosome[k] = mutatechromosome[i]
		k = k+1
		
	interchromosome = np.sort(interchromosome)
	
	for i in range(50):
		chromosome[i] = interchromosome[i]
		
	
	
encoding()

while(1):
	s = 0
	selection()
	crossing()
	mutation()
	nextgeneration()
	print(chromosome)
	
	for i in range (50):
		if chromosome[0] != chromosome[i]:
			s = s+1
	
	if s == 0:
		break


bestchromosome = chromosome[0]

for i in range(9, -1, -1):
	bestpopulation[i] = chromosome[0]%2
	chromosome[0] = chromosome[0]/2


print('Best Chromosome is ', bestchromosome)
print('Best Population is ', bestpopulation)