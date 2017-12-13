# ========================================================================= #
#                           Steps1.Import data                                      #
# :                                                     #
# ========================================================================= #


import tensorflow as tf

##1. Generatate data if we know the expected results

##2. Transform and normalize data
##    Most algorithms expect normalize data and we do this here as well,

data = tf.nn.batch_norm_with_global_normalization()

##3. Parameters

LEARN_RATE = 1e-2
ITERATION = 1000

##4 Init Variable and placeholders (Tensorflow is set once and cannt changes types)

a_var = tf.constant(42)
xinput= tf.placeholder(tf.float32,[None, input_size])
yinput = tf.placeholder(tf.float32,[None,num_classes])

##5. Define model Structure (Tell what needs to be computer)
# y = mx+B
y_perd =tf.add(tf.multiply(xinput,weight_matrix),b_matrix)

##7 Define the losee fucntion (Evaluate the output)

loss = tf.reduce_mean(tf.square(y_actual - y_perd))

##8. Train the mode

with tf.Session as sess:
    sess.run()

session = tf.Session(graph=graph)
session.run()






