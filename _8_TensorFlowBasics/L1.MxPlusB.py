# ========================================================================= #
#             Tensorflow lesson #1                                                       #
#             y = A       *X  + B
#             y = Weights * x + biase
#             Where
#              y is the output
#              A & B are unknow and need to be computer                                  #
#             Therefore we need Tensorflow do some data flow Graph
#
#              张量有多种. 零阶张量为 纯量或标量 (scalar) 也就是一个数值. 比如 [1]
#              一阶张量为 向量 (vector), 比如 一维的 [1, 2, 3]
#              二阶张量为 矩阵 (matrix), 比如 二维的 [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#              以此类推, 还有 三阶 三维的 …
#
#
#              Tensorflow use following workflow
#              1. Input Data, Generate Data,setup the data-pipeline through placeholder
#              2. Feed data through computational graph
#              3. Evaluate output on lose(cost) function
#              4. use backpropgration to modify the variables
#              5. Repeat until stop condition
# ========================================================================= #

import tensorflow as tf
import numpy as np

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == '__main__':
    # 1.训练的数据
    x_data = np.random.rand(100).astype(np.float)
    y_data = x_data * 0.1 + 3

    # 2. 搭建模型
    Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    Biases = tf.Variable(tf.zeros([1]))
    y = Weights * x_data + Biases

    # 3. 计算误差 (Test to how wrong is my model)
    loss = tf.reduce_mean(tf.square(y - y_data))

    # 4. 传播误差
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)

    # 5. 训练

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    for step in range(201):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(Weights), sess.run(Biases))
