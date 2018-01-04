import tensorflow.contrib.keras
import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

# ========================================================================= #
#                              Shadow Net for MNIS                          #
# :                       x as in put y is the label                        #
# ========================================================================= #
# load Data
from keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Inspect the samples
# print("X_train Shape" + str(X_train.shape))#6000,28,28

# print("y_train Shape" + str(y_train.shape))

# X_train Shape(60000, 28, 28)
# y_train Shape(60000,)

# print("y_train samples First 100 " + str(y_train[0:99]))
# print("X_train Array " + str(X_train)) # it is a array of a picture

# Change to 1 D

X_train = X_train.reshape(60000, 784).astype('float32')  # 28x 28 = 784
X_test = X_test.reshape(10000, 784).astype('float32')  # 28x 28 = 784

X_train /= 255
X_test /= 255

# Do One Hot
n_classes = 10  # 10 different type of numbers
y_train =to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)



# Design network

model = Sequential()
model.add(Dense((64), activation='sigmoid', input_shape=(784,))) #64 is the hidden layer
# dense_1 (Dense)              (None, 64)                50240 (784*64)+ 64

model.add(Dense((10), activation='softmax'))
# dense_2 (Dense)              (None, 10)                650 (#64 come in, *10 )+10
model.summary()

#Config the model
model.compile(loss='mean_squared_error',optimizer=SGD(lr=0.01),metrics=['accuracy'])

#Train
model.fit(X_train,y_train,batch_size=128,epochs=1000, verbose=1,validation_data=(X_test,y_test))

##something
