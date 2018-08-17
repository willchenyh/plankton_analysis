import urllib2
from scipy.misc import imread
from PIL import Image
from skimage import color
import pandas
import numpy as np
from sklearn.neural_network import MLPRegressor

image_url = pandas.read_csv('class01_00_tail.csv', sep=',', usecols=(28,))
Xtrain = []
Ytrain = []

for i in xrange(0,100):

  url = "https://s3-us-west-1.amazonaws.com/planktonsummer17/ZP100/" + image_url['Input.image_url'].loc[5*i]

  file1 = urllib2.urlopen(url)
  img = imread(file1, mode='RGB')
  img = color.colorconv.rgb2grey(img)
  img = img.reshape(65536, 1)
  Xtrain.append(img)

Xtrain = np.array(Xtrain)
np.save('Xtrain',Xtrain)
yleft = np.load('head_left.npy')
ytop = np.load('head_top.npy')
Ytrain.append(yleft)
Ytrain.append(ytop)
Ytrain = np.array(Ytrain)
Ytrain = np.reshape(Ytrain, (100, 2))
np.save('Ytrain',Ytrain)

#mlp = MLPRegressor(solver='adam', hidden_layer_sizes=50,
                           #max_iter=150, shuffle=True, random_state=1,
                           #activation='relu')
#mlp.fit(Xtrain, Ytrain)
