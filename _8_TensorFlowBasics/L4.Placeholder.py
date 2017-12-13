# ========================================================================= #
#                            Placeholder 传入值                             #
#                                                                           #
#                                                                          #
# ========================================================================= #

import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    import tensorflow as tf

    # # 在 Tensorflow 中需要定义 placeholder 的 type ，一般为 float32 形式
    # input1 = tf.placeholder(tf.float32)
    # input2 = tf.placeholder(tf.float32)
    #
    # # mul = multiply 是将input1和input2 做乘法运算，并输出为 output
    # ouput = tf.multiply(input1, input2)
    #
    # with tf.Session() as sess:
    #     print(sess.run(ouput, feed_dict={input1: [7.], input2: [2.]}))

    input1 = tf.placeholder(tf.float32)
    input2 = tf.placeholder(tf.float32)

    mul = tf.multiply(input1, input2)  ## mul = multiply 是将input1和input2 做乘法运算，并输出为 output

    sess = tf.Session()

    print(sess.run(mul, feed_dict={input1: [7.0], input2: [12.0]}))

    print("#Use placeholder and feeddict and Matrix operation")
    x = tf.placeholder(tf.float32, shape=(4, 4)) #Accept float32, and a shape (4,4)

    rand_array = np.random.rand(4,4)

    y = tf.identity(x) #Tf Martix operation

    print(sess.run(y,feed_dict={x: rand_array}))

    print("## To see it in the tensorboard")

    merge = tf.summary.merge_all()
    writer = tf.summary.FileWriter("./tmp/variable_logs",sess.graph)

   #Run command tensorboard --logdir = _8_TensorFlowBasics/tmp