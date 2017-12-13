import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#   import TensorFlow
import tensorflow as tf

sess = tf.Session()

# Verify we can print a string
hello = tf.constant("Hello Victor from TensorFlow")
print(sess.run(hello))

#   Perform some simple math
a = tf.constant(20)
b = tf.constant(22)
c = tf.constant(35)

print('a + b + c = {0}'.format(sess.run(a + b+ c)))


print(dir(tf));
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
