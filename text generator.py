import numpy as np
import random
import sys
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import RMSprop


text = "Your input text here"  # Replace with your text data
chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))
maxlen = 40  
step = 3  s

sentences = []  
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i : i + maxlen])
    next_chars.append(text[i + maxlen])


x = np.zeros((len(sentences), maxlen, len(chars), dtype=np.bool)
y = np.zeros((len(sentences), len(chars), dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars)))
model.add(Dense(len(chars), activation="softmax")


optimizer = RMSprop(learning_rate=0.01)
model.compile(loss="categorical_crossentropy", optimizer=optimizer)


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype("float64")
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)
for epoch in range(1, 60):
    print("Epoch", epoch)
    model.fit(x, y, batch_size=128, epochs=1)
    start_index = random.randint(0, len(text) - maxlen - 1)
    generated_text = text[start_index : start_index + maxlen]

    for temperature in [0.2, 0.5, 1.0, 1.2]:
        print("Temperature:", temperature)
        sys.stdout.write(generated_text)

        for i in range(400):
            sampled = np.zeros((1, maxlen, len(chars))
            for t, char in enumerate(generated_text):
                sampled[0, t, char_indices[char]] = 1.0

            preds = model.predict(sampled, verbose=0)[0]
            next_index = sample(preds, temperature)
            next_char = indices_char[next_index]

            generated_text += next_char
            generated_text = generated_text[1:]

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()
