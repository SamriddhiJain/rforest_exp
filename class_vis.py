#!/usr/bin/python

#from udacityplots import *
import matplotlib 
matplotlib.use('agg')

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

#import numpy as np
#import matplotlib.pyplot as plt
#plt.ioff()

def Picture(clf, X_test, y_test):
    x_min = 200.0; x_max = 1000.0
    y_min = 600.0; y_max = 2500.0

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = 1  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)

    # Plot also the test points
    x1 = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==0]
    y1 = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==0]
    x2 = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==1]
    y2 = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==1]
    x3 = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==2]
    y3 = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==2]

    plt.scatter(x1, y1, color = "b", label="class1")
    plt.scatter(x2, y2, color = "r", label="class2")
    plt.scatter(x3, y3, color = "g", label="class3")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")

    plt.savefig("testrf.png")
    
import base64
import json
import subprocess

def output_image(name, format, bytes):
    image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)
    print image_start+json.dumps(data)+image_end
