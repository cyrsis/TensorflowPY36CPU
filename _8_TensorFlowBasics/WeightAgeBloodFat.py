# ========================================================================= #
#                              X = Weight, Age
#                              Y = Blood Fat                                      #

# Problems:age and weight are to be related to blood fat content.
#
#  Data: http://people.sc.fsu.edu/~jburkardt/datasets/regression/x09.txt
#
# ========================================================================= #
import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops

ops.reset_default_graph()


#Variables and Placeholder

weights = tf.Variable(tf.zeros([2, 1]), name="weights")
bias = tf.Variable(0., name="bias")
# victor
# 16/12/2017
# Created @ 2017-12-16 00:57

def inputs():
    weight_age = [[84, 46], [73, 20], [65, 52], [70, 30], [76, 57], [69, 25], [63, 28], [72, 36], [79, 57], [75, 44],
                  [27, 24], [89, 31], [65, 52], [57, 23], [59, 60], [69, 48], [60, 34], [79, 51], [75, 50], [82, 34],
                  [59, 46], [67, 23], [85, 37], [55, 40], [63, 30]]
    blood_fat_content = [354, 190, 405, 263, 451, 302, 288, 385, 402, 365, 209, 290, 346, 254, 395, 434, 220, 374, 308,
                         220, 311, 181, 274, 303, 244]
    
    return tf.to_float(weight_age), tf.to_float(blood_fat_content)

def loss(X, Y):
    Y_predicted = tf.transpose(inference(X))  # make it a row vector
    return tf.reduce_sum(tf.squared_difference(Y, Y_predicted))

def train(total_loss):
    learning_rate = 0.000001
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)


def inference(X):
    return tf.matmul(X, weights) + bias





def evaluate(sess, X, Y):
    print(sess.run(inference([[50., 20.]])))  # ~ 303
    print(sess.run(inference([[50., 70.]])))  # ~ 256
    print(sess.run(inference([[90., 20.]])))  # ~ 303
    print(sess.run(inference([[90., 70.]])))  # ~ 256


model_saver = tf.train.Saver()

with tf.Session() as sess:
    tf.global_variables_initializer().run()

    X, Y = inputs()

    total_loss = loss(X, Y)

    train_ops = train(total_loss)

    coord = tf.train.Coordinator()

    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    train_steps = 10000

    for steps in range(train_steps):
        sess.run([train_ops])

        if steps % 1000 == 0:
            print("Loss ", sess.run([total_loss]))

    print("Final model W=", sess.run(weights), "b=", sess.run(bias))

    evaluate(sess,X,Y)

    coord.request_stop()
    coord.join(threads)

    model_saver.save(sess, 'my_model', global_step=train_steps)
    sess.close()
