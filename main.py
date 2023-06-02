import telebot

bot = telebot.TeleBot('5885143732:AAFoAMITlbkmlQzUEFc0BXMWiAmTDq5av3Y')

@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

bot.polling(none_stop=True)
