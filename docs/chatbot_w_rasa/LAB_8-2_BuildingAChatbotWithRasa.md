# Lab: Building a Chatbot with Rasa

## Part 2: Training the Model

### **Objective:**

By the end of this lab, you will be able to train a chatbot model using Rasa. This includes defining the pipeline, training the NLU model, and training the dialogue management model.

### **Tools Required:**

- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- Rasa

## **Steps:**

1. **Setup your Python Environment**

   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Define the Pipeline**

   - Open the `config.yml` file in the root directory of your Rasa project. This is where you'll define the pipeline for your chatbot.
   - The pipeline specifies the sequence of processing steps that Rasa will use to train the NLU model. The choice of pipeline depends on your data and use case, but a common choice is the `supervised_embeddings` pipeline. Here's an example:

   ```yaml
   language: en
   pipeline: supervised_embeddings
   ```

3. **Train the NLU Model**

   - Now, let's train the NLU model. Open your terminal/command prompt, navigate to the root directory of your Rasa project, and run the following command:

   ```bash
   rasa train nlu
   ```

   - This will train the NLU model using the data in `nlu.yml` and the pipeline in `config.yml`. The trained model will be saved in the `models` directory.

4. **Define the Dialogue Management Model**

   - Open the `domain.yml` file in the root directory of your Rasa project. This is where you'll define the dialogue management model for your chatbot.
   - The dialogue management model specifies the intents, entities, slots, and actions that your chatbot can handle, as well as the templates for the chatbot's responses. Here's an example:

   ```yaml
   intents:
     - greet
     - book_flight

   entities:
     - location

   slots:
   location:
     type: text

   responses:
   utter_greet:
     - text: "Hello! How can I help you today?"

   utter_book_flight:
     - text: "Sure, I can help you book a flight. Where would you like to go?"

   actions:
     - utter_greet
     - utter_book_flight
   ```

5. **Train the Dialogue Management Model**

   - Finally, let's train the dialogue management model. Run the following command in your terminal/command prompt:

   ```bash
   rasa train core
   ```

   - This will train the dialogue management model using the data in `stories.yml` and the domain in `domain.yml`. The trained model will be saved in the `models` directory.

**Note:** This is the second part of the Rasa chatbot lab. In the next part, we will cover implementing the model.

### **Further Reading:**

- [Rasa Documentation](https://rasa.com/docs/)
- [Rasa Pipeline Configuration](https://rasa.com/docs/rasa/tuning-your-model)
- [Rasa Domain Format](https://rasa.com/docs/rasa/domain)

Happy coding!
