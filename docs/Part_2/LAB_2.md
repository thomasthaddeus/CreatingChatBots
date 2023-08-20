# Lab 2: Enhancing the Chatbot with Service Frameworks

## Objective

By the end of this lab, you will be able to enhance your simple chatbot by integrating it with different service frameworks.

We will use the Flask web framework to create a web-based interface for our chatbot and Twilio API for SMS-based interaction.

### Tools Required

**Python 3.x**
**pip** (Python package installer)
Text editor or **Python IDE** (like *PyCharm*, *Jupyter notebook*, or *VS Code*)
Twilio account

## Steps

### Setup your Python Environment

Make sure Python and pip are installed on your system.

You can verify this by typing `python --version` and `pip --version` in your terminal/command prompt.

### Install Required Libraries

Install the necessary libraries using pip:

```python
pip install chatterbot flask twilio
```

### Create a New Python File

Open your text editor or Python IDE and create a new Python file. You can name it chatbot_service.py.

### Import Required Libraries

At the top of your Python file, import the necessary libraries:

```python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
```

### Create and Train a ChatBot Instance

This step is similar to the previous lab. Create an instance of ChatBot and train it:

```python
chatbot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
```

### Create a Flask App

Now, let's create a Flask app and define a route that will handle incoming messages:

```python
app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    # Get the message the user sent our Twilio number
    user_message = request.values.get('Body', None)

    # Get a response from the chatbot
    response = str(chatbot.get_response(user_message))

    # Create a Twilio response object to be able to send a reply back (as an SMS)
    twilio_response = MessagingResponse()
    twilio_response.message(response)

    return str(twilio_response)

if __name__ == "__main__":
    app.run(debug=True)
```

### Setup Twilio Webhook

Log in to your Twilio account, go to the console, and select your active phone number.

Under the messaging section, find the "*A Message Comes In*" field and set the webhook to the URL of your Flask app (e.g., <http://your-server.com/sms>).

Make sure the HTTP method is set to `POST`.

### Run the Chatbot Service

Save your Python file and run it in the terminal/command prompt using the command `python chatbot_service.py`. You should now be able to interact with your chatbot through SMS!

**Note**: This lab assumes that you have a publicly accessible server where your Flask app is running. If you're working locally, you can use tools like `ngrok` to expose your local server to the internet.

### Further Reading

[Flask Documentation][flask]
[Twilio API Documentation][twilio]
[ChatterBot Documentation][chatterbot]
[Python Official Documentation][python]

**Happy coding!**

[flask]: https://flask.palletsprojects.com/en/2.3.x/ "Latest Flask Documentation"
[twilio]: https://www.twilio.com/docs/quickstart "Twilio Docs for sending SMS messages"
[chatterbot]: https://chatterbot.readthedocs.io/en/stable/ "Chatterbot Documentation"
[python]: https://docs.python.org/3/ "Python3 Documentation"
