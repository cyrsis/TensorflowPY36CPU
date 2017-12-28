
# coding: utf-8

# # K-means Clustering using Simple 1-D Arrays

# In[3]:

# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals

import numpy as np
import tensorflow as tf


# ### To plot pretty figures inline in the notebook

# In[6]:

get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt


# In[7]:

get_ipython().system(u'pip install --upgrade tensorflow')
print(tf.__version__)
print(np.__version__)
print(matplotlib.__version__)


# ### Set up any 1-D array at random
# 
# * Notice that this data is clustered around 0-10 and around 80-120

# In[8]:

input_1d_x = np.array([1, 2, 3.0, 4, 5, 126, 21, 33, 6, 73.0, 2, 3, 56, 98, 100, 4, 8, 33, 102], dtype=np.float32)


# ### Input function to generate features and labels for the estimator
# 
# *This is an unsupervised algorithm so we generate only the features, labels is set to None*
# 
# * The function takes in a 1-D array as an input and converts it to a Tensor
# * Expands its dimensions [1, 2, 3] -> [[1], [2], [3]] to get a feature vector
# * Returns a tuple of features and labels

# In[12]:

def input_fn_1d(input_1d):
    input_t = tf.convert_to_tensor(input_1d, dtype=tf.float32)
    input_t = tf.expand_dims(input_t, 1)
    
    return (input_t, None)


# In[13]:

plt.scatter(input_1d_x, np.zeros_like(input_1d_x), s=500)
plt.show()


# In[14]:

from tensorflow.contrib.learn.python.learn.estimators import kmeans


# ### TensorFlow documentation

# https://www.tensorflow.org/api_docs/python/tf/contrib/learn/KMeansClustering

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

# In[20]:

k_means_estimator = kmeans.KMeansClustering(num_clusters=2)

fit = k_means_estimator.fit(input_fn=lambda: input_fn_1d(input_1d_x), steps=1000)


# ### The centroids of the clusters

# In[21]:

clusters_1d = k_means_estimator.clusters()
clusters_1d


# ### Plot the cluster centers along with the points 

# In[22]:

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(input_1d_x, np.zeros_like(input_1d_x), s=300, marker='o')
ax1.scatter(clusters_1d, np.zeros_like(clusters_1d), c='r', s=200, marker='s')

plt.show()


# In[23]:

k_means_estimator.get_params()


# In[26]:

for variable_name in fit.get_variable_names():
   print(variable_name, " ---> " , fit.get_variable_value(variable_name))


# ### Transforms each element to distances to cluster centers.
# 
# *Note that the transform() function expects the input exactly like how we specified the feature vector*

# In[27]:

ex_1d_x = np.array([0, 100], dtype=np.float32)

transform = k_means_estimator.transform(input_fn=lambda: input_fn_1d(ex_1d_x))


# ### The distance is measured in squared Euclidean distance
# *Get the square root to find actual distances*

# In[30]:

np.sqrt(transform)


# In[31]:

clusters_1d


# ### Predicts which cluster each point belongs to
# 
# *Note that the predict() function expects the input exactly like how we specified the feature vector*

# In[33]:

# Change the 50 to 54 and it will move to the next cluster
ex_1d_x = np.array([50, 150], dtype=np.float32)

predict = k_means_estimator.predict(input_fn=lambda: input_fn_1d(ex_1d_x), as_iterable=False)


# In[34]:

predict


# In[ ]:



