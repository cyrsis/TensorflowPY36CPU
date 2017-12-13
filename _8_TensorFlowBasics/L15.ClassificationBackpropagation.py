# ========================================================================= #
#                              Classification propagration                                      #
# :                                                     #
# ========================================================================= #
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.framework import ops

ops.reset_default_graph()

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()

# A regression example with punch of numbers

# Creating the target and placeholders
x_vals = np.concatenate((np.random.normal(-1,1,50),np.random.normal(3,1,50)))
y_vals = np.concatenate((np.repeat(0.,50),np.repeat(1.,50)))
x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)

# Create variable (one model parameter =A)
A = tf.Variable(tf.random_normal(mean=10,shape=[1]))

# Add model operation to the graph
# Want to create the operation to sigmoid (x+A)
my_output = tf.add(x_data, A)

#need to add an other dimension to the each
my_output_expanded = tf.expand_dims(my_output,0)
y_target_expanded = tf.expand_dims(y_target,0)



# Add classification Losee (cross entropy)
# sigmoid is left out because we use a loss function that has it build in
xentropy = tf.nn.sigmoid_cross_entropy_with_logits(logits=my_output_expanded,labels=y_target_expanded)



# Optimizer, minize of the lose with learning Rate is 0.05
my_opt = tf.train.GradientDescentOptimizer(0.05)
train_step = my_opt.minimize(xentropy)


#init Variable
sess.run(tf.global_variables_initializer())

# Do the Regression Graph
for i in range(1400):
    rand_index = np.random.choice(100)
    rand_x = [x_vals[rand_index]]
    rand_y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    if (i + 1) % 25 == 0:
        print("Steps #" + str(i + 1))
        print(' A = ' + str(sess.run(A)))
        print("Loss =" + str(sess.run(xentropy, feed_dict={x_data: rand_x, y_target: rand_y})))



predictions =[]
for i in range(len(x_vals)):
    x_val = [x_vals[i]]
    prediction = sess.run(tf.round(tf.sigmoid(my_output)),feed_dict={x_data:x_val})
    predictions.append(prediction[0])

accuracy = sum(x==y for x,y in zip(predictions,y_vals))/100
print('Ending Accuracy = ' + str(np.round(accuracy,2)))
