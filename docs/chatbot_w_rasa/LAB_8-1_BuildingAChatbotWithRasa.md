# Lab: Building a Chatbot with Rasa

## Part 1: Data Sanitization

### **Objective:**

By the end of this lab, you will be able to sanitize and prepare your data for training a chatbot using Rasa. This includes techniques such as data cleaning, intent and entity annotation, and creating conversation stories.

### **Tools Required:**

- `Python 3.x`
- `pip` (Python package installer)
- Text editor or **Python IDE** (like _PyCharm_, _Jupyter notebook_, or _VS Code_)
- `Rasa`

## **Steps:**

1. **Setup your Python Environment**

   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**

   - Install Rasa using pip:

     ```bash
     pip install rasa
     ```

3. **Create a New Rasa Project**

   - Open your terminal/command prompt and navigate to the directory where you want to create your Rasa project. Then, create a new Rasa project using the command:

   ```bash
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

### **Further Reading:**

- [Rasa Documentation](https://rasa.com/docs/)
- [Rasa NLU Training Data Format](https://rasa.com/docs/rasa/training-data-format)
- [Rasa Stories Format](https://rasa.com/docs/rasa/stories)

Happy coding!
