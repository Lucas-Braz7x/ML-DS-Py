import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

''' CRIANDO MATRIZES
a = numpy.array([10, 20, 30, 40])
type(a)

mat = numpy.array([[1,2], [3,4]])
print(mat)
print(mat.transpose())'''

'''CRIANDO E EXIBINDO GRÁFICOS
salario = np.array([100,200,300,400,150])
salario2 = np.array([500, 200, 150, 300, 400])
salario3 = np.array([250,100,490,350,180])

plt.plot(salario, c='Black', ls='--', marker='s', label='Salário 1')
plt.plot(salario2, c='Red', ls='--', marker='s', label='Salário 2')
plt.plot(salario3, c='Green', ls='--', marker='s', label='Salário 3')
plt.legend(loc='upper left')
plt.show()
'''
#INSERINDO ELEMENTOS NO ARRAY
'''
arr = np.array([1,2,3])
print(arr)
arr = np.insert(arr, 1, 10)
print(arr)

a = np.array([[1,2], [3,4]])
print(a)
print(a.ndim)
print(a.sum(axis=0))
print(a.sum(axis=1))
print("\n...............\n\n")
a = np.insert(a, 1, 5, axis=1)
print(a)
#INSERINDO ELEMENTO COM O "APPEND"

arr = np.append(arr, [7,8,9])
print(arr)
'''
#DELETANDO ELEMENTOS DO ARRAY
'''
arr = np.array([[1,2], [3,4], [5,6]])
print(arr)
arr = np.delete(arr, 1, axis=0)
print(arr)
arr = np.delete(arr, 0, 1)
print(arr)
'''

#REPETINDO ELEMENTOS DO ARRAY
'''
arr = np.array([[1,2],[3,4]])
print(arr)
arr = np.repeat(arr, 2)
print(arr)
arr = np.array([[1,2], [3,4]])
print(arr)
arr = np.tile(arr, 5)
print(arr)'''

#DIVIDINDO O ARRAY
'''a = np.array([[1,2,3], [4,5,6]])
print(a)
a = np.array_split(a,2, axis = 0)
print(a)'''

#CRIANDO MATRIZES IDENTIDADES
'''arr = np.zeros(4)
print(arr)
print('\n')
m = np.zeros((2,2))
print(m)
print('\n')
b = np.ones(4)
print(b)
print('\n')
c = np.ones((2,2))
print(c)
print('\n Matriz identidade:\n')
d = np.eye(4)
print(d)'''

#Verificação booleana
'''a = np.array([[1,2], [3,4], [5,6]])
print(a[a>3])
print(a[a<3])'''

#CARREGANDO DADOS DE UM ARQUIVO
'''val1, val2, val3 = np.loadtxt('dados.txt', skiprows=1, unpack=True)
print(val1)
print(val2)
print(val3)
print('\n')

arr= np.genfromtxt('dados2.txt', skip_header=1, filling_values=1000)
print(arr)'''

#JUNTANDO ARRAYS
'''
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.concatenate((a,b), axis= 0)
print(c)
#Embaralhando array
np.random.shuffle(arr)'''

#NÚMEROS COMPLEXOS
'''a = np.array([1,10+2j, 10+5j], dtype=complex)
print(a)'''

#IRIS.DATA

data = np.genfromtxt('iris.data',delimiter=',', usecols=(0,1,2,3))
print(data)
print('\n')
#primeira coluna
print(data[:,0])

#Primeiras 50 colunas
print('\n')
print(data[:50,0])

plt.plot(data[:50,0], c='Red', ls=':', marker='s', ms=8, label='Iris-Setosa')
plt.plot(data[50:100,0], c='Green', ls=':', marker='o', ms=8, label='Iris-versicolor')
plt.legend()
plt.show()



