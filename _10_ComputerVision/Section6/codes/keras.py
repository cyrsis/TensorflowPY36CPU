from keras.models import Sequential

from keras.layers.convolutional import Convolution2D, MaxPooling2D

from keras.layers.core import Activation, Flatten, Dense

from keras.optimizers import SGD

from keras.utils import np_utils

from sklearn import datasets

from sklearn.model_selection import train_test_split

import numpy as np 



num_classes=10

img_depth=1

img_height=28

img_width=28

model = Sequential()



model.add(Convolution2D(20, 5, 5, border_mode="same", input_shape=(img_depth, img_height, img_width)))

model.add(Activation("relu"))

model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), dim_ordering="th"))

model.add(Convolution2D(50, 5, 5, border_mode="same"))

model.add(Activation("relu"))

model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), dim_ordering="th"))

model.add(Flatten())

model.add(Dense(output_dim=500))

model.add(Activation("relu"))

model.add(Dense(output_dim=num_classes))

model.add(Activation("softmax"))



mnist = datasets.fetch_mldata("MNIST Original")



mnist.data = mnist.data.reshape((mnist.data.shape[0], 28, 28))

mnist.data = mnist.data[:, np.newaxis, :, :]

mnist.data = mnist.data / 255.0



train_data, test_data, train_label, test_label = train_test_split(mnist.data, mnist.target, test_size=0.25)

train_label = np_utils.to_categorical(train_label, 10)

test_label = np_utils.to_categorical(test_label, 10)



model.compile(loss="categorical_crossentropy", optimizer=SGD(lr=0.0001), metrics=["accuracy"])

model.fit(train_data, train_label, batch_size=32, nb_epoch=30, verbose=1)



loss, accuracy = model.evaluate(test_data, test_label, batch_size=64, verbose=1)

print("Accuracy: {} %".format(accuracy * 100))

