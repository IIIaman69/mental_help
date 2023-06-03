import random
import telebot
from telebot import types


bot = telebot.TeleBot('5885143732:AAFoAMITlbkmlQzUEFc0BXMWiAmTDq5av3Y')
#TO_CHAT_ID = -1001980809298
with open('aforism.txt','r', encoding="utf-8") as aforism:
    aforism = aforism.readlines()

@bot.message_handler(commands=['start', 'hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Книги')
    btn2 = types.KeyboardButton('Почта для предложений')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Новый афоризм')
    btn4 = types.KeyboardButton('Консультация специалиста - 🚧')
    markup.row(btn3, btn4)
    btn5 = types.KeyboardButton('Наш сайт')
    markup.row(btn5)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def callback_message(message):
    if message.text == 'Книги':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Почта для предложений':
        bot.send_message(message.chat.id, 'Направляйте по этому адресу ваши пожелания, а также книги и статьи, '
                                          'которые морально или эмоционально помогли вам: 6moonwolf6@gmail.com')
    elif message.text == 'Новый афоризм':
        bot.send_message(message.chat.id, random.choice(aforism))
    elif message.text == 'Консультация специалиста - 🚧':
        bot.send_message(message.chat.id, '👷‍♂️ В данное время функция недоступна, но мы уже близки к ее настройке!')
    elif message.text == 'Наш сайт':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://students.kpfu.ru/psychological-service/about/general-information')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Адрес нашего сайта', reply_markup=markup)

'''@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn2 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)'''

'''@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit', callback.message.chat.id, callback.message.message_id)'''

'''@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')'''

if __name__ == '__main__':
    bot.polling(none_stop=True)
