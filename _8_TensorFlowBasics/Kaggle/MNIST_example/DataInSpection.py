import tensorflow as tf
import pandas as pd



train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print(train.head())
print()
print(train.describe())
