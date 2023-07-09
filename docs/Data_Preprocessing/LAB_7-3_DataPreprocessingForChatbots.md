# Lab: Data Preprocessing for Chatbots

## Part 3: Splitting the Data into Training and Validation Sets

## **Objective:**

By the end of this lab, you will be able to split your preprocessed data into training and validation sets. This is an essential step in preparing your data for a chatbot, as it allows you to evaluate the performance of your model on unseen data.

### **Tools Required:**

- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- scikit-learn

## **Steps:**

1. **Setup your Python Environment**

   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**

   - Install the necessary libraries using pip:

    ```python
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

Happy coding!
