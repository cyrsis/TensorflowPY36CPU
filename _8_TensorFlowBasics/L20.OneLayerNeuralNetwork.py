# ========================================================================= #
#            One Layer Nerual Network to make
#               The 4 flower attributes are
#                 1 sepal length
#                 2.sepal width
#                 3.pedal length
#                 4.pedal width
#           Goal: Predict (4) from 1-3                                      #
#                                                                          #
# ========================================================================= #

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.framework import ops
from sklearn.datasets import load_iris

ops.reset_default_graph()

sess = tf.Session()


#data
iris = load_iris()

x_vals = np.array([x[0:3] for x in iris.data]) #[[ 5.1  3.5  1.4]
y_vals = np.array([x[3] for x in iris.data]) #[0.2


#print(x_vals) #['tar' 'tar' 'DES' 'dat' 'fea']
#print(y_vals) #['g' 'g' 'C' 'a' 't']

#make result Reproduce
seed = 2
tf.set_random_seed(seed)
np.random.seed(seed)

#splite the data into train/set 80%/20%
train_indice = np.random.choice(len(x_vals),round(len(x_vals)*0.8),replace=False)
test_indice = np.array(list(set(range(len(x_vals)))-set(train_indice))) #set - set
x_vals_train = x_vals[train_indice]
x_vals_test = x_vals[test_indice]
y_vals_train = y_vals[train_indice]
y_vals_test = y_vals[test_indice]

#Place holder
x_data = tf.placeholder(shape=[None, 3], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

batch_size = 50

#Normalize by column (min-max norm)
def normalize_cols(m):
    col_max = m.max(axis=0)
    col_min = m.min(axis=0)
    return (m-col_min)/(col_max-col_min)

x_vals_train = np.nan_to_num(normalize_cols(x_vals_train))
x_vals_test = np.nan_to_num(normalize_cols(x_vals_test))



#hidden layuer_nodes

hidden_layer_nodes= 10
A1 = tf.Variable(tf.random_normal(shape=[3,hidden_layer_nodes])) #input to hidden nodes
b1 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes])) #one bias to each hidden nodes

A2 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes,1])) #hidden nodes -> 1 output
b2 = tf.Variable(tf.random_normal(shape=[1])) #1 bias for the output

#Mode Operation y = mx+b
hidden_output= tf.nn.relu(tf.add(tf.matmul(x_data,A1),b1))
final_output = tf.nn.relu(tf.add(tf.matmul(hidden_output,A2),b2))

#lose function
loss = tf.reduce_mean(tf.square(y_target- final_output))
#Optimizer
my_opt = tf.train.GradientDescentOptimizer(0.050)
train_step = my_opt.minimize(loss)

sess.run(tf.global_variables_initializer())

#train loop

loss_vec =[]
test_vec =[]

for i in range(500):
    rand_index = np.random.choice(len(x_vals_train),size=batch_size )
    rand_x = x_vals_train[rand_index]
    rand_y =np.transpose([y_vals_train[rand_index]])
    sess.run(train_step,feed_dict={x_data: rand_x, y_target: rand_y})

    temp_loss =sess.run(loss,feed_dict={x_data: rand_x, y_target: rand_y})
    loss_vec.append(np.square(temp_loss))
    
    test_temp_loss = sess.run(loss,feed_dict={x_data: x_vals_test, y_target: np.transpose([y_vals_test])})
    test_vec.append(np.square(test_temp_loss))

    if (i+1)%50 ==0:
        print('Generation: ' + str(i+1)+ ' . Loss = '+str(temp_loss))


plt.plot(loss_vec,'k--',label='Train loss')
plt.plot(test_vec,'r--',label='Test loss')
plt.title('Loss per Generation')
plt.legend(loc='upper right')
plt.xlabel('Generation')
plt.ylabel('Loss')
plt.show()