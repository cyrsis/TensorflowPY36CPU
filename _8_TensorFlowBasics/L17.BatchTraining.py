# ========================================================================= #
#                        Stochastic vs Batch Training                       #
#             Batch Training have a few benefit , save some memory          #
#                                                                           #
#                                                                           #
# ========================================================================= #
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.python.framework import ops

ops.reset_default_graph()

sess = tf.Session()

#Stochastic Training

x_vals = np.random.normal(1,0.1,100) #mean =1, std =0.1
y_vals = np.repeat(10.,100) #targets

x_data = tf.placeholder(shape=[1],dtype=tf.float32)
y_target =tf.placeholder(shape=[1],dtype=tf.float32)

#model
A= tf.Variable(tf.random_normal(shape=[1]))

my_output = tf.multiply(x_data,A)

#loss Function - L2 loss , L1 is replace with tf.abs()
loss = tf.reduce_mean(tf.square(my_output-y_target)) #with batch config
#loss = tf.square(my_output-y_target)) #without batch

#optimizer
my_opt = tf.train.GradientDescentOptimizer(0.02)
train_step = my_opt.minimize(loss)

sess.run(tf.global_variables_initializer())

loss_stochastic = []
for i in range(100):

    rand_index = np.random.choice(100) #without batch size

    rand_x =[x_vals[rand_index]]
    rand_y =[y_vals[rand_index]]
    sess.run(train_step,feed_dict={x_data:rand_x,y_target:rand_y})
    if (i+1)%5 ==0:
        print("Steps # " + str(i+1) + 'A = ' +str (sess.run(A)))
        temp_loss = sess.run(loss,feed_dict={x_data:rand_x,y_target:rand_y})
        print('Loss = ' + str(temp_loss))
        loss_stochastic.append(temp_loss)

# ========================================================================= #
#                              Batch Training                               #
# :                                                                         #
# ========================================================================= #

batch_size = 25
# Batch Training is needed

x_vals = np.random.normal(1, 0.1, 100)
# x_vals = np.random.normal(1,0.1,100) #mean =1, std =0.1
y_vals = np.repeat(10., 100)  # targets

x_data = tf.placeholder(shape=[None,1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None,1], dtype=tf.float32)

# model
A = tf.Variable(tf.random_normal(shape=[1,1]))

#tf.matmul() require 2-D tensor
my_output = tf.matmul(x_data, A)

# loss Function - L2 loss , L1 is replace with tf.abs()
loss = tf.reduce_mean(tf.square(my_output - y_target))  # with batch config
# loss = tf.square(my_output-y_target)) #without batch

# optimizer
my_opt = tf.train.GradientDescentOptimizer(0.02)
train_step = my_opt.minimize(loss)

sess.run(tf.global_variables_initializer())

loss_batch= []
for i in range(100):
    rand_index = np.random.choice(100,size=batch_size)  # without batch size
    #rand_index = np.random.choice(100)  # without batch size
    rand_x = np.transpose([x_vals[rand_index]])
    #rand_x = [x_vals[rand_index]] #without batch size
    rand_y = np.transpose([y_vals[rand_index]])
    #rand_y = [y_vals[rand_index]] 3without batch size
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})

    if (i + 1) % 5 == 0:
        print("Steps # " + str(i + 1) + 'A = ' + str(sess.run(A)))
        temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
        print('Loss = ' + str(temp_loss))
        loss_batch.append(temp_loss)

plt.title("Loss Stochastic vs Loss Batch ")
plt.plot(range(0,100,5),loss_stochastic,'b-',label='Stochastic Loss')
plt.plot(range(0,100,5),loss_batch,'r-',label='Batch Loss')
plt.legend(loc='upper right', prop={'size':11})
plt.show()