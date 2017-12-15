import os
import struct
import numpy as np
import matplotlib.pyplot as ply
from scipy.special import expit
import sys
import cv2
import csv




#victor
#14/12/2017 
#Created @ 2017-12-14 23:23

def loadTrainData():
    l =[]
    with open('train.csv') as file:
        lines = csv.read(file)
        for line in lines:
            l.append(line)

    l.remove([0])
    l = np.array(l)
    label = l[:0]
    data = l[:,1:]
    return toInt()

