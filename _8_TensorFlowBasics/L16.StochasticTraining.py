# ========================================================================= #
#                              Stochastic Training                          #
# :                                                                         #
# ========================================================================= #
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.framework  import ops
ops.reset_default_graph()

sess = tf.Session()


batch_size= 25

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
