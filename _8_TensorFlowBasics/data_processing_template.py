# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('./SampleData/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


# Splitting the dataset into
# a Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#take care the clean up for NaN
from sklearn.preprocessing import Imputer
inputer = Imputer(missing_values="NaN",strategy='mean',axis=0)
inputer = inputer.fit(X[:,1:3])
X[:,1:3] = inputer.transform(X[:,1:3])
print(X)





# Feature Scaling
# Standardizing & Normalizing Features
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""