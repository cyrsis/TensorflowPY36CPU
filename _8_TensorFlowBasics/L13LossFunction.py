import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

from tensorflow.python.framework import ops

ops.reset_default_graph()

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()

# Numerical predictions, create a sequence of predictions around a target,

x_vals = tf.linspace(-1., 1., 500)

target = tf.constant(0.)

# L2 Loss square(target -x_vals)

l2_y_vals = tf.square(target - x_vals)
l2_y_out = sess.run(l2_y_vals)

# L1 Loss , take the abs value of the difference instead of square it

l1_y_values = tf.abs(target - x_vals)
l1_y_out = sess.run(l1_y_values)

# Pseudo-Huber losses (a smooth approximation to the L1 loss as the (predicted-target) values get larger, when the predicated values are clsoe to the target, the pseudo loss behave similar to the l2 losses )

# Pseudo with delta =0.25
delta1 = tf.constant(0.25)
phuber1_y_vals = tf.multiply(tf.square(delta1), tf.sqrt(1. + tf.square((target - x_vals) / delta1) - 1.))
phuber1_y_out = sess.run(phuber1_y_vals)

# Pseudio with delta =0.5
delta2 = tf.constant(0.5)
phuber2_y_vals = tf.multiply(tf.square(delta2), tf.sqrt(1. + tf.square((target - x_vals) / delta2)) - 1.)
phuber2_y_out = sess.run(phuber2_y_vals)

# plot them
x_array = sess.run(x_vals)
plt.title('Lose Fuction in Tensorflow')
plt.plot(x_array,l2_y_out,'b--',label='L2 Loss')
plt.plot(x_array,l1_y_out,'r--',label='L1 Loss')
plt.plot(x_array,phuber1_y_out,'k--',label='P-Huber Loss 0.25')
plt.plot(x_array,phuber2_y_out,'g:',label='P-Huber Loss 5.0')
plt.ylim(-0.2,0.4)
plt.legend(loc='lower right',prop={'size':11})

plt.show()

#Categorocal loss function

x_vals = tf.linspace(-3.,5.,500)

#Target os 1.0
target = tf.constant(1.)
targets = tf.fill([500,],1.)

# print(sess.run(targets))

#hinger lose is useful for categorical prediction here is the max(0,1-(pred*actual))

hing_y_vals = tf.maximum(0.,1.-tf.multiply(target,x_vals))
hing_y_out =sess.run(hing_y_vals)

#Cross Entropy Losses
# L= -actual *(log(pred)-(1-actual)(log(1-pred)))
xentropy_y_vals=- tf.multiply(target,tf.log(x_vals))-tf.multiply((1.-target),tf.log(1.-x_vals))
xentropy_y_out =sess.run(xentropy_y_vals)

#Sigmoid Entroy Loss
#Similiar to cross-entropy function except that we take the sigmoid of the predicition in the function
# L = -actual * (log(sigmoid(pred))) - (1-actual)(log(1-sigmoid(pred)))
# or
# L = max(actual, 0) - actual * pred + log(1 + exp(-abs(actual)))

x_val_input = tf.expand_dims(x_vals,1)
target_input = tf.expand_dims(targets,1)
xentropy_sigmoid_y_vals = tf.nn.softmax_cross_entropy_with_logits(logits=x_val_input,labels=target_input)
xentropy_sigmoid_y_out =sess.run(xentropy_sigmoid_y_vals)


#Weighted (Softmax) Cross Entropy Loss
# Weighted (softmax) cross entropy loss
# L = -actual * (log(pred)) * weights - (1-actual)(log(1-pred))
# or
# L = (1 - pred) * actual + (1 + (weights - 1) * pred) * log(1 + exp(-actual))

weight = tf.constant(0.5)
xentropy_weighted_y_vals = tf.nn.weighted_cross_entropy_with_logits(x_vals,targets,weight)
xentropy_weighted_y_out = sess.run(xentropy_weighted_y_vals)

#plot

x_array=sess.run(x_vals)
plt.title("Categorical Predictions")
plt.plot(x_array, hing_y_out,'b-',label='Hinge Loss')
plt.plot(x_array,xentropy_y_out,'r--',label='Cross Entropy Loss')
plt.plot(x_array,xentropy_sigmoid_y_out,'k--',label='Cross Entropy Sigmoid Loss')
plt.plot(x_array,xentropy_weighted_y_out,'g:',label='Weighted Cross Entropy Loss (0.5)')
plt.ylim(-1.5,3)
plt.legend(loc='lower right',prop={'size':11})
plt.show()

#Softmax entropy and Sparse Entropy
unscaled_logits = tf.constant([[1., -3., 10.]])
target_dist = tf.constant([[0.1, 0.02, 0.88]])
softmax_xentropy = tf.nn.softmax_cross_entropy_with_logits(logits=unscaled_logits,
                                                           labels=target_dist)
print(sess.run(softmax_xentropy))

# Sparse entropy loss
# Use when classes and targets have to be mutually exclusive
# L = sum( -actual * log(pred) )
unscaled_logits = tf.constant([[1., -3., 10.]])
sparse_target_dist = tf.constant([2])
sparse_xentropy =  tf.nn.sparse_softmax_cross_entropy_with_logits(logits=unscaled_logits,
                                                                  labels=sparse_target_dist)
print(sess.run(sparse_xentropy))
