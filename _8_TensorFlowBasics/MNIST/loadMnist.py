import os
import struct
import numpy as np
import theano
from keras.utils import np_utils
from matplotlib import pyplot as plt


def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    # labels_path = os.path.join(path,
    #						   '%s-labels-idx1-ubyte'
    #							% kind)
    # images_path = os.path.join(path,
    #						   '%s-images-idx3-ubyte'
    #						   % kind)
    if kind == 'train':
        labels_path = os.path.abspath('D:\\pycode35\\AI\\mnist\\train-labels.idx1-ubyte')
        images_path = os.path.abspath('D:\\pycode35\\AI\\mnist\\train-images.idx3-ubyte')
    else:
        labels_path = os.path.abspath('D:\\pycode35\\AI\\mnist\\t10k-labels.idx1-ubyte')
        images_path = os.path.abspath('D:\\pycode35\\AI\\mnist\\t10k-images.idx3-ubyte')

    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack(">IIII",
                                               imgpath.read(16))
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)

    return images, labels


#### Loading the data

X_train, y_train = load_mnist('..\mnist', kind='train')
print('X_train Rows: %d, columns: %d' % (X_train.shape[0], X_train.shape[1]))  # X_train=60000x784
print('y_train.shape: ', y_train.shape)  # y_train=60000
X_test, y_test = load_mnist('mnist', kind='t10k')  # X_test=10000x784
print('X_test Rows: %d, columns: %d' % (X_test.shape[0], X_test.shape[1]))

X_train2 = X_train.copy()
X_train2 = X_train2.reshape(60000, 28, 28)
print('X_train2.shape', X_train2.shape)
print('X_train2[0]=', X_train2[0])

X_train = X_train.astype(theano.config.floatX)
X_test = X_test.astype(theano.config.floatX)
y_train_ohe = np_utils.to_categorical(y_train)
print("y_train_ohe.shape=", y_train_ohe.shape)
print("y_train_ohe[0:20]=", y_train_ohe[0:20])

for i in range(100):
    plt.subplot(10, 10, i + 1), plt.imshow(X_train2[i], cmap='gray')
plt.show()