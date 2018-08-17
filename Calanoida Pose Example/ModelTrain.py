__author__      = "Xinxin Chen"

import pandas
import numpy as np
from sklearn.neural_network import MLPRegressor
np.set_printoptions(threshold=np.inf)


Xtrain = np.load('Xtrain.npy')
Ytrain = np.load('Ytrain.npy')
print Xtrain.size
print Ytrain
Xtrain = Xtrain.reshape(100, 65536)

mlp = MLPRegressor(solver='adam', hidden_layer_sizes=(1000, 1000),
                           max_iter=1000, shuffle=True, random_state=1,
                           activation='relu')
mlp.fit(Xtrain, Ytrain)
print mlp.predict(Xtrain[1].reshape(1,-1))