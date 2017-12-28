
# coding: utf-8

# # PCA with matplotlib and Autoencoders

# In[6]:

# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals

import numpy as np
import pandas as pd
import tensorflow as tf


# ### To plot pretty figures inline in the notebook

# In[7]:

get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.mlab import PCA


# In[8]:

print(tf.__version__)
print(np.__version__)
print(pd.__version__)
print(matplotlib.__version__)


# ### Read in stocks data from the directory data/stocks.csv
# 
# A link where this CSV file can be downloaded is here: https://goo.gl/PUiiQv
# 
# * This is data for the monthly closing price of 10 stocks over a 10 year period. 
# * There are 12 * 10 = 120 rows in this dataset and 10 columns, one for each stock
# * The original CSV files has a header row and an additional first column to hold the date - we'll leave these out when we convert this to a matrix to do a PCA

# In[9]:

prices = pd.read_csv('data/stocks.csv')
prices.head()


# ### Sort the prices data by date
# 
# * We're going to work with stock returns and not prices because they tend to be stationery when calculated across years (returns from 2007 can be compared to returns from 2016 even of the stock prices may have changed)
# * Returns are the percentage change in the price of the stock from the previous close
# * Sort the prices by dates in preparation for calculating returns
# * We'll work with just 3 inputs i.e. 3 stocks AAPL, GOOG and NFLX. Try this same code out with more stocks as practice!

# In[10]:

prices['Date'] = pd.to_datetime(prices['Date'], infer_datetime_format=True)
prices = prices.sort_values(['Date'], ascending=[True])

prices = prices[['AAPL', 'GOOG', 'NFLX']]
prices.head()


# ### Calculate returns
# 
# * The pct_change() function in pandas does this automatically for you, apply this only to numeric columns
# * Leave out the first row (with the earliest date) because no returns will be calculated for it

# In[11]:

returns = prices[[key for key in dict(prices.dtypes) if dict(prices.dtypes)[key] in ['float64', 'int64']]].pct_change()
returns = returns[1:]
returns.head()


# ### Choose a small part of this dataset
# 
# *In order to make it easier to understand and follow the demo we choose only 20 rows from the dataset.*

# In[12]:

returns_arr = returns.as_matrix()[:20]
returns_arr.shape


# ### Scale all inputs
# 
# PCA works better if the mean and variance of each input component is the same. Each of our inputs can be scaled to achieve this. Scaling the data involves:
# 
# * Subtracting the mean for every point
# * Dividing by the variance
# 
# Every point on the data set is now centered around 0 and has the same scale

# In[13]:

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
returns_arr_scaled = scaler.fit_transform(returns_arr)


# In[14]:

returns_arr_scaled


# ### Run PCA using a standard Python library
# 
# * Set standardize to False because we have already scaled the data ourselves
# * **fracs** gives us the proportion of variance of each principal component i.e. how much each component contributes to explaining the variance in the input

# In[15]:

results = PCA(returns_arr_scaled, standardize=False)
results.fracs


# ### Projection of the original data in PCA space
# 
# This has all the principal components from the original data. **The original data can be completely reconstructed if we use all the principal components**

# In[16]:

results.Y 


# ### The weight vector
# 
# This is the vector used to project the original data into PCA space. This can be used on the principal components to reconstruct the original data.

# In[17]:

results.Wt


# ### Generating the original data from the principal components and the weight vector

# In[18]:

np.dot(results.Y, results.Wt)


# ## Set up the TensorFlow code for an Autoencoder
# 
# * The number of inputs of the auto-encoder is equal to the number of outputs (number of columns in our input data)
# * We have one hidden layer with 2 neurons
# * Use an AdamOptimizer to minimize the loss
# 
# Notice that:
# 
# * The reconstruction loss of the output is the **mean-square error**
# * Each layer has **no activation function** i.e is a linear layer
# 
# An Autoencoder set up this way simply **performs a PCA**

# In[19]:

import tensorflow as tf

n_inputs = 3
n_hidden = 2  # codings
n_outputs = n_inputs

learning_rate = 0.01

tf.reset_default_graph()

X = tf.placeholder(tf.float32, shape=[None, n_inputs])
hidden = tf.layers.dense(X, n_hidden)
outputs = tf.layers.dense(hidden, n_outputs)

reconstruction_loss = tf.reduce_mean(tf.square(outputs - X))

optimizer = tf.train.AdamOptimizer(learning_rate)
training_op = optimizer.minimize(reconstruction_loss)

init = tf.global_variables_initializer()


# ### Run the training data through the Autoencoder
# 
# * We do not use any labels for this training only the input data
# * The output is the reconstructed value using only the 2 principal components
# 
# *Note that the reconstruction will not be equal to the input data*

# In[20]:

n_iterations = 10000

with tf.Session() as sess:
    init.run()
    for iteration in range(n_iterations):
        training_op.run(feed_dict={X: returns_arr_scaled})

    outputs_val = outputs.eval(feed_dict={X: returns_arr_scaled})
    print(outputs_val)


# ### The output of the PCA is equal to the reconstructed output if we used only 2 principal components

# In[21]:

np.dot(results.Y[:,[0,1]], results.Wt[[0,1]])


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



