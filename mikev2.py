import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = telebot.TeleBot("6077325357:AAGM3oXH01pumIGUGGDqrYm9W4UItUrBatg")



def chat(message):
    user = message.text
    robot = ChatBot("Mike")
    trainer = ChatterBotCorpusTrainer(robot)
    trainer.train("chatterbot.corpus.english.conversations")
    bot.send_message(message.from_user.id , f"{robot.get_response(user)}")

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.infinity_polling()