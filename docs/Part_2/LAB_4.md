# Lab: Enhancing the Chatbot with Natural Language Processing (NLP) and Custom Logic Adapters

## Objective

By the end of this lab, you will be able to enhance your chatbot by integrating it with Natural Language Processing (NLP) capabilities using NLTK (Natural Language Toolkit) and creating custom logic adapters for more sophisticated responses.

### Tools Required

`Python 3.x`
`pip` (Python package installer)
Text editor or *Python IDE* (like *PyCharm*, *Jupyter notebook*, or *VS Code*)

## Steps

### Setup your Python Environment

Make sure Python and pip are installed on your system. You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

### Install Required Libraries

Install the necessary libraries using pip:

```python
pip install chatterbot flask twilio nltk
```

### Create a New Python File

Open your text editor or Python IDE and create a new Python file. You can name it `chatbot_nlp.py`.

### Import Required Libraries

At the top of your Python file, import the necessary libraries:

```python
import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
```

### Create a Custom Logic Adapter

Before creating the chatbot, let's create a custom logic adapter that uses NLTK's sentiment analysis to respond differently to positive and negative messages:

```python
class SentimentAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.sia = SentimentIntensityAnalyzer()

    def can_process(self, statement):
        return True

    def process(self, statement, additional_response_selection_parameters):
        sentiment = self.sia.polarity_scores(statement.text)
        confidence = abs(sentiment['compound'])
        if sentiment['compound'] > 0:
            response_statement = Statement(text="I'm glad you're feeling good!")
        else:
            response_statement = Statement(text="I'm sorry to hear that. How can I assist you further?")
        response_statement.confidence = confidence
        return response_statement
```

### Create and Train a ChatBot Instance with Custom Logic Adapter

Now, create an instance of ChatBot and train it, but also specify the custom logic adapter in the list of logic adapters:

```python
chatbot = ChatBot('Bot', logic_adapters=['chatterbot.logic.BestMatch', 'chatbot_nlp.SentimentAdapter'])
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
```

### Create a Flask App with Logging

Now, let's create a Flask app and define a route that will handle incoming messages. We'll also add logging statements to track incoming messages and the chatbot's responses:

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

### Run the Chatbot Service

Save your Python file and run it in the terminal/command prompt using the command `python chatbot_nlp.py`. You should now be able to interact with your chatbot through SMS, and the chatbot will respond differently to positive and negative messages.

**Note**: This lab assumes that you have a publicly accessible server where your Flask app is running. If you're working locally, you can use tools like `ngrok` to expose your local server to the internet.

### Further Reading

[Flask Documentation][flask]
[Twilio API Documentation][twilio]
[ChatterBot Documentation][chatterbot]
[NLTK Documentation][nltk]

*Happy coding!*

[flask]: https://flask.palletsprojects.com/en/2.3.x/ "Flask Documentation"
[twilio]: https://www.twilio.com/docs/quickstart "Twilio Documentation"
[chatterbot]: https://chatterbot.readthedocs.io/en/stable/ "Chatterbot Documentation"
[nltk]: https://www.nltk.org/ "Natural Language Toolkit"
