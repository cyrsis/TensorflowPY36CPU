import tensorflow as tf
import numpy as np
import math

#   Create data in straight Python, create some size(x) and price(y) data points, using price = (m * size) + b.  
#        Here b is a price base based on other factors

#  generation some house sizes between 1000 and 3500 (typical sq ft of house)
num_house = 160
np.random.seed(42)
house_size = np.random.randint(low=1000, high=3500, size=num_house )

# Generate house prices from house size with a random noise added+.
np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(low=20000, high=70000, size=num_house)  

# you need to normalize values to prevent under/overflows.
def normalize(array):
    return (array - array.mean()) / array.std()

# 1. Get Data
# Split the data into training and testing, and normalized the data 

# define number of training samples, 0.7 = 70%.  We can take the first 70% since the values are randomized
num_train_samples = math.floor(num_house * 0.7)

# define training data
train_house_size = np.asarray(house_size[:num_train_samples])
train_price = np.asanyarray(house_price[:num_train_samples:])

train_house_size_norm = normalize(train_house_size)
train_price_norm = normalize(train_price)

# define test data
test_house_size = np.array(house_size[num_train_samples:])
test_house_price = np.array(house_price[num_train_samples:])

test_house_size_norm = normalize(test_house_size)
test_house_price_norm = normalize(test_house_price)


#  Set up the TensorFlow placeholders that get updated as we descend down the gradient
#n_samples = train_X.shape[0]
# tf Graph Input
house_size = tf.placeholder("float", name="house_size")
price = tf.placeholder("float", name="price")

# Define the variables holding the size_factor and price we set during training.  
# We initialize them to some random values based on the normal distribution.
size_factor = tf.Variable(np.random.randn(), name="size_factor")
price_offset = tf.Variable(np.random.randn(), name="price_offset")

# 2. Define the operations for the predicting values - predicted price = (size_factor * house_size ) + price_offset
#  Notice, the use of the tensorflow add and mul functions.  These add the operations to the computation graph,
#  AND the tensorflow methods understand how to deal with Tensors.  Therefore do not try to use numpy or other library 
#  methods.
price_pred = tf.add(tf.multiply(size_factor, house_size), price_offset)

# 3. Define the Loss Function (how much error) - Mean squared error
cost = tf.reduce_sum(tf.pow(price_pred-price, 2))/(2*num_train_samples)

# Optimizer learning rate.  The size of the steps down the gradient
learning_rate = 0.1

# 4. define a Gradient descent optimizer that will minimize the loss defined in the operation "cost".
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()


# 5. Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # set how often to display training progress and number of training iterations
    display_every = 2
    num_training_iter = 50

    # keep iterating the training data
    for iteration in range(num_training_iter):
        # Fit all training data
        for (x, y) in zip(train_house_size_norm, train_price_norm):
            sess.run(optimizer, feed_dict={house_size: x, price: y})

        # Display current status
        if (iteration + 1) % display_every == 0:
            c = sess.run(cost, feed_dict={house_size: train_house_size_norm, price:train_price_norm})
            print("iteration #:", '%04d' % (iteration + 1), "cost=", "{:.9f}".format(c), \
                "size_factor=", sess.run(size_factor), "price_offset=", sess.run(price_offset))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={house_size: train_house_size_norm, price: train_price_norm})
    print("Trained cost=", training_cost, "size_factor=", sess.run(size_factor), "price_offset=", sess.run(price_offset), '\n')