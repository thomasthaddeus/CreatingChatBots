
# Lab: Data Preprocessing for Chatbots

## Part 2: Tokenization and Sequence Padding

### **Objective:**

By the end of this lab, you will be able to convert text data into sequences of integers (a process known as tokenization) and pad these sequences to ensure they all have the same length. This is a crucial step in preparing your data for a chatbot, especially when using neural networks.

### **Tools Required:**

- `Python 3.x`
- `pip` (Python package installer)
- Text editor or Python IDE (like `PyCharm`, `Jupyter notebook`, or *VS Code*)
- `Keras`

## **Steps:**

1. **Setup your Python Environment**
   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**
   - Install the necessary libraries using pip:

    ```bash
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

### **Further Reading:**

- [Keras Preprocessing Documentation](https://keras.io/api/preprocessing/)
- [Keras Tokenizer Documentation](https://keras.io/api/preprocessing/text/#tokenizer-class)

Happy coding!
