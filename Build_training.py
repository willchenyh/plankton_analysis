import urllib2
from scipy.misc import imread
from PIL import Image
from skimage import color
import pandas
import numpy as np
from skimage.transform import resize
ytleft00 = np.load('tail_left00.npy')
ytleft00 = np.reshape(ytleft00, (100, 1))
ytleft03 = np.load('tail_left03.npy')
ytleft03 = np.reshape(ytleft03, (100, 1))
ytleft04 = np.load('tail_left04.npy')
ytleft04 = np.reshape(ytleft04, (100, 1))
ytleft05 = np.load('tail_left05.npy')
ytleft05 = np.reshape(ytleft05, (100, 1))
ytleft06 = np.load('tail_left06.npy')
ytleft06 = np.reshape(ytleft06, (100, 1))
ytleft07 = np.load('tail_left07.npy')
ytleft07 = np.reshape(ytleft07, (100, 1))
ytleft08 = np.load('tail_left08.npy')
ytleft08 = np.reshape(ytleft08, (100, 1))
ytleft09 = np.load('tail_left09.npy')
ytleft09 = np.reshape(ytleft09, (100, 1))
ytleft11 = np.load('tail_left11.npy')
ytleft11 = np.reshape(ytleft11, (100, 1))
ytleft12 = np.load('tail_left12.npy')
ytleft12 = np.reshape(ytleft12, (100, 1))
ytleft13 = np.load('tail_left13.npy')
ytleft13 = np.reshape(ytleft13, (100, 1))
ytleft14 = np.load('tail_left14.npy')
ytleft14 = np.reshape(ytleft14, (100, 1))
ytleft15 = np.load('tail_left15.npy')
ytleft15 = np.reshape(ytleft15, (100, 1))

Ytailtrain_left = np.concatenate((ytleft00,ytleft03,ytleft04,ytleft05,ytleft06,ytleft07,ytleft08,ytleft09,ytleft11,ytleft12,ytleft13,ytleft14,ytleft15), axis=0)

yttop00 = np.load('tail_top00.npy')
yttop00 = np.reshape(yttop00, (100, 1))
yttop03 = np.load('tail_top03.npy')
yttop03 = np.reshape(yttop03, (100, 1))
yttop04 = np.load('tail_top04.npy')
yttop04 = np.reshape(yttop04, (100, 1))
yttop05 = np.load('tail_top05.npy')
yttop05 = np.reshape(yttop05, (100, 1))
yttop06 = np.load('tail_top06.npy')
yttop06 = np.reshape(yttop06, (100, 1))
yttop07 = np.load('tail_top07.npy')
yttop07 = np.reshape(yttop07, (100, 1))
yttop08 = np.load('tail_top08.npy')
yttop08 = np.reshape(yttop08, (100, 1))
yttop09 = np.load('tail_top09.npy')
yttop09 = np.reshape(yttop09, (100, 1))
yttop11 = np.load('tail_top11.npy')
yttop11 = np.reshape(yttop11, (100, 1))
yttop12 = np.load('tail_top12.npy')
yttop12 = np.reshape(yttop12, (100, 1))
yttop13 = np.load('tail_top13.npy')
yttop13 = np.reshape(yttop13, (100, 1))
yttop14 = np.load('tail_top14.npy')
yttop14 = np.reshape(yttop14, (100, 1))
yttop15 = np.load('tail_top15.npy')
yttop15 = np.reshape(yttop15, (100, 1))

Ytailtrain_top = np.concatenate((yttop00,yttop03,yttop04,yttop05,yttop06,yttop07,yttop08,yttop09,yttop11,yttop12,yttop13,yttop14,yttop15), axis=0)

yleft00 = np.load('head_left00.npy')
yleft00 = np.reshape(yleft00, (100, 1))
yleft03 = np.load('head_left03.npy')
yleft03 = np.reshape(yleft03, (100, 1))
yleft04 = np.load('head_left04.npy')
yleft04 = np.reshape(yleft04, (100, 1))
yleft05 = np.load('head_left05.npy')
yleft05 = np.reshape(yleft05, (100, 1))
yleft06 = np.load('head_left06.npy')
yleft06 = np.reshape(yleft06, (100, 1))
yleft07 = np.load('head_left07.npy')
yleft07 = np.reshape(yleft07, (100, 1))
yleft08 = np.load('head_left08.npy')
yleft08 = np.reshape(yleft08, (100, 1))
yleft09 = np.load('head_left09.npy')
yleft09 = np.reshape(yleft09, (100, 1))
yleft11 = np.load('head_left11.npy')
yleft11 = np.reshape(yleft11, (100, 1))
yleft12 = np.load('head_left12.npy')
yleft12 = np.reshape(yleft12, (100, 1))
yleft13 = np.load('head_left13.npy')
yleft13 = np.reshape(yleft13, (100, 1))
yleft14 = np.load('head_left14.npy')
yleft14 = np.reshape(yleft14, (100, 1))
yleft15 = np.load('head_left15.npy')
yleft15 = np.reshape(yleft15, (100, 1))



Ytrain_left = np.concatenate((yleft00,yleft03,yleft04,yleft05,yleft06,yleft07,yleft08,yleft09,yleft11,yleft12,yleft13,yleft14,yleft15), axis=0)

ytop00 = np.load('head_top00.npy')
ytop00 = np.reshape(ytop00, (100, 1))
ytop03 = np.load('head_top03.npy')
ytop03 = np.reshape(ytop03, (100, 1))
ytop04 = np.load('head_top04.npy')
ytop04 = np.reshape(ytop04, (100, 1))
ytop05 = np.load('head_top05.npy')
ytop05 = np.reshape(ytop05, (100, 1))
ytop06 = np.load('head_top06.npy')
ytop06 = np.reshape(ytop06, (100, 1))
ytop07 = np.load('head_top07.npy')
ytop07 = np.reshape(ytop07, (100, 1))
ytop08 = np.load('head_top08.npy')
ytop08 = np.reshape(ytop08, (100, 1))
ytop09 = np.load('head_top09.npy')
ytop09 = np.reshape(ytop09, (100, 1))
ytop11 = np.load('head_top11.npy')
ytop11 = np.reshape(ytop11, (100, 1))
ytop12 = np.load('head_top12.npy')
ytop12 = np.reshape(ytop12, (100, 1))
ytop13 = np.load('head_top13.npy')
ytop13 = np.reshape(ytop13, (100, 1))
ytop14 = np.load('head_top14.npy')
ytop14 = np.reshape(ytop14, (100, 1))
ytop15 = np.load('head_top15.npy')
ytop15 = np.reshape(ytop15, (100, 1))
Ytrain_top = np.concatenate((ytop00,ytop03,ytop04,ytop05,ytop06,ytop07,ytop08,ytop09,ytop11,ytop12,ytop13,ytop14,ytop15), axis=0)

Ytrain = np.concatenate((Ytrain_left, Ytrain_top, Ytailtrain_left, Ytailtrain_top), axis=1)
Ytrain = Ytrain
np.save('Ytrain', Ytrain)


image_url = {}
image_url[1] = pandas.read_csv('class01_00_tail.csv', sep=',', usecols=(28,))
image_url[2] = pandas.read_csv('class01_03_tail.csv', sep=',', usecols=(28,))
image_url[3] = pandas.read_csv('class01_04_tail.csv', sep=',', usecols=(28,))
image_url[4] = pandas.read_csv('class01_05_tail.csv', sep=',', usecols=(28,))
image_url[5] = pandas.read_csv('class01_06_tail.csv', sep=',', usecols=(28,))
image_url[6] = pandas.read_csv('class01_07_tail.csv', sep=',', usecols=(28,))
image_url[7] = pandas.read_csv('class01_08_tail.csv', sep=',', usecols=(28,))
image_url[8] = pandas.read_csv('class01_09_tail.csv', sep=',', usecols=(28,))
image_url[9] = pandas.read_csv('class01_11_tail.csv', sep=',', usecols=(28,))
image_url[10] = pandas.read_csv('class01_12_tail.csv', sep=',', usecols=(28,))
image_url[11] = pandas.read_csv('class01_13_tail.csv', sep=',', usecols=(28,))
image_url[12] = pandas.read_csv('class01_14_tail.csv', sep=',', usecols=(28,))
image_url[13] = pandas.read_csv('class01_15_tail.csv', sep=',', usecols=(28,))



for j in xrange(1,14):
   for i in xrange(0,100):

      url = "https://s3-us-west-1.amazonaws.com/planktonsummer17/ZP100/" + image_url[1]['Input.image_url'].loc[5*i]

      file1 = urllib2.urlopen(url)
      img = imread(file1, mode='RGB')
      img = color.colorconv.rgb2grey(img)
      img = resize(img, (128, 128))
      img = img.reshape(1, 16384)
      print img[0][10000]
      if j == 1 and i == 0:
         Xtrain = img
      else:
         Xtrain = np.row_stack((Xtrain, img))

Xtrain = np.array(Xtrain)
np.save('Xtrain',Xtrain)


