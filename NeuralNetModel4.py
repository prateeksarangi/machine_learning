import math
import statistics
import random
import numpy as np
import matplotlib.pyplot as plt


Ai = np.array( [[0.1, 0.1], [0.1, 0.9], [0.9, 0.1], [0.9, 0.9]] )
Tk = np.array( [0.1, 0.9, 0.9, 0.1] )

Wji = np.random.rand(4, 2)
Wkj = np.random.rand(4)

Itr = np.array( [0 for i in range(5000)] )

Wji = Wji - 0.5
Wkj = Wkj - 0.5

Slopj = np.array( [0.0 for i in range(4)] )
Slopk = np.array( [0.0 for i in range(4)] )

Aj = np.array( [0.0 for i in range(4)] )
Ak = np.array( [0.0 for i in range(4)] )

Netj = np.array( [0.0 for i in range(4)] )
Netk = np.array( [0.0 for i in range(4)] )

Ek = np.array( [0.0 for i in range(4)] )
Error = np.array( [0.0 for i in range(5000)] )
EkEnd = 0.0

ErrorArr = ( [[0.0 for j in range(3)] for i in range(4)] )

def GenerateRandom(a, b):
	x = random.uniform(a, b)
	return x
	

def Tanh(x):
	Ans = ( 1 - math.exp(-x) ) / ( 1 + math.exp(-x) )
	return Ans
	

def Get1DSum(x, y):
	a = np.array( [0.0 for i in range(4)] )
	for i in range(4):
		a[i] = x[i]*y[i]
		
	return a


def Get2DSum(x, y):
	a = np.array( [0.0 for i in range(4)] )
	for i in range(4):
		for j in range(2):
			a[i] = a[i] + x[i][j]*y[i][j]
			
	return a


def FindNetj(Ai, Wji):
	Netj = Get2DSum(Ai, Wji)
	Netj = Netj +1
	return Netj


def FindAj(Netj, Slopj):
	for i in range(4):
		Aj[i] = Tanh(Netj[i]*Slopj[i])
		
	return Aj
	

def FindNetk(Aj, Wkj):
	Netk = Get1DSum(Aj, Wkj)
	Netk = Netk+1
	return Netk
	
	
def FindAk(Netk, Slopk):
	for i in range(4):
		Ak[i] = Tanh(Netk[i]*Slopk[i])
		
	return Ak


def FindError(Tk, Ak):
	Ek = Tk - Ak
	return Ek
	

def FindAbsError(Tk, Ak):
	E = 0.0
	for i in range(4):
		E = E + ((0.5)*(Tk[i]-Ak[i])**2 )
	E = E/4
	
	return E


def UpdateWkj(Wkj, Ek, Aj):
	delWkj = (0.1)*(Ek*Aj*( 1-(Ak**2) )) / 2
	Wkj = Wkj + delWkj
	
	return Wkj


def UpdateWji(Wji, Ek, Wkj, Ak):
	delWji = np.array( [0.0 for i in range(4)] )
	
	for i in range(4):
		delWji[i] = (0.1)*(Ek[i]*Wkj[i]*Ai[i][0]*( 1-(Ak[i]**2) )*( 1-Aj[i]**2 )) / 4
	
	for i in range(4):
		for j in range(2):
			Wji[i][j] = delWji[i]
	
	return Wji


def UpdateSlopek(Slopk, Ek, Ak, Netk):
	delSlopk = ( 0.001*Ek*Netk*( 1-(Ak**2) ) ) / 2
	Slopk = Slopk + delSlopk
	return Slopk
	
	
def UpdateSlopej(Slopj, Ek, Netj, Aj, Wkj):
	delSlopj = ( 0.001*Ek*Netj*Wkj*( 1-(Aj**2) ) ) / 2
	Slopj = Slopj + delSlopj
	return Slopj

	
def ShowTable():
	Err = np.array( [0.0 for i in range(4)] )
	ERR = 0.0
	
	Err = Tk - Ak
	
	ErrorArr[0] = Ak
	ErrorArr[1] = Tk
	ErrorArr[2] = Err
	
	print('\n\nTable\n')
	
	for i in range(3):
	
		if i == 0:
			print('Estimated Values')
			
		elif i == 1:
			print('Correct Values')
			
		else:
			print('Error')
			
		for j in range(4):
			print(ErrorArr[i][j], end = ',')
		print('\n')
	
	for i in range(4):
		ERR = ERR + Err[i]
		
	ERR = ERR/4
	
	print('Average Error =',ERR)

'''	plt.plot(Itr, Error, '-')
	plt.show()'''
	
	
	
for i in range(5000):
	Itr[i] = i


	

for i in range(5000):
	Netj = FindNetj(Ai, Wji)
	Aj = FindAj(Netj, Slopj)
	Netk = FindNetk(Aj, Wkj)
	Ak = FindAk(Netk, Slopk)
	Ek = FindError(Tk, Ak)
	E = FindAbsError(Tk, Ak)
	Error[i] = E
	Wkj = UpdateWkj(Wkj, Ek, Aj)
	Wji = UpdateWji(Wji, Ek, Wkj, Ak)
	Slopj = UpdateSlopej(Slopj, Ek, Netj, Aj, Wkj)
	Slopk = UpdateSlopek(Slopk, Ek, Ak, Netk)
	
	if Error[i] < 0.001:
		print('Model4 converse at', i)
		break

print('\n\n')
	
#ShowTable()