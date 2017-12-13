# ========================================================================= #
#                              Regression propagration                                      #
# :                                                     #
# ========================================================================= #
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.framework import ops

ops.reset_default_graph()

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()

# A regression example with punch of numbers

# Creating the target and placeholders
x_vals = np.random.normal(1, 0.1, 100)
y_vals = np.repeat(10., 100)
x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)

# Create variable (one model parameter =A)
A = tf.Variable(tf.random_normal(shape=[1]))

# Add model operation to the graph
my_output = tf.multiply(x_data, A)

# Specifiy the losee function, this allow how to change the model variagbles, we use L2 in here

loss = tf.square(my_output - y_target)

# init variable
sess.run(tf.global_variables_initializer())

# Optimizer, minize of the lose with learning Rate is 0.02
my_opt = tf.train.GradientDescentOptimizer(0.02)
train_step = my_opt.minimize(loss)

# Do the Regression Graph
for i in range(1000):
    rand_index = np.random.choice(100)
    rand_x = [x_vals[rand_index]]
    rand_y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    if (i + 1) % 25 == 0:
        print("Steps #" + str(i + 1))
        print(' A = ' + str(sess.run(A)))
        print("Loss =" + str(sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})))
