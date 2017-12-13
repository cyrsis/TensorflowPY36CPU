# This is my very first lessons for my
# April 30, 2017 10:26 am
# Start working on the basic
# Python learning,





import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf   # This is needed to work with tensorflow


# You can create constants in TF to
# hold specific values
a = tf.constant(1)
b = tf.constant(2)


# Of course you can add, multiply,
# and compute on these as you like
c = a + b
d = a * b

# TF numbers are stored in "tensors",
# a fancy term for multidimensional arrays
# If you pass TF a Python list, it can convert it
V1 = tf.constant([1., 2.])   # Vector, 1-dimensional , the '.' to make sure save it as decimal place
V2 = tf.constant([3., 4.])   # Vector, 1-dimensional
M = tf.constant([[1., 2.]])             # Matrix, 2d
N = tf.constant([[1., 2.],[3.,4.]])     # Matrix, 2d
K = tf.constant([[[1., 2.],[3.,4.]]])   # Tensor, 3d+ , this is the true tensor, contain 3

# You can also compute on tensors
# like you did scalars, but be careful of shape
V3 = V1 + V2

# Operations are element-wise by default
M2 = M * M

# True matrix multiplication requires a special call
NN = tf.matmul(N,N)

# The above code only defines a TF "graph".
# Nothing has been computed yet
# For that, you first need to create a TF "session"
sess = tf.Session()
# Note the parallelism information TF
# reports to you when starting a session

# Now you can run specific nodes of your graph,
# i.e. the variables you've named
output = sess.run(NN)
print("NN is:")
print(output)

# Remember to close your session
# when you're done using it
sess.close()

#---------------

# Often, we work interactively,
# it's convenient to use a simplified session
sess = tf.InteractiveSession()

# Now we can compute any node
print("M2 is:")
print(M2.eval())

# TF "variables" can change value,
# useful for updating model weights
W = tf.Variable(0, name="weight")

# But variables must be initialized by TF before use
init_op = tf.global_variables_initializer()
sess.run(init_op)


print("W Should be #0 and now  is:")
print(W.eval())

W += a
print("W after adding a:")
print(W.eval())

W += a
print("W after adding a again:")
print(W.eval())

# You can return or supply arbitrary nodes,
# i.e. check an intermediate value or
# sub your value in the middle of a computation

# Define a function in here at first
E = d + b # 1*2 + 2 = 4

print("E as defined in the beginning:")
print(E.eval())

# Let's see what d was at the same time
print("E was 4 and d is :")
print(sess.run([E,d]))

# Use a custom d by specifying a dictionary
print("Just for the debugging, add E with custom d=4:")
print(sess.run(E, feed_dict = {d:4.}))

