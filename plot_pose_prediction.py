import os
import numpy as np
import math
import sys
import h5py
from matplotlib import pyplot
import matplotlib.patches as patches

height = 256

def plot_sample(x, y, axis):
    img = x.reshape(height, height)
    axis.imshow(img, cmap='gray')
    rect = patches.Rectangle((y[0], y[1]),
                             1,
                             1,
                             linewidth=1, edgecolor='#32cd32', facecolor='none')
    rect1 = patches.Rectangle((y[2], y[3]),
                             1,
                             1,
                             linewidth=1, edgecolor='#32cd32', facecolor='none')
    axis.add_patch(rect)
    axis.add_patch(rect1)

t = 'test'
f = h5py.File(t + '_data.h5','r')
X = f['data'][:]
y_pred = np.load('result_both.npy')


fig = pyplot.figure(figsize=(6, 6))
fig.subplots_adjust(
    left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

for i in xrange(70,86,1):
    ax = fig.add_subplot(4, 4, i - 70 + 1, xticks=[], yticks=[])
    plot_sample(X[i], y_pred[i], ax)
pyplot.show()
