"""
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""


import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage import SQLStorageAdapter

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

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
