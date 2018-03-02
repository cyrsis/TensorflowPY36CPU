import numpy as np
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train, _), (x_test, _) = mnist.load_data()



# display some images from the dataset
for i in range(5):
    plt.figure(figsize=(1, 1))
    plt.imshow(x_train[i])
    plt.show()

# reshape
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

noise_factor = 0.4
x_train_noise  = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape)
x_test_noise = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape)

x_train_noise = np.clip(x_train_noise, 0., 1.)
x_test_noise = np.clip(x_test_noise, 0., 1.)

for i in range(1,5):
    plt.figure(figsize=(1,1))
    plt.imshow(x_train_noise[i].reshape(28,28))
    plt.show()


input_layer = Input(shape=(28, 28, 1))

#encoder
encoding_layer1 = Conv2D(32, (3, 3), activation='relu', padding='same')(input_layer)
max_pool_1 = MaxPooling2D((2, 2), padding='same')(encoding_layer1)
encoding_layer2 = Conv2D(64, (3, 3), activation='relu', padding='same')(max_pool_1)
max_pool_2 = MaxPooling2D((2, 2), padding='same')(encoding_layer2)

#decoder
decoding_layer1 = Conv2D(64, (3, 3), activation='relu', padding='same')(max_pool_2)
upsampling_layer1 = UpSampling2D((2, 2))(decoding_layer1)
decoding_layer2 = Conv2D(32, (3, 3), activation='relu', padding='same')(upsampling_layer1)
upsampling_layer2 = UpSampling2D((2, 2))(decoding_layer2)

output_decoding_layer = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(upsampling_layer2)

autoencoder = Model(input_layer, output_decoding_layer)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

autoencoder.fit(x_train_noise, x_train, epochs=10, batch_size=128, shuffle=True, validation_split = 0.15)

output_images = autoencoder.predict(x_test_noise)

for i in range(1,5):
    plt.figure(figsize=(1,1))
    plt.imshow(x_test_noise[i].reshape(28,28))
    plt.show()
    plt.figure(figsize=(1,1))
    plt.imshow(output_images[i].reshape(28,28))
    plt.show()