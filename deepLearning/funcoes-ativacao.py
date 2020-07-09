# transfer function
# usado para determinar a saída de um neurônio

import numpy as np

# tudo ou nada
# problemas linearmente separáveis
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

# retornar probabilidades
# The softmax function is a more generalized logistic activation 
# function which is used for multiclass classification.
def sigmoid(soma):
    return 1/(1+np.exp(-soma))

# tanh para classificação de duas classes
# A vantagem é que as entradas negativas serão mapeadas fortemente 
# negativas e as entradas zero serão mapeadas próximas a zero no gráfico
def tanh(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

# mais usada atualmente, principalmente em redes convolucionais e deep learning
# But the issue is that all the negative values become zero 
# immediately which decreases the ability of the model to fit or 
# train from the data properly. That means any negative input 
# given to the ReLU activation function turns the value into zero 
# immediately in the graph
def relu(soma):
    if soma >= 0:
        return soma
    return 0

# somente passa o valor, para regressão. Não tem um range de valores
def linear(soma):
    return soma

# problemas multiclasse
def softmax(x):
    ex = np.exp(x)
    return ex / ex.sum()

valores = [5.0, 2.0, 1.3]
print(softmax(valores))


