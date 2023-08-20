**Lab: Building a Chatbot with Rasa - Part 1: Data Sanitization**

**Objective:** By the end of this lab, you will be able to sanitize and prepare your data for training a chatbot using Rasa. This includes techniques such as data cleaning, intent and entity annotation, and creating conversation stories.

**Tools Required:**
- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- Rasa

**Steps:**

1. **Setup your Python Environment**
   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**
   - Install Rasa using pip:
     ```
     pip install rasa
     ```

3. **Create a New Rasa Project**
   - Open your terminal/command prompt and navigate to the directory where you want to create your Rasa project. Then, create a new Rasa project using the command:
     ```
     rasa init --no-prompt
     ```
   - This will create a new Rasa project with some example files that we'll modify in the next steps.

4. **Sanitize Your Data**
   - For this lab, we'll assume you have a dataset of user messages and their corresponding intents and entities. The first step is to sanitize this data by removing any irrelevant information, correcting typos, and standardizing the format.

5. **Annotate Intents and Entities**
   - Open the `nlu.yml` file in the `data` directory of your Rasa project. This is where you'll define the intents and entities for your chatbot.
   - For each unique intent in your data, add an entry under `intents:`. Then, for each user message corresponding to that intent, add an example under `nlu:`. If the message includes entities, annotate them in the format `[entity_value](entity_name)`. Here's an example:
     ```yaml
     version: "2.0"

     nlu:
     - intent: greet
       examples: |
         - Hi
         - Hello
         - Hey
     - intent: book_flight
       examples: |
         - I want to book a flight to [New York](location)
         - Can you help me book a flight to [Paris](location)?
     ```

6. **Create Conversation Stories**
   - Open the `stories.yml` file in the `data` directory of your Rasa project. This is where you'll define the conversation stories for your chatbot.
   - For each possible conversation flow in your data, add a story under `stories:`. A story consists of a sequence of user messages (intents and entities) and chatbot actions. Here's an example:
     ```yaml
     version: "2.0"

     stories:
     - story: book flight story
       steps:
       - intent: greet
       - action: utter_greet
       - intent: book_flight
         entities:
         - location: "New York"
       - action: utter_book_flight
     ```

**Note:** This is the first part of the Rasa chatbot lab. In the next parts, we will cover training a model and implementing the model.

**Further Reading:**
- [Rasa Documentation](https://rasa.com/docs/)
- [Rasa NLU Training Data Format](https://rasa.com/docs/rasa/training-data-format)
- [Rasa Stories Format](https://rasa.com/docs/rasa/stories)

**Lab: Building a Chatbot with Rasa - Part 2: Training the Model**

**Objective:** By the end of this lab, you will be able to train a chatbot model using Rasa. This includes defining the pipeline, training the NLU model, and training the dialogue management model.

**Tools Required:**
- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- Rasa

**Steps:**

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
     ```
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
     ```
     rasa train core
     ```
   - This will train the dialogue management model using the data in `stories.yml` and the domain in `domain.yml`. The trained model will be saved in the `models` directory.

**Note:** This is the second part of the Rasa chatbot lab. In the next part, we will cover implementing the model.

**Further Reading:**
- [Rasa Documentation](https://rasa.com/docs/)
- [Rasa Pipeline Configuration](https://rasa.com/docs/rasa/tuning-your-model)
- [Rasa Domain Format](https://rasa.com/docs/rasa/domain)

**Lab: Building a Chatbot with Rasa - Part 3: Implementing the Model**

**Objective:** By the end of this lab, you will be able to implement a chatbot model using Rasa. This includes loading the trained model, interacting with the chatbot in the command line, and evaluating the model's performance.

**Tools Required:**
- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)
- Rasa

**Steps:**

1. **Setup your Python Environment**
   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Load the Trained Model**
   - After training the NLU and dialogue management models in the previous parts of the lab, you should have a `.tar.gz` file in the `models` directory of your Rasa project. This file contains the trained model.
   - To load the trained model, you don't need to do anything special. Rasa will automatically use the latest model in the `models` directory.

3. **Interact with the Chatbot in the Command Line**
   - Now, let's interact with the chatbot. Open your terminal/command prompt, navigate to the root directory of your Rasa project, and run the following command:
     ```
     rasa shell
     ```
   - This will start a conversation with the chatbot in the command line. You can type your messages, and the chatbot will respond based on the trained model.

4. **Evaluate the Model's Performance**
   - Finally, let's evaluate the performance of the model. Rasa provides several commands to evaluate the NLU and dialogue management models.
   - To evaluate the NLU model, run the following command in your terminal/command prompt:
     ```
     rasa test nlu --nlu data/nlu.yml
     ```
   - This will evaluate the NLU model using the data in `nlu.yml` and print the evaluation results.
   - To evaluate the dialogue management model, run the following command:
     ```
     rasa test core --stories data/stories.yml
     ```
   - This will evaluate the dialogue management model using the data in `stories.yml` and print the evaluation results.

**Note:** This is the final part of the Rasa chatbot lab. You now have a functioning chatbot that you can interact with in the command line and evaluate its performance.

**Further Reading:**
- [Rasa Documentation](https://rasa.com/docs/)
- [Rasa Shell](https://rasa.com/docs/rasa/command-line-interface#rasa-shell)
- [Rasa Test](https://rasa.com/docs/rasa/testing-your-assistant)

Happy coding!