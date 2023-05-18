from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer , ListTrainer

bot = ChatBot("Mike")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

while True:
    user = input("ME : ")
    if user == "exit":
        break
    else:
        response = bot.get_response(user)
        print("BOT : {}".format(response))