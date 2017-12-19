
import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

# 至此，我們來以下圖9計算一下使用了多少參數(w權重及b偏誤)，及多少連接到神經元。
# 原始圖像大小為32x32，使用6個不同的5x5 卷積核(filter)，產生了6個新feature map。
# 產生的新featue map大小為28x28，因為32-5+1=28
# 一個新feature map所使用參數數量為：5x5+1=26，也就是5x5個W權重及1個偏誤(bias)
# 6個新feature map所使用參數數量為：6x(5x5+1)=156個參數
# 那麼一個新feature map所須連接數量為：(5x5+1)x28x28=20384，也就是28x28個神經元各有(5x5+1)個權重及偏誤連接。
# 那麼6個新feature map所須連接數量為(5x5+1)x28x28x6=122304。
# 這個連接方式及數量其實便是LetNet-5第一個卷積層的狀況。
#
#     有關卷積(Convolutional)的操作也可以參閱底下一般影像處理領域的操作。其操作本質上便
# 是對影像作濾波(filter)


# mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# Parameters
learning_rate = 0.001
training_iters = 40000  #迭帶400000次
batch_size = 500 #使用minibatch方式
display_step = 100

# Network Parameters
n_input = 784  #原本MNIST數據集為1x784，會被reshape回28x28，當作原始輸入
n_classes = 10  # MNIST total classes (0-9 digits)
dropout = 0.6  #dropout = 0.75意義為：為了減少過度適合(Overfitting)的問題，應用了丟棄(dropout)正則化技術。
#意旨在神經網路中丟棄一些連接的單元(輸入，隱藏，和輸出)，決定丟棄那些神經元是隨機
#的也可以用機率決定。s

# tf Graph input
x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_prob = tf.placeholder(tf.float32)  # dropout (keep probability)


# Create model
def conv2d(img, filter, b):
    return tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(input=img,filter=filter, strides=[1, 1, 1, 1], padding='SAME'), b))


def max_pool(img, k):
    return tf.nn.max_pool(img,
                          ksize=[1, k, k, 1],
                          strides=[1, k, k, 1],
                          padding='SAME')
    #在Tensorflow 理定義padding='SAME'，如下程式在卷積層會自動使用padding成一樣尺寸。


# Store layers weight & bias

wc1 = tf.Variable(tf.random_normal([5, 5, 1, 32]))
# 5x5 conv, 1 input, 32 outputs
#32代表第1個卷積層要產生32個新的feature map

wc2 = tf.Variable(tf.random_normal([5, 5, 32, 64]))
# 5x5 conv, 32 inputs, 64 outputs
#5,5則是5x5的卷積核(filter權重)
#64代表第2個卷積層要產生64個新的feature map

wd1 = tf.Variable(tf.random_normal([7 * 7 * 64, 1024]))  # fully connected, 7*7*64 inputs, 1024 outputs

wout = tf.Variable(tf.random_normal([1024, n_classes]))  # 1024 inputs, 10 outputs (class prediction)
#1024則是全連接層的1024個神經元數量，n_classes=10，代表0-9的數字類別

bc1 = tf.Variable(tf.random_normal([32]))
bc2 = tf.Variable(tf.random_normal([64]))
bd1 = tf.Variable(tf.random_normal([1024]))
bout = tf.Variable(tf.random_normal([n_classes]))

# Construct model
_X = tf.reshape(x, shape=[-1, 28, 28, 1])

# Convolution Layer
# Computes 32 features using a 5x5 filter with ReLU activation.
conv1 = conv2d(_X, wc1, bc1)
# Max Pooling (down-sampling)
conv1 = max_pool(conv1, k=2)
# Apply Dropout
conv1 = tf.nn.dropout(conv1, keep_prob)
#定義第1層卷積層及pooling層並使用dropout正則化

# Convolution Layer
conv2 = conv2d(conv1, wc2, bc2)
# Max Pooling (down-sampling)
conv2 = max_pool(conv2, k=2)
# Apply Dropout
conv2 = tf.nn.dropout(conv2, keep_prob)
#定義第2層卷積層及pooling層並使用dropout正則化

# Fully connected layer
dense1 = tf.reshape(conv2, [-1, wd1.get_shape().as_list()[0]])  # Reshape conv2 output to fit dense layer input
dense1 = tf.nn.relu(tf.add(tf.matmul(dense1, wd1), bd1))  # Relu activation
dense1 = tf.nn.dropout(dense1,keep_prob=keep_prob)  # Apply Dropout
#定義F5層全連接層使用ReLu激勵函數及dropout正則化


# Output, class prediction
pred = tf.add(tf.matmul(dense1, wout), bout)

# pred = conv_net(x, weights, biases, keep_prob)
# Define loss and optimizer

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=pred))
#計算成本函數的方式並使用softmax_cross_entropy_with_logits
#注意，在Tensorflow R1.0.1版，注意這兩個參數(labels=y, logits=pred)的放法跟以前版本不同


optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
#使用AdamOptimizer最佳化。


# Evaluate model
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
# init = tf.initialize_all_variables()
init = tf.global_variables_initializer()
# Launch the graph
with tf.Session() as sess:
    sess.run(init)
    step = 1
    # Keep training until reach max iterations
    while step * batch_size < training_iters:
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        # Fit training using batch data
        sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys, keep_prob: dropout})
        if step % display_step == 0:
            # Calculate batch accuracy
            acc = sess.run(accuracy, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 1.})
            # Calculate batch loss
            loss = sess.run(cost, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 1.})
            print("Iter " + str(step * batch_size) + ", Minibatch Loss= " + "{:.6f}".format(
                loss) + ", Training Accuracy= " + "{:.5f}".format(acc))
        step += 1
    print("Optimization Finished!")
    # Calculate accuracy for 256 mnist test images
    print("Testing Accuracy:",
          sess.run(accuracy, feed_dict={x: mnist.test.images[:1024], y: mnist.test.labels[:1024], keep_prob: 1.}))
