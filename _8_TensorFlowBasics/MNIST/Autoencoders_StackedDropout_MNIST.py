
# coding: utf-8

# # Stacked Autoencoder with Dropout
# 
# Inspired and modified from: https://github.com/ageron/handson-ml/blob/master/15_autoencoders.ipynb by Aurélien Géron

# In[13]:

# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals

import numpy as np
import tensorflow as tf
import sys

from tensorflow.examples.tutorials.mnist import input_data


# ### To plot pretty figures inline in the notebook

# In[14]:

#get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt


# In[15]:

print(tf.__version__)
print(np.__version__)
print(matplotlib.__version__)


# ### Store the MNIST data in "mnist_data/" in the current working directory

# In[16]:

mnist = input_data.read_data_sets("mnist_data/")


# ### Result the default graph so you can have a fresh run

# In[17]:

tf.reset_default_graph()


# ### Displays a digit inline on screen
# * Takes in a 1-D array of 784 pixels representing an image

# In[18]:

def display_digit(digit):
    plt.imshow(digit.reshape(28, 28), cmap="Greys", interpolation='nearest')


# ### Pass in 2 test images and see how they are reconstructed using the Autoencoder
# 
# * Reconstructs the session using the saved model
# * Sets up the plot to display the original and reconstructed image side-by-side

# In[19]:

def show_reconstructed_digits(X, outputs, model_path = None, num_digits = 2):
    with tf.Session() as sess:
        if model_path:
            saver.restore(sess, model_path)
        X_test = mnist.test.images[20 : 20 + num_digits]
        outputs_val = outputs.eval(feed_dict={X: X_test})

    fig = plt.figure(figsize=(8, 3 * num_digits))
    for i in range(num_digits):
        plt.subplot(num_digits, 2, i * 2 + 1)
        display_digit(X_test[i])
        plt.subplot(num_digits, 2, i * 2 + 2)
        display_digit(outputs_val[i])


# ### Build a stacked denoising autoencoder with 3 hidden layers
#    * Number of inputs are 28 * 28 = 784, the number of pixels in any MNIST image
#    * The hidden layers are symmetric and get progressively narrower
#    * The narrowest layer is the codings
#    * The number of inputs is equal to the number of outputs 

# In[20]:

n_inputs = 28 * 28
n_hidden1 = 300
n_hidden2 = 150  # codings
n_hidden3 = n_hidden1
n_outputs = n_inputs


# In[21]:

X = tf.placeholder(tf.float32, shape=[None, n_inputs])


# ### Avoid overfitting the input data by using dropout instead of regularization
# 
# * Adds a dropout to the very first hidden layer
# * Use a boolean value "training" to determine whether the dropout should be applied or not
# * Dropout should be used only while training and not during prediction

# In[22]:

dropout_rate = 0.3

training = tf.placeholder_with_default(False, shape=(), name='training')
X_drop = tf.layers.dropout(X, dropout_rate, training=training)


# ### Set up layers of the Autoencoder neural network
# 
# * We use a partial specification for tf.layers.dense to make it easier to read the code
# * We use the RELU activation function
# * The last layer does not have an activation function

# In[28]:

from functools import partial

dense_layer = partial(tf.layers.dense,
                      activation=tf.nn.relu)

hidden1 = dense_layer(X_drop, n_hidden1)
hidden2 = dense_layer(hidden1, n_hidden2)
hidden3 = dense_layer(hidden2, n_hidden3)
outputs = dense_layer(hidden3, n_outputs, activation=None)


# ### Set up the loss function and the optimizer

# In[24]:

reconstruction_loss = tf.reduce_mean(tf.square(outputs - X))

optimizer = tf.train.AdamOptimizer(0.01)
training_op = optimizer.minimize(reconstruction_loss)

init = tf.global_variables_initializer()
saver = tf.train.Saver() 


# ### Train the model using training data
# 
# * Note that we do not use the labels from each MNIST batch
# * At the end of each epoch write the model out to a checkpoint
# * The training flag has to be set to True during the training process to enable dropout

# In[25]:

n_epochs = 10
batch_size = 150

with tf.Session() as sess:
    init.run()
    for epoch in range(n_epochs):
        n_batches = mnist.train.num_examples // batch_size

        for iteration in range(n_batches):
            X_batch, _ = mnist.train.next_batch(batch_size)
            sess.run(training_op, feed_dict={X: X_batch, training: True})

        loss_train = reconstruction_loss.eval(feed_dict={X: X_batch})   
        print("\r{}".format(epoch), "Train MSE:", loss_train)

        saver.save(sess, "./stacked_dropout_autoencoder.ckpt")


# In[27]:

show_reconstructed_digits(X, outputs, "./stacked_dropout_autoencoder.ckpt")


# In[ ]:



