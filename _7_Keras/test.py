# ========================================================================= #
#           Keras RNN , Translation Example                                 #
#                                                                          #
# ========================================================================= #
import os
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import GRU, Input, Dense, TimeDistributed, Embedding, Bidirectional, RepeatVector
from keras.models import Model, Sequential
from keras.layers import Activation, LSTM
from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy


def load_text_file(path):
    input_file = os.path.join(path)
    with open(input_file, "r", encoding = "utf8") as f:
        data = f.read().split('\n')

    return data


english_sentences = load_text_file('K:\\TensorflowPY36CPU\\TensorflowPY36CPU\\_0_Working\\Section 5\\9217_05_code\\data\\en_data')
french_sentences = load_text_file('K:\\TensorflowPY36CPU\\TensorflowPY36CPU\\_0_Working\\Section 5\\9217_05_code\\data\\fr_data')

print('Dataset Loaded')


def tokenize(input):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(input)
    input_tokenized = tokenizer.texts_to_sequences(input)

    return input_tokenized, tokenizer


french_data_tokenized, french_tokenizer = tokenize(french_sentences)
english_data_tokenized, english_tokenizer = tokenize(english_sentences)

print(english_data_tokenized[1])
print(french_data_tokenized[1])


def pad(input, length=None):
    if length == None:
        length = max([len(seq) for seq in input])

    return pad_sequences(input, maxlen=length, padding='post')


french_data_padded = pad(french_data_tokenized)
french_data_padded = french_data_padded.reshape(*french_data_padded.shape, 1)
english_data_padded = pad(english_data_tokenized)

print(english_data_padded[1])
print(french_data_padded[1])


def advanced_model(input_shape, output_len, num_uniq_en_words, num_uniq_fr_words):
    model = Sequential()
    model.add(Embedding(num_uniq_en_words, 512, input_length=input_shape[1]))
    model.add(Bidirectional(LSTM(512, return_sequences=False)))
    model.add(RepeatVector(output_len))
    model.add(Bidirectional(LSTM(512, return_sequences=True)))
    model.add(TimeDistributed(Dense(num_uniq_fr_words)))
    model.add(Activation('softmax'))

    learning_rate = 0.002

    model.compile(loss=sparse_categorical_crossentropy,
                  optimizer=Adam(learning_rate),
                  metrics=['accuracy'])
    return model

model = advanced_model(english_data_padded.shape, french_data_padded.shape[1],
                       len(english_tokenizer.word_index), len(french_tokenizer.word_index))
model.fit(english_data_padded, french_data_padded, batch_size=1024, epochs=10, validation_split=0.2)

fr_id_to_word = {value: key for key, value in french_tokenizer.word_index.items()}
fr_id_to_word[0] = '|empty space|'

sentence = 'china is usually hot during february and it is usually wonderful in winter'
sentence = [english_tokenizer.word_index[word] for word in sentence.split()]
sentence = pad_sequences([sentence], maxlen=english_data_padded.shape[-1], padding='post')

sentences = np.array([sentence[0]])
predictions = model.predict(sentence)

print(' '.join([fr_id_to_word[np.argmax(x)] for x in predictions[0]]))