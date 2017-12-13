# -*- coding: utf-8 -*-
# __author__ = 'Victor Tong'
# --github-- = 'cyrsis

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops

sess = tf.Session()

scalar = tf.constant(100)
vector = tf.constant([1,2,3,4,5]) #(5,)
matrix = tf.constant([[1,2,3],[4,5,6]]) #(2,3)
cube_matrix = tf.constant([[[1,2,3],[4,5,6],[7,8,9]]])

print(scalar.get_shape()) #()
print(vector.get_shape()) #(5,)
print(matrix.get_shape()) #(2,3)
print(cube_matrix.get_shape()) #(1, 3, 3)


