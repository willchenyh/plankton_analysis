import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
import requests
from io import BytesIO
from PIL import Image
import csv
import pandas
from sklearn.cluster import KMeans



image_url = pandas.read_csv('class01_05_tail.csv', sep=',', usecols=(28,))
location = pandas.read_csv('class01_05_tail.csv', sep=',', usecols=(29,))
label = pandas.read_csv('class01_05_tail.csv', sep=',', usecols=(30,))

location = location['Answer.annotation_data'].str.split(',', expand=True)

location['left'] = location[0].map(lambda x: x.lstrip('[{"left":'))
location['top'] = location[1].map(lambda x: x.lstrip('"top":'))
location['width'] = location[2].map(lambda x: x.lstrip('"width":'))
location['height'] = location[3].map(lambda x: x.lstrip('"height":'))
#process the top location data
top_location = location.loc[:, 'top']
numpy_t = top_location.as_matrix()
numpy_t.resize((100, 5))
top_location = pandas.DataFrame(numpy_t).astype(float)
result = top_location.mean(axis = 1)

mean_top = top_location.copy()
for x in range(0,5):
  mean_top.loc[:,x] = mean_top.loc[:,x] - result
mean_top = mean_top.abs()
result = mean_top.idxmax(axis=1)

# result contains the index of outliner
#print(result)
Numtop = top_location.as_matrix()
Indextop = result.as_matrix()
temp = np.zeros(shape=(100,4))

for i in range(0,100):
    m = 0
    j = 0
    while j < 5:
        if m == 4:
            break
        if j == Indextop[i]:
            j += 1
            continue
        elif j != Indextop[i]:
             temp[i][m] = Numtop[i][j]
             m += 1
             j += 1
#print(Numtop)
temp = pandas.DataFrame(temp).astype(float)
result1 = temp.mean(axis = 1)

mean_top1 = temp.copy()
for x in range(0,4):
  mean_top1.loc[:,x] = mean_top1.loc[:,x] - result1
mean_top1 = mean_top1.abs()
result1 = mean_top1.idxmax(axis=1)

# result contains the index of outliner
#print(result)
Numtop1 = temp.as_matrix()
Indextop1 = result1.as_matrix()
temp1 = np.zeros(shape=(100,3))
#print(Indextop1)
for i in range(0,100):
    m = 0
    j = 0
    while j < 4:
        if m == 3:
            break
        if j == Indextop1[i]:
            j += 1
            continue
        elif j != Indextop1[i]:
             temp1[i][m] = Numtop1[i][j]
             m += 1
             j += 1



final_top = temp1.copy()
#print(final_top)
# end of the top location process
# start of the left location process

left_location = location.loc[:, 'left']
numpy_t = left_location.as_matrix()
numpy_t.resize((100, 5))
left_location = pandas.DataFrame(numpy_t).astype(float)
result = left_location.mean(axis = 1)

mean_left = left_location.copy()
for x in range(0,5):
  mean_left.loc[:,x] = mean_left.loc[:,x] - result
mean_left = mean_left.abs()
result = mean_left.idxmax(axis=1)

# result contains the index of outliner
#print(result)
Numleft = left_location.as_matrix()
Indexleft = result.as_matrix()
temp = np.zeros(shape=(100,4))

for i in range(0,100):
    m = 0
    j = 0
    while j < 5:
        if m == 4:
            break
        if j == Indexleft[i]:
            j += 1
            continue
        elif j != Indexleft[i]:
             temp[i][m] = Numleft[i][j]
             m += 1
             j += 1
#print(Numtop)
#print(temp)
temp = pandas.DataFrame(temp).astype(float)
result1 = temp.mean(axis = 1)

mean_left1 = temp.copy()
for x in range(0,4):
  mean_left1.loc[:,x] = mean_left1.loc[:,x] - result1
mean_left1 = mean_left1.abs()
result1 = mean_left1.idxmax(axis=1)

# result contains the index of outliner
#print(result)
Numleft1 = temp.as_matrix()
Indexleft1 = result1.as_matrix()
temp1 = np.zeros(shape=(100,3))
for i in range(0,100):
    m = 0
    j = 0
    while j < 4:
        if m == 3:
            break
        if j == Indexleft1[i]:
            j += 1
            continue
        elif j != Indexleft1[i]:
             temp1[i][m] = Numleft1[i][j]
             m += 1
             j += 1

#print(temp1)
final_left = temp1.copy()
final_top_mean = final_top.mean(axis=1).astype(int)
final_left_mean = final_left.mean(axis=1).astype(int)


image_url = pandas.read_csv('class01_subclass05.csv', sep=',', usecols=(28,))
location = pandas.read_csv('class01_subclass05.csv', sep=',', usecols=(29,))
label = pandas.read_csv('class01_subclass05.csv', sep=',', usecols=(30,))

location = location['Answer.annotation_data'].str.split(',', expand=True)

location['left'] = location[0].map(lambda x: x.lstrip('[{"left":'))
location['top'] = location[1].map(lambda x: x.lstrip('"top":'))
location['width'] = location[2].map(lambda x: x.lstrip('"width":'))
location['height'] = location[3].map(lambda x: x.lstrip('"height":'))
#process the top location data
top_location = location.loc[:, 'top']
numpy_t = top_location.as_matrix()
numpy_t.resize((100, 5))
top_location = pandas.DataFrame(numpy_t).astype(float)
result = top_location.mean(axis = 1)

mean_top = top_location.copy()
for x in range(0,5):
  mean_top.loc[:,x] = mean_top.loc[:,x] - result
mean_top = mean_top.abs()
result = mean_top.idxmax(axis=1)

# result contains the index of outliner
#print(result)
Numtop = top_location.as_matrix()
Indextop = result.as_matrix()
temp = np.zeros(shape=(100,4))

for i in range(0,100):
    m = 0
    j = 0
    while j < 5:
        if m == 4:
            break
        if j == Indextop[i]:
            j += 1
            continue
        elif j != Indextop[i]:
             temp[i][m] = Numtop[i][j]
             m += 1
             j += 1
#print(Numtop)
temp = pandas.DataFrame(temp).astype(float)
result1 = temp.mean(axis = 1)

mean_top1 = temp.copy()
for x in range(0,4):
  mean_top1.loc[:,x] = mean_top1.loc[:,x] - result1
mean_top1 = mean_top1.abs()
result1 = mean_top1.idxmax(axis=1)

# result contains the index of outliner
#print(result)
Numtop1 = temp.as_matrix()
Indextop1 = result1.as_matrix()
temp1 = np.zeros(shape=(100,3))
#print(Indextop1)
for i in range(0,100):
    m = 0
    j = 0
    while j < 4:
        if m == 3:
            break
        if j == Indextop1[i]:
            j += 1
            continue
        elif j != Indextop1[i]:
             temp1[i][m] = Numtop1[i][j]
             m += 1
             j += 1



final_top = temp1.copy()
#print(final_top)
# end of the top location process
# start of the left location process

left_location = location.loc[:, 'left']
numpy_t = left_location.as_matrix()
numpy_t.resize((100, 5))
left_location = pandas.DataFrame(numpy_t).astype(float)
result = left_location.mean(axis = 1)

mean_left = left_location.copy()
for x in range(0,5):
  mean_left.loc[:,x] = mean_left.loc[:,x] - result
mean_left = mean_left.abs()
result = mean_left.idxmax(axis=1)

# result contains the index of outliner
#print(result)
Numleft = left_location.as_matrix()
Indexleft = result.as_matrix()
temp = np.zeros(shape=(100,4))

for i in range(0,100):
    m = 0
    j = 0
    while j < 5:
        if m == 4:
            break
        if j == Indexleft[i]:
            j += 1
            continue
        elif j != Indexleft[i]:
             temp[i][m] = Numleft[i][j]
             m += 1
             j += 1
#print(Numtop)
#print(temp)
temp = pandas.DataFrame(temp).astype(float)
result1 = temp.mean(axis = 1)

mean_left1 = temp.copy()
for x in range(0,4):
  mean_left1.loc[:,x] = mean_left1.loc[:,x] - result1
mean_left1 = mean_left1.abs()
result1 = mean_left1.idxmax(axis=1)

# result contains the index of outliner
#print(result)
Numleft1 = temp.as_matrix()
Indexleft1 = result1.as_matrix()
temp1 = np.zeros(shape=(100,3))
for i in range(0,100):
    m = 0
    j = 0
    while j < 4:
        if m == 3:
            break
        if j == Indexleft1[i]:
            j += 1
            continue
        elif j != Indexleft1[i]:
             temp1[i][m] = Numleft1[i][j]
             m += 1
             j += 1

#print(temp1)
final_left = temp1.copy()
final_top_mean1 = final_top.mean(axis=1).astype(int)
final_left_mean1= final_left.mean(axis=1).astype(int)

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 255), ylim=(0, 255))


for i in range(0, 100):
    ax.annotate('', xy=(128 + final_left_mean1[i] - final_left_mean[i], 128 + final_top_mean[i] - final_top_mean1[i]),
                xytext=(128, 128),
                arrowprops=dict(arrowstyle="->", color='r', lw=1))
fig.savefig('PoseVariance')


