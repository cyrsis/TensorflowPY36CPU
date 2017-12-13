import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Get the graph handle
sess = tf.Session()

my_tensor = tf.zeros([1, 20])#1D, 20 of 0s
print(sess.run(my_tensor))
#array


print("Is this 2D tensor?")
my_tensor2 = tf.zeros([2,20])
print(sess.run(my_tensor2))

print("Is this 3D tensor?")
my_tensor3 = tf.zeros([3,20])
print(sess.run(my_tensor3))

# Declear a variables
my_var = tf.Variable(tf.zeros([1, 20]))
sess.run(my_var.initializer)  # have to run init before it can a
print(sess.run(my_var))

# Different  kind of variables
row_dim = 2
col_dim = 2

# Zero init variable
zero_var = tf.Variable(tf.zeros([row_dim, col_dim]))

# One init variable
one_var = tf.Variable(tf.ones([row_dim, col_dim]))

print("##Test 2D array with zero_var and one_var ")
# Shaped like other variable
sess.run(zero_var.initializer)
sess.run(one_var.initializer)
print(sess.run(zero_var))
print(sess.run(one_var))

print("##If shape are dependence on othter shape, use build -in fucntion ones_like() or zeros_like()")
zero_similiar = tf.Variable(tf.zeros_like(zero_var))
one_similiar = tf.Variable(tf.ones_like(one_var))

print("#Fill shape with a constant , constant is -1")
fill_var = tf.Variable(tf.fill([row_dim, col_dim], -1))
sess.run(fill_var.initializer)
print(sess.run(fill_var))

print("#Create a variable from a constant")
const_var = tf.Variable(tf.constant([8, 6, 7, 5, 3, 0, 9]))
sess.run(const_var.initializer)
print(sess.run(const_var))

const_fill_var = tf.Variable(tf.constant(-1, shape=[row_dim, col_dim]))

print("#Sequence generateion, very similar with numpy")
linear_var = tf.Variable(tf.linspace(start=0.0, stop=1.0, num=3))  # Generates [0.0,0.5,1.0] includes the end
sess.run(linear_var.initializer)
print(sess.run(linear_var))

sequence_withoutEnd = tf.Variable(tf.range(start=0.0, limit=1.0, delta=0.3))  # Generate [0.3,0.6,0.9]
sess.run(sequence_withoutEnd.initializer)
print(sess.run(sequence_withoutEnd))

print("#Random number")
rnormal_var = tf.random_normal([row_dim, col_dim], mean=0.0, stddev=1.0)
print(sess.run(rnormal_var))

runif_var = tf.random_uniform([row_dim, col_dim], minval=0, maxval=4)
print(sess.run(runif_var))

print("###Create tensorbaord and see it yourself")
# add summaired to tensorboard
from tensorflow.python.framework import ops

ops.reset_default_graph()

sess2 = tf.Session()

# Create tensor
my_var = tf.Variable(tf.zeros([1, 20]))



megered = tf.summary.merge_all()

# init Grap write

writer = tf.summary.FileWriter("./tmp/variable_logs", graph=sess2.graph)




##tensorboard --logdir=/tmp


