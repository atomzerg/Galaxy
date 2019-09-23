import config
import requests
import telebot
import urllib.request
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    requests.get('https://serge-fashion.by/aktsii-i-skidki/atom.php?text='+message.text)
if __name__ == '__main__':
     bot.polling(none_stop=True)