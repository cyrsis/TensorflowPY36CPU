import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops

ops.reset_default_graph()


# victor
# 16/12/2017
# Created @ 2017-12-16 00:57
def inputs():
    pass


def train(total_loss):
    pass


def inference(X):
    pass


def loss(X, Y):
    pass


def evaluate(sess, X, Y):
    pass



model_saver = tf.train.Saver()

with tf.Session() as sess:
    tf.global_variables_initializer().run()

    X, Y = inputs()

    total_loss = loss(X, Y)

    train_ops = train(total_loss)

    coord = tf.train.Coordinator()

    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    train_steps = 1000

    for steps in range(train_steps):
        sess.run([train_ops])

        if steps % 10 == 0:
            print("Loss ", sess.run([total_loss]))


    evaluate(sess, X, Y)

    coord.request_stop()
    coord.join(threads)

    model_saver.save(sess,'my_model',global_step=train_steps)
    sess.close()
