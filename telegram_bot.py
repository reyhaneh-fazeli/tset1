from telegram.ext import *
import khayyam
API_KEY = "7463383952:AAGby0rfqK9rcexbuLXdEJDSFCLYb3TsXc4"
print("Bot started!")

def start_command (update , context) :
    return update.message.reply_text ("جونم؟")

def hlep_command (update , context) :
    return update.message.reply_text ("کیان")
   

def message (update , context) :
    txt = str (update.message.text).lower()

    if txt in ("زمان" , "چندمه" , "امروز") :
        res = khayyam.JalaliDatetime.today().strftime(("%A %d %B %Y"))

    else :
        res = "نمیدونم"
    update.message.reply_text(res)


updater = Updater("7463383952:AAGby0rfqK9rcexbuLXdEJDSFCLYb3TsXc4" , use_ = True)
dp =updater.initialize()

dp.add_handler (CommandHandler ("start" , start_command))
dp.add_handler (CommandHandler ("help" , hlep_command))
dp.add_handler (MessageHandler (filters.text, message ))

updater.start_polling(5)
updater.idle()