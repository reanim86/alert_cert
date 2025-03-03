import configparser
import telebot

def send_mes_telebot(messege, chat):
    """
    Отправка сообщения в телеграм с помощью бота
    :param messege: количество строк в таблице БД
    :param chat: id чата
    """
    bot = telebot.TeleBot(token)
    bot.send_message(chat, messege)
    return

config = configparser.ConfigParser()
config.read('settings.ini')
token = config['Tg']['token'] #Прописать токен