import NeuralNetModel3 as N3
import NeuralNetModel4 as N4
import matplotlib.pyplot as plt



N3.ShowTable()
N4.ShowTable()


Model3 = plt.plot(N3.Itr, N3.Error, '-', color = 'red', label = 'Model3')
Model4 = plt.plot(N4.Itr, N4.Error, '-', color = 'blue', label = 'Model4')

plt.legend( loc = 'upper right' )
plt.show()