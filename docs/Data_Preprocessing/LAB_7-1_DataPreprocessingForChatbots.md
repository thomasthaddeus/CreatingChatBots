# Lab: Data Preprocessing for Chatbots

## Part 1: Text Cleaning and Normalization

### **Objective:**

By the end of this lab, you will be able to clean and normalize text data, which is the first step in preparing your data for a chatbot. This includes techniques such as lowercasing, punctuation removal, stopword removal, and lemmatization.

### **Tools Required:**

- `Python 3.x`
- `pip` (Python package installer)
- Text editor or *Python IDE* (like *PyCharm*, *Jupyter notebook*, or *VS Code*)
- **NLTK** (Natural Language Toolkit)

## **Steps:**

1. **Setup your Python Environment**
   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**
   - Install the necessary libraries using pip:

    ```bash
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

### **Further Reading:**

- [NLTK Documentation](https://www.nltk.org/)
- [Python String Documentation](https://docs.python.org/3/library/string.html)

Happy coding!
