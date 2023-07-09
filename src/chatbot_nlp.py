"""
This module implements a chatbot application using Flask and ChatterBot. The application is configured to respond to incoming SMS messages via Twilio, using a custom sentiment analysis logic adapter.

The chatbot is trained using the English corpus from ChatterBot and utilizes a SentimentAdapter, which gauges the sentiment of a user's input and adjusts its responses accordingly.

Returns:
    _type_: _description_
"""

# pip install chatterbot flask twilio nltk

import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAdapter(LogicAdapter):
    """
    This is a custom LogicAdapter that uses sentiment analysis to influence the
    chatbot's responses.

    It uses the SentimentIntensityAnalyzer from the NLTK library to analyze the
    sentiment of the user's input. Depending on the sentiment score, it
    generates a positive or negative response.

    Args:
        chatbot (ChatBot): The ChatBot instance that this adapter is part of.
        **kwargs: Additional keyword arguments.
    """

    def __init__(self, chatbot, **kwargs):
        """
        Initializes the SentimentAdapter instance.

        It creates an instance of the SentimentIntensityAnalyzer, which will be
        used to perform sentiment analysis on the user's input.

        Args:
            chatbot (ChatBot): The ChatBot instance that this adapter is part
            of.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(chatbot, **kwargs)
        self.sia = SentimentIntensityAnalyzer()

    def can_process(self, statement):
        """
        Determines if the adapter can process a given statement. For this
        adapter, all statements can be processed.

        Args:
            statement (Statement): The statement to be processed.

        Returns:
            bool: Always returns True for this adapter as it can process all
            statements.
        """
        return True


    def process(self, statement, addl_resp_sel_para):
        """
        Processes a given statement using sentiment analysis.

        It performs sentiment analysis on the statement's text, and depending
        on the sentiment score, generates a positive or negative response.

        Args:
            statement (Statement): The statement to be processed.
            addl_resp_sel_para: Additional parameters for response selection,
            not used in this method.

        Returns:
            Statement: The response statement with its confidence score.
        """
        sentiment = self.sia.polarity_scores(statement.text)
        confidence = abs(sentiment["compound"])
        if sentiment["compound"] > 0:
            response_statement = Statement(text="I'm glad you're feeling good!")
        else:
            response_statement = Statement(
                text="I'm sorry to hear that. How can I assist you further?"
            )
        response_statement.confidence = confidence
        return response_statement

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    """
    Flask route that responds to incoming POST requests with a chatbot response.

    It retrieves the user's message from the request, passes it to the chatbot
    for processing, and returns the chatbot's response in a Twilio-compatible
    format.

    Returns:
        str: The chatbot's response in a Twilio-compatible format.
    """
    # Get the message the user sent our Twilio number
    user_message = request.values.get("Body", None)
    logging.info(f"Received user message: {user_message}")

    # Get a response from the chatbot
    response = str(chatbot.get_response(user_message))
    logging.info(f"Chatbot response: {response}")

    # Create a Twilio response object to be able to send a reply back (as an
    # SMS)
    twilio_response = MessagingResponse()
    twilio_response.message(response)

    return str(twilio_response)


chatbot = ChatBot(
    "Bot", logic_adapters=["chatterbot.logic.BestMatch",
                           "chatbot_nlp.SentimentAdapter"]
)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

if __name__ == "__main__":
    app.run(debug=True)
