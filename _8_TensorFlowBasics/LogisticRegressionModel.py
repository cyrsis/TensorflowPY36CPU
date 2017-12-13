# Logistic Regression model

# First , we define the problem we want to solve
# 1. Classifying image of character by Font
# 2. Using Logistic regression to "score" each class
# 3. Build a logistic regression model

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np

#tqdm is option, it just show some nice progress bar
try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x, *args, **kwargs):
        return x


#set random seed
np.random.seed(0)
# Get some consistent thing for the random number

# Load data
data = np.load('data_with_labels.npz')


# The data we load contain 5 fonts and compress in npz file

train = data['arr_0']/255. # it holds the pixel value from the font
labels = data['arr_1']   # type of fonts

# Look at some data
print(train[0])
print(labels[0])

# If you have matplotlib installed
import matplotlib.pyplot as plt
plt.ion()


# Let's look at a subplot of one of A in each font
f, plts = plt.subplots(5, sharex=True)
c = 91
for i in range(5):
    plts[i].pcolor(train[c + i * 558],
                   cmap=plt.cm.gray_r)

def to_onehot(labels,nclasses = 5):
    '''
    Convert labels to "one-hot" format.
    >>> a = [0,1,2,3]
    >>> to_onehot(a,5)
    array([[ 1.,  0.,  0.,  0.,  0.],
           [ 0.,  1.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  1.,  0.]])
    '''
    outlabels = np.zeros((len(labels),nclasses))
    for i,l in enumerate(labels):
        outlabels[i,l] = 1
    return outlabels

#Fix from stackoverflow
plt.interactive(False)
plt.show()


# This is call to onehot function
onehot = to_onehot(labels)


# Linear Regression, you have know the logistic regression
# It represent the weights and sum in here

# Split data into training and validation
indices = np.random.permutation(train.shape[0])
valid_cnt = int(train.shape[0] * 0.1)
test_idx, training_idx = indices[:valid_cnt],\
                         indices[valid_cnt:]
test, train = train[test_idx,:],\
              train[training_idx,:]
onehot_test, onehot_train = onehot[test_idx,:],\
                        onehot[training_idx,:]


# This is the true start of tensorflow session
sess = tf.InteractiveSession()


# These will be inputs
## Input pixels, flattened
x = tf.placeholder("float", [None, 1296])
## Known labels
y_ = tf.placeholder("float", [None,5])

# Variables
W = tf.Variable(tf.zeros([1296,5])) # This is weight
b = tf.Variable(tf.zeros([5]))  #This is bias


# Just initialize
sess.run(tf.global_variables_initializer())

# Define model
y = tf.nn.softmax(tf.matmul(x,W) + b) #This computate the probability of the tensorflow

### End model specification, begin training code


#### Logistic Regression loss function
# Training model weights with Tensorflow
# Evaluating model accuracy and weights


#Goal: Minize how wrong I am

# Climb on cross-entropy
cross_entropy = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(
        logits=y + 1e-50,labels= y_))

# we add the 1e-50 to maintain the stability problems
# Think of punish the model more for less accuracy


# How we train
# 0.1 to help us train better, the best class of working on it
train_step = tf.train.GradientDescentOptimizer(
                0.1).minimize(cross_entropy)


# Define accuracy
correct_prediction = tf.equal(tf.argmax(y,1),
                     tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(
           correct_prediction, "float"))

# Actually train
epochs = 1000
train_acc = np.zeros(epochs//10)
test_acc = np.zeros(epochs//10)
for i in tqdm(range(epochs)):
    # Record summary data, and the accuracy
    if i % 10 == 0:
        # Check accuracy on train set on every 10 epics
        A = accuracy.eval(feed_dict={
            x: train.reshape([-1,1296]),
            y_: onehot_train})
        train_acc[i//10] = A
        # And now the validation set
        A = accuracy.eval(feed_dict={
            x: test.reshape([-1,1296]),
            y_: onehot_test})
        test_acc[i//10] = A
        # Improve the accuracy in hereR
    train_step.run(feed_dict={
        x: train.reshape([-1,1296]),
        y_: onehot_train})

# Notice that accuracy flattens out
print(train_acc[-1])
print(test_acc[-1])

# Plot the accuracy curves
plt.figure(figsize=(6,6))
plt.plot(train_acc,'bo')
plt.plot(test_acc,'rx')

plt.interactive(False)
plt.show()


# Look at a subplot of the weights for each font
f, plts = plt.subplots(5, sharex=True)
for i in range(5):
    plts[i].pcolor(W.eval()[:,i].reshape([36,36]))

plt.interactive(False)
plt.show()

