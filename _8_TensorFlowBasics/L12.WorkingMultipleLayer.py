import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.python.framework import ops

ops.reset_default_graph()


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_shape = [1, 4, 4, 1]
x_val = np.random.uniform(size=x_shape)
x_data = tf.placeholder(tf.float32, shape=x_shape)

my_filter = tf.constant(0.25, shape=[2, 2, 1, 1])
my_stride = [1, 2, 2, 1]
mov_avg_layer = tf.nn.conv2d(x_data, my_filter, my_stride, padding='SAME', name='Moving_Avg_Window')


def custom_layer(input_matrix):
    input_matrix_sqeezed = tf.squeeze(input_matrix)
    A = tf.constant([[1., 2.], [-1., 3.]])
    b = tf.constant(1., shape=[2, 2])
    temp1 = tf.matmul(A, input_matrix_sqeezed)
    temp = tf.add(temp1, b)
    return (tf.sigmoid(temp))


with tf.name_scope('Custom_Layer') as scope:
    custom_layer1 = custom_layer(mov_avg_layer)

sess = tf.Session()

print(sess.run(custom_layer1, feed_dict={x_data: x_val}))

merged = tf.summary.merge_all(key='summaries')

my_writ =tf.summary.FileWriter('tensorboard_logs/',sess.graph)
