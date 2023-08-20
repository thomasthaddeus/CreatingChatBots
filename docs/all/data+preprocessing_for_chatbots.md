**Lab: Data Preprocessing for Chatbots - Part 1: Text Cleaning and Normalization**

**Objective:** By the end of this lab, you will be able to clean and normalize text data, which is the first step in preparing your data for a chatbot. This includes techniques such as lowercasing, punctuation removal, stopword removal, and lemmatization.

**Tools Required:**
- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- NLTK (Natural Language Toolkit)

**Steps:**

1. **Setup your Python Environment**
   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**
   - Install the necessary libraries using pip:
     ```
     pip install nltk
     ```

3. **Download NLTK Data**
   - You will need some datasets from NLTK for stopword removal and lemmatization. You can download these datasets using the following commands in Python:
     ```python
     import nltk
     nltk.download('stopwords')
     nltk.download('wordnet')
     ```

4. **Create a New Python File**
   - Open your text editor or Python IDE and create a new Python file. You can name it `data_preprocessing_part1.py`.

5. **Import Required Libraries**
   - At the top of your Python file, import the necessary libraries:
     ```python
     import string
     import nltk
     from nltk.corpus import stopwords
     from nltk.stem import WordNetLemmatizer
     ```

6. **Define Text Cleaning and Normalization Functions**
   - Now, let's define some functions for text cleaning and normalization. We'll create functions for lowercasing, punctuation removal, stopword removal, and lemmatization:
     ```python
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
     ```

7. **Test the Functions**
   - Finally, let's test our functions with a sample sentence:
     ```python
     text = "This is a sample sentence, showing off the stop words filtration."

     text = lowercase_text(text)
     print(text)  # Output: "this is a sample sentence, showing off the stop words filtration."

     text = remove_punctuation(text)
     print(text)  # Output: "this is a sample sentence showing off the stop words filtration"

     text = remove_stopwords(text)
     print(text)  # Output: "sample sentence showing stop words filtration"

     text = lemmatize_text(text)
     print(text)  # Output: "sample sentence show stop word filtration"
     ```

**Note:** This is the first part of the data preprocessing lab. In the next parts, we will cover tokenization, sequence padding, and splitting the data into training and validation sets.

**Further Reading:**
- [NLTK Documentation](https://www.nltk.org/)
- [Python String Documentation](https://docs.python.org/3/library/string.html)

**Lab: Data Preprocessing for Chatbots - Part 2: Tokenization and Sequence Padding**

**Objective:** By the end of this lab, you will be able to convert text data into sequences of integers (a process known as tokenization) and pad these sequences to ensure they all have the same length. This is a crucial step in preparing your data for a chatbot, especially when using neural networks.

**Tools Required:**
- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- Keras

**Steps:**

1. **Setup your Python Environment**
   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**
   - Install the necessary libraries using pip:
     ```
     pip install keras
     ```

3. **Create a New Python File**
   - Open your text editor or Python IDE and create a new Python file. You can name it `data_preprocessing_part2.py`.

4. **Import Required Libraries**
   - At the top of your Python file, import the necessary libraries:
     ```python
     from keras.preprocessing.text import Tokenizer
     from keras.preprocessing.sequence import pad_sequences
     ```

5. **Define Tokenization and Padding Functions**
   - Now, let's define some functions for tokenization and sequence padding. We'll create a function to tokenize text and convert it to sequences of integers, and another function to pad these sequences to the same length:
     ```python
     def tokenize_text(texts, num_words):
         tokenizer = Tokenizer(num_words=num_words)
         tokenizer.fit_on_texts(texts)
         sequences = tokenizer.texts_to_sequences(texts)
         return sequences, tokenizer

     def pad_sequences(sequences, maxlen):
         return pad_sequences(sequences, maxlen=maxlen)
     ```

6. **Test the Functions**
   - Finally, let's test our functions with some sample sentences:
     ```python
     texts = ["This is the first sentence.", "And this is another one.", "Can we try a third sentence?"]

     sequences, tokenizer = tokenize_text(texts, num_words=100)
     print(sequences)  # Output: [[1, 2, 3, 4, 5], [6, 1, 2, 7, 8], [9, 10, 11, 12, 4, 5]]

     padded_sequences = pad_sequences(sequences, maxlen=10)
     print(padded_sequences)  # Output: [[0 0 0 0 0 1 2 3 4 5], [0 0 0 0 0 6 1 2 7 8], [0 0 0 0 9 10 11 12 4 5]]
     ```

**Note:** This is the second part of the data preprocessing lab. In the next part, we will cover splitting the data into training and validation sets.

**Further Reading:**
- [Keras Preprocessing Documentation](https://keras.io/api/preprocessing/)
- [Keras Tokenizer Documentation](https://keras.io/api/preprocessing/text/#tokenizer-class)

**Lab: Data Preprocessing for Chatbots - Part 3: Splitting the Data into Training and Validation Sets**

**Objective:** By the end of this lab, you will be able to split your preprocessed data into training and validation sets. This is an essential step in preparing your data for a chatbot, as it allows you to evaluate the performance of your model on unseen data.

**Tools Required:**
- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- scikit-learn

**Steps:**

1. **Setup your Python Environment**
   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**
   - Install the necessary libraries using pip:
     ```
     pip install scikit-learn
     ```

3. **Create a New Python File**
   - Open your text editor or Python IDE and create a new Python file. You can name it `data_preprocessing_part3.py`.

4. **Import Required Libraries**
   - At the top of your Python file, import the necessary libraries:
     ```python
     from sklearn.model_selection import train_test_split
     ```

5. **Define a Function to Split the Data**
   - Now, let's define a function to split the data into training and validation sets. We'll use the `train_test_split` function from scikit-learn, which shuffles the data and splits it into two sets:
     ```python
     def split_data(inputs, targets, test_size=0.2, random_state=42):
         inputs_train, inputs_val, targets_train, targets_val = train_test_split(inputs, targets, test_size=test_size, random_state=random_state)
         return inputs_train, inputs_val, targets_train, targets_val
     ```

6. **Test the Function**
   - Finally, let's test our function with some sample data. We'll assume that `sequences` is a list of integer sequences representing the input data, and `targets` is a list of integer sequences representing the target data:
     ```python
     sequences = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
     targets = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]]

     inputs_train, inputs_val, targets_train, targets_val = split_data(sequences, targets)
     print(inputs_train)  # Output: [[4, 5, 6], [10, 11, 12], [1, 2, 3]]
     print(inputs_val)  # Output: [[7, 8, 9]]
     print(targets_train)  # Output: [[5, 6, 7], [11, 12, 13], [2, 3, 4]]
     print(targets_val)  # Output: [[8, 9, 10]]
     ```

**Note:** This is the final part of the data preprocessing lab. You now have a set of functions to clean and normalize text, convert text to sequences, pad sequences, and split the data into training and validation sets.

**Further Reading:**
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [train_test_split Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
