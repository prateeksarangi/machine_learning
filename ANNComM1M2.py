import NeuralNetModel1 as N1
import NeuralNetModel2 as N2
import matplotlib.pyplot as plt



N1.ShowTable()
N2.ShowTable()


Model1 = plt.plot(N1.Itr, N1.Error, '-', color = 'red', label = 'Model1')
Model2 = plt.plot(N2.Itr, N2.Error, '-', color = 'blue', label = 'Model2')

plt.legend( loc = 'upper right' )
plt.show()