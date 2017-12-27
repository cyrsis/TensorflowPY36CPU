# victor
# 23/12/2017
# Created @ 2017-12-23 18:36

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from tensorflow.python.framework import ops

ops.reset_default_graph()


sess = tf.Session()

mnist = input_data("/temp/MNIST/", one_hot=True)

print(mnist.shape)
