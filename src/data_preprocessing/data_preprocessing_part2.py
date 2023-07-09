from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def tokenize_text(texts, num_words):
    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    return sequences, tokenizer

def pad_sequences(sequences, maxlen):
    return pad_sequences(sequences, maxlen=maxlen)

texts = ["This is the first sentence.", "And this is another one.", "Can we try a third sentence?"]

sequences, tokenizer = tokenize_text(texts, num_words=100)
print(sequences)  # Output: [[1, 2, 3, 4, 5], [6, 1, 2, 7, 8], [9, 10, 11, 12, 4, 5]]

padded_sequences = pad_sequences(sequences, maxlen=10)
print(padded_sequences)  # Output: [[0 0 0 0 0 1 2 3 4 5], [0 0 0 0 0 6 1 2 7 8], [0 0 0 0 9 10 11 12 4 5]]
