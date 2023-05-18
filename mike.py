from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer , ListTrainer

bot_token = "6077325357:AAGM3oXH01pumIGUGGDqrYm9W4UItUrBatg"
updater = Updater(bot_token , use_context = True)

keyboards = [
    InlineKeyboardButton("About project" , callback_data = "about_project"),
    InlineKeyboardButton("Test project" , callback_data = "start_project"),
    InlineKeyboardButton("Developers" , callback_data = "developers"),
    InlineKeyboardButton("Have fun with bot" , callback_data = "fun")
]

def start(update : Update , context : CallbackContext):
    update.message.reply_text("Wellcome to Mike bot system. How can I help you ? " , reply_markup = InlineKeyboardMarkup(keyboards))

def chat(update : Update , context : CallbackContext):
    robot = ChatBot("Mike")
    trainer = ChatterBotCorpusTrainer(robot)
    trainer.train("chatterbot.corpus.english.conversations")
    user_message = update.message.text
    update.message.reply_text(f"{robot.get_response(user_message)}" , reply_markup = keyboards)

def button(update : Update , context : CallbackContext) -> None:
    query = update.callback_query
    
    if query.data == "about_project":
        query.message.reply_text("Mike is first Telegram bot that change you favorite music sound to you sound.We on the test version and we will lunch soon." , reply_markup = InlineKeyboardMarkup(keyboards))

    elif query.data == "start_project":
        query.message.reply_text("We will lunch soon." , reply_markup = InlineKeyboardMarkup(keyboards))
    
    elif query.data == "developers":
        query.message.reply_text("You can contact us with this ID : @mmoeiinp" , reply_markup = InlineKeyboardMarkup(keyboards))
    
    elif query.data == "fun":
        query.message.reply_text("Just send me message, I will happy to anwser you" , reply_markup = InlineKeyboardMarkup(keyboards))
    
    else:
        query.message.reply_text("SO ? " , reply_markup = InlineKeyboardMarkup(keyboards))


updater.dispatcher.add_handler(MessageHandler(Filters.text , chat))
updater.dispatcher.add_handler("start" , start)
updater.dispatcher.add_handler(CallbackQueryHandler(button))