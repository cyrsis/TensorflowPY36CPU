# ========================================================================= #
#                              Working with Matrix                                      #
# :                                                     #
# ========================================================================= #


import tensorflow as tf
import numpy as np

from tensorflow.python.framework import ops

ops.reset_default_graph()

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()

identity_matrix = tf.diag([1.0, 1.0, 1.0])
print(sess.run(identity_matrix))
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

print("#2X3 Random Norm martix")
TwotimeThreeMartix = tf.truncated_normal([2, 3])
print(sess.run(TwotimeThreeMartix))

print("#2x3 Constant Martix")
TwotimeThreeConstantMartic = tf.fill([2, 3], 5.0) #5.0 is different than 5
print(sess.run(TwotimeThreeConstantMartic))

print("#3x2 Uniform Martix")
ThreeTimeTwoUniformMatrix = tf.random_uniform([3, 2])
print(sess.run(ThreeTimeTwoUniformMatrix))

print("# Convert to tensor")
ConvertToTensor = tf.convert_to_tensor(np.array([[1., 2.0, 3.0], [-3.0, -7.0, -1.], [0., 5.0, -2.]]))
print(sess.run(ConvertToTensor))

print("##Matric  Add Operation")
print(sess.run(TwotimeThreeMartix+TwotimeThreeConstantMartic))

print("##matrix Sub Operation")
print(sess.run(TwotimeThreeMartix-TwotimeThreeConstantMartic))

print("##Matrix Multiplication")
print(sess.run(tf.matmul(TwotimeThreeConstantMartic,identity_matrix)))

print("##martix Transpose")
print(sess.run(tf.transpose(TwotimeThreeConstantMartic)))

print("##Matrix Determinant")
print(sess.run(tf.matrix_determinant(ConvertToTensor)))

print("##Martic Inverse")
print(sess.run(tf.matrix_inverse(ConvertToTensor)))

print("## Cholesky Decomposition")
print(sess.run(tf.cholesky(identity_matrix)))

eigenvalue,eigenvectors=sess.run(tf.self_adjoint_eig(identity_matrix))
print("Value is",eigenvalue)
print("Vector is ",eigenvectors)
