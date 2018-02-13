import numpy as np
import tensorflow as tf

# TENSORFLOW CODE

INPUT_SIZE = 3

x = tf.placeholder(tf.float32, shape=(1, INPUT_SIZE))

weights = tf.Variable(tf.random_normal((INPUT_SIZE, 1)), name="weights")
biases = tf.Variable(tf.zeros(shape=1), name="biases")

model = tf.nn.sigmoid(tf.matmul(x, weights) + biases)

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

print(sess.run(model, feed_dict={x: np.random.uniform(size=(1, INPUT_SIZE))}))

# KERAS CODE

from keras.models import Sequential
from keras.layers import Dense

m = Sequential()
m.add(Dense(1, input_shape=(1, INPUT_SIZE), activation='sigmoid'))

m.compile(optimizer='adam', loss='mse')

print(m.predict(np.random.uniform(size=(1, 1, INPUT_SIZE)))[0])
