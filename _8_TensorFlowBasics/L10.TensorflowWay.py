import tensorflow as tf
import numpy as np

sess = tf.Session()

x_values = np.array([1.,3.,5.,6.,8.])

x_data = tf.placeholder(tf.float32)

constance = tf.constant(10.0)

product = tf.multiply(x_data,constance)

for x_value in x_values:
    print(sess.run(product,{x_data: x_value}))

merged = tf.summary.merge_all(key = 'summaries')
my_writer=tf.summary.FileWriter('tensorboard/logs',sess.graph)


