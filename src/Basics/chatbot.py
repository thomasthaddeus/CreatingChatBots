"""chatbot.py

_summary_

_extended_summary_
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

print('Hello, I am Bot. How can I assist you? If you want to exit, type quit.')
while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.get_response(user_input)
    print("Bot: ", response)
