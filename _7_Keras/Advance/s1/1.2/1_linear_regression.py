import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import Adam

BATCH_SIZE = 128


# Y = 3X + 10

def get_data():
    x_ = np.random.standard_normal(BATCH_SIZE)
    y_ = 3 * x_ + 10
    return x_, y_


model = Sequential()
model.add(Dense(1, input_shape=(1,), activation=None))
model.add(Dense(1, input_shape=(1,), activation=None))

model.add(Dense(1, input_shape=(1,), activation=None))
model.summary()
model.summary()

adam = Adam(lr=0.5)
adam = Adam(lr=0.5)

model.compile(loss='mse',
              optimizer=adam)

x, y = get_data()
x_t, y_t = get_data()

# train network
NUM_EPOCHS = 20
BATCH_SIZE = 10

history = model.fit(x, y,
                    batch_size=BATCH_SIZE,
                    epochs=100,
                    verbose=1,
                    validation_data=(x_t, y_t))

print(model.get_weights())
