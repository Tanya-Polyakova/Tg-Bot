import telebot

bot = telebot.TeleBot('6482673854:AAEEJTL9JYHF16SqQIulMLPJYeje7ta0gDs')

@bot.message_handler(commands=['start'])
def main(message):

  bot.send_message(message.chat.id, "Привет!")
  
bot.polling(none_stop=True) #обязательная для работы бота часть


