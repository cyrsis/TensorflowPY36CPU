# ========================================================================= #
# CNN有三個主要的特點。
#
# 1.感知區域(Receptive field)：可採用3維的圖像資料(width，height，depth)與神經元連接方式，
#     實際上也可以直接採用2維的圖像資料，但隱含層內部的神經元只與原本圖像的某一小塊
#     區域做連結。該區塊我們稱之為感知區域(Receptive field)。
#
# 2.局部連結採樣(Local connectivity)：根據上述感知區域(Receptive field)的概念，CNN使用過濾
#   器(filters)增強與該局部圖形空間的相關性，然後堆疊許多這樣子的層，可以達到非線性
#    濾波的功能，且擴及全域，也就是允許網路架構從原圖小區塊的較好的特徵值代表性，組
#    合後變成大區塊的特徵值代表性。
#
# 3.共享權重(Shared weights)：使用的過濾器(filters)是可以重複使用的，當在原始圖像產生一
#     特徵圖(Feature Map)時，其權重向量(weights vector)及偏誤(bias)是共用的。這樣可以確保
#     在該卷積層所使用的神經元會偵測相同的特徵。並且即使圖像位置或是有旋轉的狀態，
#     仍然可以被偵測。
#
#     這三個特點使得CNN在圖像辨識上有更好的效果。在實際操作上的三個基礎分別是：
#     區域感知域(Local Receptive field)，卷積(Convolutional )，池化(pooling)。
#     我們可以從下面圖形化的實際操作來理解它的意思。
# :                                                     #
# ========================================================================= #
import tensorflow as tf
import numpy as np
#import mnist_data 

batch_size = 128
test_size = 256
img_size = 28
num_classes = 10

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))


def model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden):

    conv1 = tf.nn.conv2d(X, w,\
                         strides=[1, 1, 1, 1],\
                         padding='SAME')

    conv1_a = tf.nn.relu(conv1)
    conv1 = tf.nn.max_pool(conv1_a, ksize=[1, 2, 2, 1]\
                        ,strides=[1, 2, 2, 1],\
                        padding='SAME')
    conv1 = tf.nn.dropout(conv1, p_keep_conv)

    conv2 = tf.nn.conv2d(conv1, w2,\
                         strides=[1, 1, 1, 1],\
                         padding='SAME')
    conv2_a = tf.nn.relu(conv2)
    conv2 = tf.nn.max_pool(conv2_a, ksize=[1, 2, 2, 1],\
                        strides=[1, 2, 2, 1],\
                        padding='SAME')
    conv2 = tf.nn.dropout(conv2, p_keep_conv)

    conv3=tf.nn.conv2d(conv2, w3,\
                       strides=[1, 1, 1, 1]\
                       ,padding='SAME')

    conv3 = tf.nn.relu(conv3)


    FC_layer = tf.nn.max_pool(conv3, ksize=[1, 2, 2, 1],\
                        strides=[1, 2, 2, 1],\
                        padding='SAME')
    
    FC_layer = tf.reshape(FC_layer, [-1, w4.get_shape().as_list()[0]])    
    FC_layer = tf.nn.dropout(FC_layer, p_keep_conv)


    output_layer = tf.nn.relu(tf.matmul(FC_layer, w4))
    output_layer = tf.nn.dropout(output_layer, p_keep_hidden)

    result = tf.matmul(output_layer, w_o)
    return result


#mnist = mnist_data.read_data_sets("ata/")
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

trX, trY, teX, teY = mnist.train.images,\
                     mnist.train.labels, \
                     mnist.test.images, \
                     mnist.test.labels

trX = trX.reshape(-1, img_size, img_size, 1)  # 28x28x1 input img
teX = teX.reshape(-1, img_size, img_size, 1)  # 28x28x1 input img

X = tf.placeholder("float", [None, img_size, img_size, 1])
Y = tf.placeholder("float", [None, num_classes])

w = init_weights([3, 3, 1, 32])       # 3x3x1 conv, 32 outputs
w2 = init_weights([3, 3, 32, 64])     # 3x3x32 conv, 64 outputs
w3 = init_weights([3, 3, 64, 128])    # 3x3x32 conv, 128 outputs
w4 = init_weights([128 * 4 * 4, 625]) # FC 128 * 4 * 4 inputs, 625 outputs
w_o = init_weights([625, num_classes])         # FC 625 inputs, 10 outputs (labels)

p_keep_conv = tf.placeholder("float")
p_keep_hidden = tf.placeholder("float")
py_x = model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden)

Y_ = tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y)
cost = tf.reduce_mean(Y_)
optimizer  = tf.train.\
           RMSPropOptimizer(0.001, 0.9).minimize(cost)
predict_op = tf.argmax(py_x, 1)

with tf.Session() as sess:
    #tf.initialize_all_variables().run()
    tf.global_variables_initializer().run()
    for i in range(100):
        training_batch = \
                       zip(range(0, len(trX), \
                                 batch_size),
                             range(batch_size, \
                                   len(trX)+1, \
                                   batch_size))
        for start, end in training_batch:
            sess.run(optimizer, feed_dict={X: trX[start:end],\
                                          Y: trY[start:end],\
                                          p_keep_conv: 0.8,\
                                          p_keep_hidden: 0.5})

        test_indices = np.arange(len(teX))# Get A Test Batch
        np.random.shuffle(test_indices)
        test_indices = test_indices[0:test_size]

        print(i, np.mean(np.argmax(teY[test_indices], axis=1) ==\
                         sess.run\
                         (predict_op,\
                          feed_dict={X: teX[test_indices],\
                                     Y: teY[test_indices], \
                                     p_keep_conv: 1.0,\
                                     p_keep_hidden: 1.0})))

"""
Successfully downloaded train-images-idx3-ubyte.gz 9912422 bytes.
Successfully extracted to train-images-idx3-ubyte.mnist 9912422 bytes.
Loading ata/train-images-idx3-ubyte.mnist
Successfully downloaded train-labels-idx1-ubyte.gz 28881 bytes.
Successfully extracted to train-labels-idx1-ubyte.mnist 28881 bytes.
Loading ata/train-labels-idx1-ubyte.mnist
Successfully downloaded t10k-images-idx3-ubyte.gz 1648877 bytes.
Successfully extracted to t10k-images-idx3-ubyte.mnist 1648877 bytes.
Loading ata/t10k-images-idx3-ubyte.mnist
Successfully downloaded t10k-labels-idx1-ubyte.gz 4542 bytes.
Successfully extracted to t10k-labels-idx1-ubyte.mnist 4542 bytes.
Loading ata/t10k-labels-idx1-ubyte.mnist
(0, 0.95703125)
(1, 0.98046875)
(2, 0.9921875)
(3, 0.99609375)
(4, 0.99609375)
(5, 0.98828125)
(6, 0.99609375)
(7, 0.99609375)
(8, 0.98828125)
(9, 0.98046875)
(10, 0.99609375)
(11, 1.0)
(12, 0.9921875)
(13, 0.98046875)
(14, 0.98828125)
(15, 0.9921875)
(16, 0.9921875)
(17, 0.9921875)
(18, 0.9921875)
(19, 1.0)
(20, 0.98828125)
(21, 0.99609375)
(22, 0.98828125)
(23, 1.0)
(24, 0.9921875)
(25, 0.99609375)
(26, 0.99609375)
(27, 0.98828125)
(28, 0.98828125)
(29, 0.9921875)
(30, 0.99609375)
(31, 0.9921875)
(32, 0.99609375)
(33, 1.0)
(34, 0.99609375)
(35, 1.0)
(36, 0.9921875)
(37, 1.0)
(38, 0.99609375)
(39, 0.99609375)
(40, 0.99609375)
(41, 0.9921875)
(42, 0.98828125)
(43, 0.9921875)
(44, 0.9921875)
(45, 0.9921875)
(46, 0.9921875)
(47, 0.98828125)
(48, 0.99609375)
(49, 0.99609375)
(50, 1.0)
(51, 0.98046875)
(52, 0.99609375)
(53, 0.98828125)
(54, 0.99609375)
(55, 0.9921875)
(56, 0.99609375)
(57, 0.9921875)
(58, 0.98828125)
(59, 0.99609375)
(60, 0.99609375)
(61, 0.98828125)
(62, 1.0)
(63, 0.98828125)
(64, 0.98828125)
(65, 0.98828125)
(66, 1.0)
(67, 0.99609375)
(68, 1.0)
(69, 1.0)
(70, 0.9921875)
(71, 0.99609375)
(72, 0.984375)
(73, 0.9921875)
(74, 0.98828125)
(75, 0.99609375)
(76, 1.0)
(77, 0.9921875)
(78, 0.984375)
(79, 1.0)
(80, 0.9921875)
(81, 0.9921875)
(82, 0.99609375)
(83, 1.0)
(84, 0.98828125)
(85, 0.98828125)
(86, 0.99609375)
(87, 1.0)
(88, 0.99609375)
"""
