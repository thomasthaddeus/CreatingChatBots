"""data_prep.py
This is the first part of a three part series on cleaning data with chatbots
"""


#!pip install nltk

import nltk
nltk.download('stopwords')
nltk.download('wordnet')


import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def lowercase_text(text):
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

text = "This is a sample sentence, showing off the stop words filtration."

text = lowercase_text(text)
print(text)  # Output: "this is a sample sentence, showing off the stop words filtration."

text = remove_punctuation(text)
print(text)  # Output: "this is a sample sentence showing off the stop words filtration"

text = remove_stopwords(text)
print(text)  # Output: "sample sentence showing stop words filtration"

text = lemmatize_text(text)
print(text)  # Output: "sample sentence show stop word filtration"
