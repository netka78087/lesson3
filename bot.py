from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater("662345430:AAFKTulWdNi7uLVirgsh6BZ3luZsv0yqTkE", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
    # Импортируем нужные компоненты

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def get_constellation(bot, update):
    user_text = update.message.text
    planet_name = user_text.split(' ')[1]
    if planet_name == 'Mars':
        date = datetime.datetime.now()
        planet = ephem.Mars(date.strftime('%Y/%m/%d'))
    print(ephem.constellation(planet))
    update.message.reply_text(ephem.constellation(planet))

main()