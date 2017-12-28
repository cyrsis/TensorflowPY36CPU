
# coding: utf-8

# # Stacked Autoencoders
# 
# Inspired and modified from: https://github.com/ageron/handson-ml/blob/master/15_autoencoders.ipynb by Aurélien Géron

# In[1]:

# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals

import numpy as np
import tensorflow as tf
import sys

from tensorflow.examples.tutorials.mnist import input_data


# ### To plot pretty figures inline in the notebook

# In[2]:

get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt


# In[5]:

print(tf.__version__)
print(np.__version__)
print(matplotlib.__version__)


# ### Store the MNIST data in "mnist_data/" in the current working directory

# In[6]:

mnist = input_data.read_data_sets("mnist_data/")


# ### Result the default graph so you can have a fresh run

# In[7]:

tf.reset_default_graph()


# ### Displays a digit inline on screen
# * Takes in a 1-D array of 784 pixels representing an image

# In[21]:

def display_digit(digit):
    plt.imshow(digit.reshape(28, 28), cmap="Greys", interpolation='nearest')


# ### Pass in 2 test images and see how they are reconstructed using the Autoencoder
# 
# * Reconstructs the session using the saved model
# * Sets up the plot to display the original and reconstructed image side-by-side

# In[8]:

def show_reconstructed_digits(X, outputs, model_path = None, num_digits = 2):
    with tf.Session() as sess:
        if model_path:
            saver.restore(sess, model_path)
        X_test = mnist.test.images[5 : 5 + num_digits]
        outputs_val = outputs.eval(feed_dict={X: X_test})

    fig = plt.figure(figsize=(8, 3 * num_digits))
    for i in range(num_digits):
        plt.subplot(num_digits, 2, i * 2 + 1)
        display_digit(X_test[i])
        plt.subplot(num_digits, 2, i * 2 + 2)
        display_digit(outputs_val[i])


# ### Build a stacked autoencoder with 3 hidden layers
#    * Number of inputs are 28 * 28 = 784, the number of pixels in any MNIST image
#    * The hidden layers are symmetric and get progressively narrower
#    * The narrowest layer is the codings
#    * The number of inputs is equal to the number of outputs 

# In[9]:

n_inputs = 28 * 28
n_hidden1 = 300
n_hidden2 = 150  # codings
n_hidden3 = n_hidden1
n_outputs = n_inputs


# ### Initialization and regularization
# 
# * The He initializer is used to initialize the weights of the neurons, this has proven to greatly **reduce the vanishing and exploding gradients** problem in neural networks
# * The l2 regularizer is used to **prevent overfitting** of the neural network to the data

# In[10]:

he_init = tf.contrib.layers.variance_scaling_initializer()
l2_regularizer = tf.contrib.layers.l2_regularizer(0.0001)


# In[11]:

X = tf.placeholder(tf.float32, shape=[None, n_inputs])


# ### Set up layers of the Autoencoder neural network
# 
# * We use a partial specification for tf.layers.dense to make it easier to read the code
# * We use the ELU activation function which greatly reduces the problem of dying neurons
# * The last layer does not have an activation function

# In[28]:

from functools import partial

dense_layer = partial(tf.layers.dense,
                      activation=tf.nn.elu,
                      kernel_initializer=he_init,
                      kernel_regularizer=l2_regularizer)

hidden1 = dense_layer(X, n_hidden1)
hidden2 = dense_layer(hidden1, n_hidden2)
hidden3 = dense_layer(hidden2, n_hidden3)
outputs = dense_layer(hidden3, n_outputs, activation=None)


# ### Set up the loss function and the optimizer
# 
# * Use the MSE to calculate reconstruction losses - compare outputs with the inputs and not labels (unsupervised!)
# * The regularization losses from each layer are added to find the total loss
# 
# *TensorFlow automatically adds nodes to compute the regularization losses for each layer to a collection which can be accessed using the key tf.GraphKeys.REGULARIZATION_LOSSES*

# In[29]:

reconstruction_loss = tf.reduce_mean(tf.square(outputs - X))

reg_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
loss = tf.add_n([reconstruction_loss] + reg_losses)

optimizer = tf.train.AdamOptimizer(0.01)
training_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()


# #### The saver is used to save a model to directory, this model can be reloaded into the session when needed

# In[30]:

saver = tf.train.Saver()


# ### Train the model using training data
# 
# * Note that we do not use the labels from each MNIST batch
# * At the end of each epoch write the model out to a checkpoint

# In[31]:

n_epochs = 6
batch_size = 150

with tf.Session() as sess:
    init.run()
    for epoch in range(n_epochs):
        n_batches = mnist.train.num_examples // batch_size

        for iteration in range(n_batches):
            X_batch, _ = mnist.train.next_batch(batch_size)
            sess.run(training_op, feed_dict={X: X_batch})

        loss_train = reconstruction_loss.eval(feed_dict={X: X_batch})   
        print("\r{}".format(epoch), "Train MSE:", loss_train)

        saver.save(sess, "./stacked_autoencoder.ckpt")


# In[22]:

# With regularization
show_reconstructed_digits(X, outputs, "./stacked_autoencoder.ckpt")


# In[27]:

# Without regularization
show_reconstructed_digits(X, outputs, "./stacked_autoencoder.ckpt")


# In[ ]:



