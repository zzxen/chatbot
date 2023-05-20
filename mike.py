from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer , UbuntuCorpusTrainer
from gtts import gTTS

bot_token = "6077325357:AAGM3oXH01pumIGUGGDqrYm9W4UItUrBatg"
updater = Updater(bot_token , use_context = True)

keyboards = [
    [InlineKeyboardButton("About project" , callback_data = "about_project")],
    [InlineKeyboardButton("Test project" , callback_data = "start_project")],
    [InlineKeyboardButton("Developers" , callback_data = "developers")],
    [InlineKeyboardButton("Have fun with bot" , callback_data = "fun")],
]

def start(update : Update , context : CallbackContext):

    update.message.reply_text("Wellcome to Mike bot system. How can I help you ? " , reply_markup = InlineKeyboardMarkup(keyboards))

def chat(update : Update , context : CallbackContext):
    robot = ChatBot(
        "Mike" ,     
        logic_adapters=[
        'chatterbot.logic.BestMatch'
    ])
    trainer = UbuntuCorpusTrainer(robot)
    trainer.train()
    user_message = update.message.text
    bot_message = robot.get_response(user_message)
    voice_bot = gTTS(text = str(bot_message) , lang = "en" , slow = False)
    file_voice = voice_bot.save("bot.ogg")
    update.message.reply_voice(voice = open("bot.ogg" , "rb") , caption = f"{bot_message}" , reply_markup = InlineKeyboardMarkup(keyboards))

def button(update : Update , context : CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == "about_project":
        query.message.reply_text("This project will lunch soon with whitepaper. We want to create AI friend for world with voice cloner. Im trying to learn how I can anwser you.", reply_markup = InlineKeyboardMarkup(keyboards))
    
    elif query.data == "start_project":
        query.message.reply_text("Voice cloner will lunch soon." , reply_markup = InlineKeyboardMarkup(keyboards))
    
    elif query.data == "developers":
        query.message.reply_text("This project creator is @mmoeiinp.We listen you and you can contact from my owner.", reply_markup = InlineKeyboardMarkup(keyboards))
    
    elif query.data == "fun":
        query.message.reply_text("Just send me message with no / . I will anwser you soon.", reply_markup = InlineKeyboardMarkup(keyboards))

updater.dispatcher.add_handler(MessageHandler(Filters.text , chat))
updater.dispatcher.add_handler(CommandHandler("start" , start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()