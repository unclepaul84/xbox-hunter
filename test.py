import os
import telegram

bot = telegram.Bot(token=os.getenv("TG_BOT_TOKEN"))

bot.send_message(text='Xbox found!', chat_id=-491453449)