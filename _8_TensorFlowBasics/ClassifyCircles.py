import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_circles


#Gene some data
x, y = make_circles(n_samples=1000,noise=0.1,factor=0.2,random_state=0)

print(x) #1000 samples
print(x.shape)  # (1000, 2)

plt.figure(figsize=(5,5))
plt.plot()

