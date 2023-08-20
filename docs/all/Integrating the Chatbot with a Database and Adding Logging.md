# **Lab: Integrating the Chatbot with a Database and Adding Logging**

**Objective:** By the end of this lab, you will be able to enhance your chatbot by integrating it with a SQLite database for storing conversation history and adding logging capabilities for better debugging and tracking.

**Tools Required:**
- Python 3.x
- pip (Python package installer)
- Text editor or Python IDE (like PyCharm, Jupyter notebook, or VS Code)

**Steps:**

1. **Setup your Python Environment**
   - Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

2. **Install Required Libraries**
   - Install the necessary libraries using pip:
     ```
     pip install chatterbot flask twilio
     ```

3. **Create a New Python File**
   - Open your text editor or Python IDE and create a new Python file. You can name it `chatbot_db.py`.

4. **Import Required Libraries**
   - At the top of your Python file, import the necessary libraries:
     ```python
     import logging
     from flask import Flask, request
     from twilio.twiml.messaging_response import MessagingResponse
     from chatterbot import ChatBot
     from chatterbot.trainers import ChatterBotCorpusTrainer
     from chatterbot.storage import SQLStorageAdapter
     ```

5. **Setup Logging**
   - Before creating the chatbot, set up logging so that we can track the chatbot's activities:
     ```python
     logging.basicConfig(level=logging.INFO)
     ```

6. **Create and Train a ChatBot Instance with SQL Storage**
   - This time, when creating the ChatBot instance, we'll specify a SQL storage adapter to store conversation history in a SQLite database:
     ```python
     chatbot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
     trainer = ChatterBotCorpusTrainer(chatbot)
     trainer.train("chatterbot.corpus.english")
     ```

7. **Create a Flask App with Logging**
   - Now, let's create a Flask app and define a route that will handle incoming messages. We'll also add logging statements to track incoming messages and the chatbot's responses:
     ```python
     app = Flask(__name__)

     @app.route("/sms", methods=['POST'])
     def sms_reply():
         # Get the message the user sent our Twilio number
         user_message = request.values.get('Body', None)
         logging.info(f"Received user message: {user_message}")

         # Get a response from the chatbot
         response = str(chatbot.get_response(user_message))
         logging.info(f"Chatbot response: {response}")

         # Create a Twilio response object to be able to send a reply back (as an SMS)
         twilio_response = MessagingResponse()
         twilio_response.message(response)

         return str(twilio_response)

     if __name__ == "__main__":
         app.run(debug=True)
     ```

8. **Run the Chatbot Service**
   - Save your Python file and run it in the terminal/command prompt using the command `python chatbot_db.py`. You should now be able to interact with your chatbot through SMS, and all conversation history will be stored in a SQLite database. You can also check the logs to see the flow of messages.

**Note:** This lab assumes that you have a publicly accessible server where your Flask app is running. If you're working locally, you can use tools like ngrok to expose your local server to the internet.

**Further Reading:**
- [Flask Documentation](https://flask.pallet

sprojects.com/en/2.0.x/)
- [Twilio API Documentation](https://www.twilio.com/docs/quickstart)
- [ChatterBot Documentation](https://chatterbot.readthedocs.io/en/stable/)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)

Happy coding!