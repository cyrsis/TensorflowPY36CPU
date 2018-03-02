import numpy as np
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.datasets import mnist
import matplotlib.pyplot as plt

(X_train, _), (X_test, _) = mnist.load_data()

X_train = X_train.astype('float32') / 255.
X_test = X_test.astype('float32') / 255.

X_train = np.reshape(X_train, (len(X_train), 28, 28, 1))
X_test = np.reshape(X_test, (len(X_test), 28, 28, 1))

noise_factor = 0.4
X_train_noise = X_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=X_train.shape)
X_test_noise = X_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=X_test.shape)

X_train_noise = np.clip(X_train_noise, 0., 1.)
X_test_noise = np.clip(X_test_noise, 0., 1.)

input_layer = Input(shape=(28, 28, 1))

# encoder
encoding_layer1 = Conv2D(32, (3, 3), activation='relu', padding='same')(input_layer)
max_pool_1 = MaxPooling2D((2, 2), padding='same')(encoding_layer1)
encoding_layer2 = Conv2D(64, (3, 3), activation='relu', padding='same')(max_pool_1)
max_pool_2 = MaxPooling2D((2, 2), padding='same')(encoding_layer2)

# decoder
decoding_layer1 = Conv2D(64, (3, 3), activation='relu', padding='same')(max_pool_2)
upsampling_layer1 = UpSampling2D((2, 2))(decoding_layer1)
decoding_layer2 = Conv2D(32, (3, 3), activation='relu', padding='same')(upsampling_layer1)
upsampling_layer2 = UpSampling2D((2, 2))(decoding_layer2)

output_decoding_layer = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(upsampling_layer2)

autoencoder = Model(input_layer, output_decoding_layer)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

autoencoder.fit(X_train_noise, X_train, epochs=10, batch_size=128, shuffle=True, validation_split=0.15)

output_images = autoencoder.predict(X_test_noise)

for i in range(1, 5):
    plt.figure(figsize=(1, 1))
    plt.imshow(X_test_noise[i].reshape(28, 28))
    plt.show()
    plt.figure(figsize=(1, 1))
    plt.imshow(output_images[i].reshape(28, 28))
    plt.show()
