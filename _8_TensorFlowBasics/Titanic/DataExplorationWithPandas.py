import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from tensorflow.python.framework import ops

ops.reset_default_graph()

df = pd.read_csv('./train.csv')

# print(df.head())
# print(df.info())
# print(df.describe())

# Pandas allow us index of the array
# print(df.iloc[3]) #int of location
# print(df.loc[0:5,'Ticket'])

# print(df['Ticket'].head())
# print(df[['Embarked','Ticket']].head()) #List of colume name


# print(df[df['Age'] > 70]) #Select the passage

# print(df['Age']>70)
# print(df[(df['Age'] == 11) & (df['SibSp'] == 5)])

# print(df[(df.Age==11)| (df.SibSp ==5)])


#print(df.query('(Age ==11) | (SibSp ==5)'))

#Find unique Values

# print(df['Embarked'].unique())

#Sorting
#print(df.sort_values('Age',ascending=False).head())



# victorxx
# 20/12/2017
# Created @ 2017-12-20 22:00
