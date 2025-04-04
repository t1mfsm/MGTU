import telebot
from telebot import types

bot  = telebot.TeleBot('5822086042:AAFy9IGAk-dwd7OXhGlzJybPK-SWhkoVBKo')

@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Как дела?', callback_data='question_1')
    item2 = types.InlineKeyboardButton('Пока', callback_data='goodbye')
    markup.add(item, item2)
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'question_1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Дела отлично!')
        elif call.data == 'goodbye':
            bot.send_message(call.message.chat.id, 'Пока друг!')

bot.polling()