import tensorflow as tf
import numpy as np
import math
# Learn more sklearn
# scikit-learn.org
import sklearn
from sklearn import metrics

# Learn more skflow
# github.com/tensorflow/skflow
# Or install
# pip install \
# https://github.com/tensorflow/skflow/archive/master.zip
import tensorflow.contrib as skflow

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x, *args, **kwargs):
        return x

# Seed the data
np.random.seed(0)

# Load data
data = np.load('./SampleData/data_with_labels.npz')
train = data['arr_0']/255.
labels = data['arr_1']

# Look at some data
print(train[0])
print(labels[0])

# If you have matplotlib installed
import matplotlib.pyplot as plt
plt.ion()

# Split data into training and validation
indices = np.random.permutation(train.shape[0])
valid_cnt = int(train.shape[0] * 0.1)
test_idx, training_idx = indices[:valid_cnt],\
                         indices[valid_cnt:]
test, train = train[test_idx,:],\
              train[training_idx,:]
test_labels, train_labels = labels[test_idx],\
                        labels[training_idx]

sess = tf.InteractiveSession()

# Logistic Regression
# steps is number of total batches
# steps/batch_size = num_epochs
classifier = skflow.TensorFlowLinearClassifier(
            n_classes=5,
            steps=1000,
            optimizer='Adam',
            learning_rate=0.01,
            continue_training=True)

# One line training
classifier.fit(train.reshape([-1,36*36]),train_labels)

# sklearn compatible accuracy
sklearn.metrics.accuracy_score(test_labels,
        classifier.predict(test.reshape([-1,36*36])))

# Dense neural net
classifier = skflow.TensorFlowDNNClassifier(
            hidden_units=[10,5],
            n_classes=5,
            steps=1000,
            optimizer='Adam',
            learning_rate=0.01,
            continue_training=True)
classifier.fit(train.reshape([-1,36*36]),train_labels)

# simple accuracy
sklearn.metrics.accuracy_score(test_labels,
        classifier.predict(test.reshape([-1,36*36])))

# confusion is easy
conf = metrics.confusion_matrix(train_labels,
        classifier.predict(train.reshape([-1,36*36])))
print(conf)

### Convolutional net
def conv_skflow(X, y):
    X = tf.reshape(X, [-1, 36, 36, 1])
    # conv layer will compute 4 kernels for each 5x5 patch
    with tf.variable_scope('conv_layer'):
        # 5x5 convolution, pad with zeros on edges
        h1 = skflow.ops.conv2d(X, n_filters=4,
                filter_shape=[5, 5], 
                bias=True, activation=tf.nn.relu)
        # 2x2 Max pooling, no padding on edges
        p1 = tf.nn.max_pool(h1, ksize=[1, 2, 2, 1],
                strides=[1, 2, 2, 1], padding='VALID')

    # Need to flatten conv output for use in dense layer
    p1_size = np.product(
              [s.value for s in p1.get_shape()[1:]])
    p1f = tf.reshape(p1, [-1, p1_size ])

    # densely connected layer with 32 neurons and dropout
    h_fc1 = skflow.ops.dnn(p1f,
            [32],
            activation=tf.nn.relu,
            dropout=0.5)
    return skflow.models.logistic_regression(h_fc1, y)

# Use generic estimator with our function
classifier = skflow.TensorFlowEstimator(
            model_fn=conv_skflow,
            n_classes=5,
            steps=1000,
            optimizer='Adam',
            learning_rate=0.01,
            continue_training=True)
classifier.fit(train,train_labels)

# simple accuracy
metrics.accuracy_score(test_labels,classifier.predict(test))

# Convolutional Layer Weights
print(classifier.get_tensor_value(
        'conv_layer/convolution/filters:0'))
print(classifier.get_tensor_value(
        'conv_layer/convolution/bias:0'))

# Dense Layer
print(classifier.get_tensor_value(
        'dnn/layer0/Linear/Matrix:0'))

# Logistic weights
print(classifier.get_tensor_value(
        'logistic_regression/weights:0'))
