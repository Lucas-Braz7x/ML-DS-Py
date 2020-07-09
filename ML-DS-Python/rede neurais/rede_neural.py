#Redes neurais com pybrain

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

#Dimensões dos valores de entrada e do objetivo 
dataset = SupervisedDataSet(2, 1)

dataset.addSample([1,1], [0])
dataset.addSample([1,0], [1])
dataset.addSample([0,1], [1])
dataset.addSample([0,0], [0])

#Passando o numero de entradas, quantos neuronios, numero de saidas
network = buildNetwork(dataset.indim, 4, dataset.outdim, bias=True) #Uma camada com quatro neuronios

#pré-Treino
#Passando a rede, o conjunto de dados, a taxa de aprendizado
trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.99)

#treino
for epoch in range(1000):
    trainer.train()
    # trainer.trainEpochs(1000) Forma alternativa#

#Teste

test_data = SupervisedDataSet(2, 1)
test_data.addSample([1,1], [0])
test_data.addSample([1,0], [1])
test_data.addSample([0,1], [1])
test_data.addSample([0,0], [0])

trainer.testOnData(test_data, verbose=True)


