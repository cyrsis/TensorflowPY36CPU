# ========================================================================= #
#                        l2 - 因为 product 不是直接计算的步骤,
#                                                                            #
#       所以我们会要使用 Session 来激活 product 并得到计算结果.
#        有两种形式使用会话控制 Session                                      #
#                                                                           #
# ========================================================================= #

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

# 2 2D martix

if __name__ == '__main__':
    martix1 = tf.constant([[3, 3]])
    martix2 = tf.constant([[2], [2]])

    product = tf.matmul(martix1, martix2)
    print(product)  # Tensor("MatMul:0", shape=(1, 1), dtype=int32)

    # Nothing happen

    # The calculate button on your keyboard

    # method 1
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    result = sess.run(product)

    print(result)

    sess.close()

    # method  2 (Without Close Session)
    with tf.Session() as sess:
        result2 = sess.run(product)
        print(result2)
