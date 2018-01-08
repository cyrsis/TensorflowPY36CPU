# victor
# 25/12/2017
# Created @ 2017-12-25 23:53

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

np.random.seed(2)

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools

from keras.utils.np_utils import to_categorical  # convert to one-hot-encoding
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau

from tensorflow.python.framework import ops

ops.reset_default_graph()

sns.set(style='white', context='notebook', palette='deep')

train = pd.read_csv('./data/train.csv')

test = pd.read_csv('./data/test.csv')

print(pd.head())
Y_train = train['label']
