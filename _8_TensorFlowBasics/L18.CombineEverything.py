# ========================================================================= #
#                  Working Everything together                              #
# :                    Binary Classification                                #
# ========================================================================= #
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from tensorflow.python.framework import ops

ops.reset_default_graph()

sess = tf.Session()

# 1. load Iris Data
# iris.target = {0,1,2} , WHERE '0' is setosa
# iris.data ~ [sepal.width, sepal.length,pedal.width,spedal.length] , we only use 3rd and 4th of the data set


iris = datasets.load_iris()
binary_target = np.array([1. if x == 0 else 0. for x in iris.target])
iris_2d = np.array([[x[2], x[3]] for x in iris.data])

# print(iris_2d)

batch_size = 20

# 2. Placeholder
x1_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
x2_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# 3. More Variable
# Since we are doing a linear model, we need to create A(Slop) and b(intercept)

A = tf.Variable(tf.random_normal(shape=[1, 1]))
b = tf.Variable(tf.random_normal(shape=[1, 1]))

# 4. Model Operation x1 = A * x2 +b
# Where line exactly on the line will satisfy 0 = x1 -(A*x2+b)
# .......... Above the line will satisfy 0>x1-(A*x2+b)
# .......... Above the line will satisfy 0<x1-(A*x2+b)

# model would be x1-(A*x2+_b)
# predictions would be prediction(x1,x2) = sign(x1-(A*x2+b))

my_mult = tf.matmul(x2_data, A)
my_add = tf.add(my_mult, A)
my_output = tf.subtract(x1_data, my_add)

# 5.Loss function
# Cataorical prediction (I.setosa or not), we use sigmoid cross entropy loss

xentropy = tf.nn.sigmoid_cross_entropy_with_logits(logits=my_output, labels=y_target)

# 6. Optimizing function

my_opt = tf.train.GradientDescentOptimizer(0.05)
train_step = my_opt.minimize(xentropy)

sess.run(tf.global_variables_initializer())

# 7. Training Steps

for i in range(1000):
    rand_index = np.random.choice(len(iris_2d), size=batch_size)
    rand_x = iris_2d[rand_index]
    rand_x1 = np.array([[x[0]] for x in rand_x])
    rand_x2 = np.array([[x[1]] for x in rand_x])
    rand_y = np.array([[y] for y in binary_target[rand_index]])
    sess.run(train_step,feed_dict={x1_data: rand_x1,x2_data:rand_x2, y_target:rand_y})
    if (i+1)%200==0:
        print("Steps #" + str(i+1)+ ' A ='+ str(sess.run(A)) + ', b =' +str(sess.run(b)))


# 8.Let 's plot them

[[slope]] = sess.run(A) #Pull out Slop/Intercept
[[intercept]] = sess.run(b)

x = np.linspace(0,3,num=50)
ablineValues =[]
for i in x:
    ablineValues.append(slope*i+intercept)

#plote the fitted line over the data
setosa_x = [a[1] for i, a in enumerate(iris_2d) if binary_target[i] ==1]
setosa_y = [a[0] for i, a in enumerate(iris_2d) if binary_target[i] ==1]
non_setosa_x = [a[1] for i, a in enumerate(iris_2d) if binary_target[i]==0]
non_setosa_y = [a[0] for i, a in enumerate(iris_2d) if binary_target[i]==0]

plt.plot(setosa_x,setosa_y,'rx',ms=10,mew=2, label='Setosa')
plt.plot(non_setosa_x,non_setosa_y,'ro',label='Non-Setosa')
plt.plot(x,ablineValues , 'b-')
plt.xlim(0.0,2.7)
plt.ylim(0.0,2.7)
plt.suptitle('Lienar Separator for I.setosa')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend(loc='lower right')
plt.show()

