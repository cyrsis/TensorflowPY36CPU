import tensorflow as tf


#Get some variable
CONSTANT_A  = tf.constant([100.0])
CONSTANT_B  = tf.constant([300.0])
CONSTANT_C  = tf.constant([3.0])

#Operation
sum_= tf.add(CONSTANT_A,CONSTANT_C)
mul_ = tf.multiply(CONSTANT_A,CONSTANT_C)

#Graph

with tf.Session() as sess:
    result = sess.run([sum_,mul_])
    print(result)
