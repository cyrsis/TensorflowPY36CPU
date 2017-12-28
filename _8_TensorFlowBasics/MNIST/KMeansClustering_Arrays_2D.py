
# coding: utf-8

# # K-means Clustering using Simple 2-D Arrays

# ### Import Tensorflow and Numpy libraries

# In[1]:

# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals

import numpy as np
import tensorflow as tf


# ### Plot images inline in the notebook

# In[2]:

get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt


# In[3]:

print(tf.__version__)
print(np.__version__)
print(matplotlib.__version__)


# ### Initialize 3 arrays of points in 2-dimensional space then concat them to a single array
# 
# *Note that the ranges for the random initializations are a little different so there are some natural clusters in the data*

# In[4]:

import random

input_2d_x_1 = np.array([[random.randint(1, 500) for i in range(2)] for j in range(50)], dtype=np.float32)
input_2d_x_2 = np.array([[random.randint(400, 900) for i in range(2)] for j in range(50)], dtype=np.float32)
input_2d_x_3 = np.array([[random.randint(800, 1300) for i in range(2)] for j in range(50)], dtype=np.float32)

input_2d_x = np.append(np.append(input_2d_x_1, input_2d_x_2, axis=0), input_2d_x_3, axis=0)

input_2d_x


# ### Input function to generate features and labels for the estimator
# 
# *This is an unsupervised algorithm so we generate only the features, labels is set to None*
# 
# * The function takes in a 2-D array as an input
# * Converts this array to a Tensor
# * Returns a tuple of features and labels

# In[5]:

def input_fn_2d(input_2d):
    input_t = tf.convert_to_tensor(input_2d, dtype=tf.float32)
    
    return (input_t, None)


# In[6]:

plt.scatter(input_2d_x[:,0], input_2d_x[:,1], s=200)
plt.show()


# In[7]:

from tensorflow.contrib.learn.python.learn.estimators import kmeans

from tensorflow.contrib.factorization.python.ops import clustering_ops


# ### TensorFlow documentation
# 
# https://www.tensorflow.org/api_docs/python/tf/contrib/learn/KMeansClustering
# 
# __init__(
#     num_clusters,
#     model_dir=None,
#     initial_clusters=RANDOM_INIT,
#     distance_metric=SQUARED_EUCLIDEAN_DISTANCE,
#     random_seed=0,
#     use_mini_batch=True,
#     mini_batch_steps_per_iteration=1,
#     kmeans_plus_plus_num_retries=2,
#     relative_tolerance=None,
#     config=None
# )

# In[11]:

# Add the additional parameters later
k_means_estimator = kmeans.KMeansClustering(num_clusters=3)
# k_means_estimator = kmeans.KMeansClustering(num_clusters=3,
#                                             distance_metric=clustering_ops.COSINE_DISTANCE,
#                                             use_mini_batch=False,
#                                             relative_tolerance=1)

fit = k_means_estimator.fit(input_fn=lambda: input_fn_2d(input_2d_x), steps=1000)


# ### The centroids of the clusters

# In[12]:

clusters_2d = k_means_estimator.clusters()
clusters_2d


# ### Plot the cluster centers along with the points

# In[59]:

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(input_2d_x[:,0], input_2d_x[:,1], s=300, marker='o')
ax1.scatter(clusters_2d[:,0], clusters_2d[:,1], c='r', s=200, marker='s')

plt.show()


# In[13]:

k_means_estimator.get_params()


# ### Predicts which cluster each point belongs to
# 
# *Note that the predict() function expects the input exactly like how we specified the feature vector*

# In[14]:

# Try the following values [850, 850], [50, 50], [400, 400]
ex_2d_x = np.array([[400, 400]], dtype=np.float32)

predict = k_means_estimator.predict(input_fn=lambda: input_fn_2d(ex_2d_x), as_iterable=False)


# In[15]:

predict


# In[ ]:



