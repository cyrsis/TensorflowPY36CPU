import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

np.random.seed(2)

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools

from keras.utils.np_utils import to_categorical # convert to one-hot-encoding
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau


sns.set(style='white', context='notebook', palette='deep')

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


Y_train = train["label"]

X_train = train.drop(labels="label",axis=1)

g = sns.countplot(Y_train)

print(Y_train.value_counts())

#Check the X value is null

X_train.isnull().any().describe()


