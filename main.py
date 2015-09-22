#!/usr/bin/python

from class_vis import Picture, output_image
from Classifyrf import classify

import numpy as np
import pylab as pl


file1_size=2488
file2_size=2164
file3_size=2388
cnt=0

data = []
label= []
data_test = []
label_test = []
for line in open('class1.txt'):
  i,j = [float(x) for x in line.strip().split(' ')]
  arr=[i,j]
  cnt+=1
  if cnt <= (file1_size*0.7) :
    data.append(arr)
    label.extend([0])
  else:
    data_test.append(arr)
    label_test.extend([0])


cnt=0

for line in open('class2.txt'):
  i,j = [float(x) for x in line.strip().split(' ')]
  arr=[i,j]
  cnt+=1
  if cnt <= (file2_size*0.7) :
    data.append(arr)
    label.extend([1])
  else:
    data_test.append(arr)
    label_test.extend([1])


cnt=0

for line in open('class3.txt'):
  i,j = [float(x) for x in line.strip().split(' ')]
  arr=[i,j]
  cnt+=1
  if cnt <= (file3_size*0.7) :
    data.append(arr)
    label.extend([2])
  else:
    data_test.append(arr)
    label_test.extend([2])

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them

clf= classify(data, label,data_test, label_test)
#print data


### draw the decision boundary with the text points overlaid
Picture(clf, data, label)
#output_image("test.png", "png", open("test.png", "rb").read())