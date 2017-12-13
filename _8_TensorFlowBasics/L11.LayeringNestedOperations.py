# https://github.com/nfmcclure/tensorflow_cookbook/blob/master/02_TensorFlow_Way/03_Working_with_Multiple_Layers/03_multiple_layers.ipynb

import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

ops.reset_default_graph()

sess = tf.Session()

my_array = np.array([[1., 3., 5., 7., 9.],
                     [-2., 0., 2., 4., 6.],
                     [-6., -3., 0.0, 3., 6]
                     ]
                    )
# Duplicate an array
x_values = np.array([my_array, my_array + 1])
print(x_values.shape)
print(x_values)

# Declear a placeholder
x_data = tf.placeholder(tf.float32,shape=[3,5])

# Declear constant
m1 = tf.constant([[1.],[0.],[-1.],[2.],[4]])
m2 = tf.constant([[2.]])
a1 = tf.constant([[10.]])

product = tf.matmul(x_data,m1)

product2 = tf.matmul(product,m2)

add1= tf.add(product2,a1)

for x_val in x_values:
    print(sess.run(add1,feed_dict={x_data:x_val}))

summary = tf.summary.merge_all(key='summaries')
my_write = tf.summary.FileWriter('tensorboard/',sess.graph)

