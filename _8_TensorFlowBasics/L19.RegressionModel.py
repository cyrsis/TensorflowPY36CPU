# ========================================================================= #
#                              L10.Regression model                                      #
# The regression will generate 1-00 random samples, Normal(mean=1,std=0.1)
# #
# ========================================================================= #
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.framework import ops

ops.reset_default_graph()

sess = tf.Session()

batch_size = 25

# data
x_vals = np.random.normal(1, 0.1, 100)  # mean =1 , std 0.1 ,100 samples
y_vals = np.repeat(10., 100)  # all 10 x 100
x_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# Splite Data into train/test = 80%/20%

train_indices = np.random.choice(len(x_vals), round(len(x_vals) * 0.8), replace=False)
test_indices = np.array(list(set(range(len(x_vals))) - set(train_indices)))

x_vals_train = x_vals[train_indices]
x_vals_test = x_vals[test_indices]
y_vals_train = y_vals[train_indices]
y_vals_test = y_vals[test_indices]

# Model Variable and operation
A = tf.Variable(tf.random_normal(shape=[1, 1]))

my_output = tf.matmul(x_data, A)

# Loss
loss = tf.reduce_mean(tf.square(my_output - y_target))

# Create Optomizer
my_opt = tf.train.GradientDescentOptimizer(0.02)
train_steps = my_opt.minimize(loss)

sess.run(tf.global_variables_initializer())

# Training
for i in range(100):
    rand_index = np.random.choice(len(x_vals_train), size=batch_size)
    rand_x = np.transpose([x_vals_train[rand_index]])
    rand_y = np.transpose([y_vals_train[rand_index]])
    sess.run(train_steps, feed_dict={x_data: rand_x, y_target: rand_y})
    if (i + 1) % 25 == 0:
        print('Step #' + str(i + 1) + ' A = ' + str(sess.run(A)))
        print('Loss' + str(sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})))

# Accuracy
mse_test = sess.run(loss, feed_dict={x_data: np.transpose([x_vals_test]), y_target: np.transpose([y_vals_test])})
mse_train = sess.run(loss, feed_dict={x_data: np.transpose([x_vals_train]), y_target: np.transpose([y_vals_train])})

print("MSe on test: " + str(np.round(mse_test,2)))
print("MSe on train: " + str(np.round(mse_train,2)))
