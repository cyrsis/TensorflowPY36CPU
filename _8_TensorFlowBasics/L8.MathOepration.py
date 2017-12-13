import tensorflow as tf
import numpy as np

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()
print(sess.run(tf.div(3, 4)))
print(sess.run(tf.truediv(3, 4)))
print(sess.run(tf.floordiv(3.0, 4.0)))

print("Mode function")
print(sess.run(tf.mod(22.0, 5.0)))

print("Cross product")
print(sess.run(tf.cross([1.0, 0.0, 0.], [0., 1.0, 0.])))

print("Trig function Sin, Cos, Tan")
print(sess.run(tf.sin(3.1416)))
print(sess.run(tf.cos(3.1416)))
print(sess.run(tf.div(tf.sin(3.1416 / 4.0), tf.cos(3.1416 / 4.))))

print("#Customer operations")
def custom_ploynomial(x_value):
    #return 3x^2-x+10
    return(tf.subtract(3*tf.square(x_value),x_value)+10)
print(sess.run(custom_ploynomial(11)))

test_nums = range(15)
expected_output = [3*x*x-x+10 for x in test_nums] #light comprehension
print(expected_output[11])

print("use Tensorflow in for loop")
for num in test_nums:
    print(sess.run(custom_ploynomial(num)))
