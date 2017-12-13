# ========================================================================= #
#          Trying out for different layer work together                                      #
# :      https://github.com/nfmcclure/tensorflow_cookbook/blob/c1fa5051c860ecb6de875db975465ced06f43ba6/06_Neural_Networks/05_Implementing_Different_Layers/05_implementing_different_layers.ipynb                                               #
# ========================================================================= #
import tensorflow as tf
import matplotlib.pyplot as plt
import csv
import os
import random
import numpy as np
from tensorflow.python.framework import ops

ops.reset_default_graph()

sess = tf.Session()

# pararmeters for the run
data_size = 25
conv_size = 5
maxpool_size = 5
stride_size = 1

# ensure reprodicibility
seed = 13
np.random.seed(seed)
tf.set_random_seed(seed)

# Generate 1 D data
data_1d = np.random.normal(size=data_size)
# print(data_1d)
input_2d = tf.expand_dims(data_1d, 0)
# print(sess.run(input_2d))
input_3d = tf.expand_dims(input_2d, 0)
# print(sess.run(input_3d))
input_4d = tf.expand_dims(input_3d, 3)
# print(sess.run(input_4d))


# Placeholder
x_input_1d = tf.placeholder(dtype=tf.float32, shape=[data_size])


# CNN
def conv_layer_1d(input_1d, my_filter, stride):
    # TensdoeFlow's 'conv2d()' fucntion only work with 4D arrays:
    # [batch#, width,height, channels] , we have 1 batch and width of 1
    # width - 1, but height -the length of the input, and 1 channel
    # So next we create the 4D array by inserting dimension 1's

    input_2d = tf.expand_dims(input_1d, 0)
    # print(sess.run(input_2d))
    input_3d = tf.expand_dims(input_2d, 0)
    # print(sess.run(input_3d))
    input_4d = tf.expand_dims(input_3d, 3)
    # print(sess.run(input_4d))

    # To increase stride [1,1,2,1]
    convolution_output = tf.nn.conv2d(input_4d, filter=my_filter, strides=[1, 1, stride, 1], padding="VALID")

    # Get away of extra dimension
    conv_out_put_1d = tf.squeeze(convolution_output)
    return (conv_out_put_1d)


# Create filter for convolution
my_filter = tf.Variable(tf.random_normal(shape=[1, conv_size, 1, 1]))

my_convolution_output = conv_layer_1d(x_input_1d, my_filter, stride=stride_size)


# ----Activation----------

def activation(input_1d):
    return (tf.nn.relu(input_1d))


my_activation_output = activation(my_convolution_output)


# -----Max pool-------
def max_pool(input_1d, width, stride):
    # Max Pool only work with 4D
    input_2d = tf.expand_dims(input_1d, 0)
    input_3d = tf.expand_dims(input_2d, 0)
    input_4d = tf.expand_dims(input_3d, 3)

    pool_output = tf.nn.max_pool(input_4d, ksize=[1, 1, width, 1], strides=[1, 1, stride, 1], padding='VALID')

    pool_output_1d = tf.squeeze(pool_output)

    return (pool_output_1d)


my_maxpool_out = max_pool(my_activation_output, width=maxpool_size, stride=stride_size)


# -----Full connected-----
def fully_connected(input_layer, num_outputs):
    # figure out the shape of the weight martix
    # the dimension will be (length of the input) by (num_outputs)
    weight_shape = tf.squeeze(tf.stack([tf.shape(input_layer), [num_outputs]]))
    weight = tf.random_normal(weight_shape, stddev=0.1)  # init the weight

    bias = tf.random_normal(shape=[num_outputs])

    input_layer_2d = tf.expand_dims(input_layer, 0)  # 2D for multiplication

    full_output = tf.add(tf.matmul(input_layer_2d, weight), bias)

    return (tf.squeeze(full_output))


my_full_output = fully_connected(my_maxpool_out, 5)

# run graphic
sess.run(tf.global_variables_initializer())

feed_dict = {x_input_1d: data_1d}

print(">>>>>>>>>>>>>>1D Data<<<<<<<<<<<<")

# CNN
print("#######CNN")
print("Input = array of length %d" % (x_input_1d.shape.as_list()[0]))
print("CNN w/Filter , length = %d, stride size =%d, result in array of length %d:" % (conv_size , stride_size,my_convolution_output.shape.as_list()[0]))

print(sess.run(my_convolution_output, feed_dict=feed_dict))


#Activation Output
print("########Relu")
print("Input = above array of length %d" % (my_convolution_output.shape.as_list()[0]))
print("Relu element wise return as array of length %d" % (my_activation_output.shape.as_list()[0]))
print(sess.run(my_activation_output,feed_dict=feed_dict))

#Maxppol Output
print("########Max Pool")
print("Input = above array of lenth %d" % (my_activation_output.shape.as_list()[0]))
print("Max Pool , windows lenth =%d, stride size =%d , result in the array of length %d " %(maxpool_size,stride_size,my_maxpool_out.shape.as_list()[0]))
print(sess.run(my_maxpool_out,feed_dict=feed_dict))


#Making some mirror changes


