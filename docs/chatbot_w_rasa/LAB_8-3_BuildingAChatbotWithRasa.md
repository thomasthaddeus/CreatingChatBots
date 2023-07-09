# Lab: Building a Chatbot with Rasa

## Part 3: Implementing the Model

### **Objective:**

By the end of this lab, you will be able to implement a chatbot model using Rasa. This includes loading the trained model, interacting with the chatbot in the command line, and evaluating the model's performance.

### **Tools Required:**

- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- Rasa

## **Steps:**

1. **Setup your Python Environment**

   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Load the Trained Model**

   - After training the NLU and dialogue management models in the previous parts of the lab, you should have a `.tar.gz` file in the `models` directory of your Rasa project. This file contains the trained model.
   - To load the trained model, you don't need to do anything special. Rasa will automatically use the latest model in the `models` directory.

3. **Interact with the Chatbot in the Command Line**

   - Now, let's interact with the chatbot. Open your terminal/command prompt, navigate to the root directory of your Rasa project, and run the following command:

   ```bash
   rasa shell
   ```

   - This will start a conversation with the chatbot in the command line. You can type your messages, and the chatbot will respond based on the trained model.

4. **Evaluate the Model's Performance**
   - Finally, let's evaluate the performance of the model. Rasa provides several commands to evaluate the NLU and dialogue management models.
   - To evaluate the NLU model, run the following command in your terminal/command prompt:

   ```bash
   rasa test nlu --nlu data/nlu.yml
   ```

   - This will evaluate the NLU model using the data in `nlu.yml` and print the evaluation results.
   - To evaluate the dialogue management model, run the following command:

   ```bash
   rasa test core --stories data/stories.yml
   ```

   - This will evaluate the dialogue management model using the data in `stories.yml` and print the evaluation results.

**Note:** This is the final part of the Rasa chatbot lab. You now have a functioning chatbot that you can interact with in the command line and evaluate its performance.

**Further Reading:**

- [Rasa Documentation](https://rasa.com/docs/)
- [Rasa Shell](https://rasa.com/docs/rasa/command-line-interface#rasa-shell)
- [Rasa Test](https://rasa.com/docs/rasa/testing-your-assistant)

Happy coding!
