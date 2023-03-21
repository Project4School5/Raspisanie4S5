import os
import telebot

from telebot import types

from config import TG_BOT_TOKEN

bot = telebot.TeleBot(TG_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

  markup = types.InlineKeyboardMarkup(row_width=1)
  item1 = types.InlineKeyboardButton("Расписание уроков📋", callback_data='less')
  item2 = types.InlineKeyboardButton("Расписание звонков🔔", callback_data='bell')
  markup.add(item1, item2)
  fotka = open('fotka.jpg', 'rb')
  bot.send_photo(message.chat.id, fotka, 
  	caption='Добро пожаловать, {0.first_name}!\nЗдесь ты можешь узнать актуальное расписание уроков и звонков в МБОУ СОШ №5. Для этого просто нажми на одну из кнопок внизу👇'.format(message.from_user, bot.get_me()),
 	parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:      
		if call.message:
			if call.data == 'back':
				markup = types.InlineKeyboardMarkup(row_width=1)
				item1 = types.InlineKeyboardButton("Расписание уроков📋", callback_data='less')
				item2 = types.InlineKeyboardButton("Расписание звонков🔔", callback_data='bell')
				markup.add(item1, item2)
				fotka = open('fotka.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(fotka), reply_markup=markup)
				bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					caption='Узнать актуальное расписание уроков и звонков в МБОУ СОШ №5 легко: для этого просто нажми на одну из кнопок внизу👇',
					parse_mode='html', reply_markup=markup)

			if call.data == 'back1':
				markup = types.InlineKeyboardMarkup(row_width=3)
				item5 = types.InlineKeyboardButton("5", callback_data='5')
				item6 = types.InlineKeyboardButton("6", callback_data='6')
				item7 = types.InlineKeyboardButton("7", callback_data='7')
				item8 = types.InlineKeyboardButton("8", callback_data='8')
				item9 = types.InlineKeyboardButton("9", callback_data='9')
				item10 = types.InlineKeyboardButton("10", callback_data='10')
				item11 = types.InlineKeyboardButton("11", callback_data='11')
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back')
				markup.add(item5, item6, item7, item8, item9, item10, item11, item)
				fotka = open('fotka.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(fotka), reply_markup=markup)
				bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
					caption='Выберитe номер вашего класса#️⃣', reply_markup=markup)

			if call.data == '5':	
				markup = types.InlineKeyboardMarkup(row_width=1)
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back1')
				markup.add(item)
				CL5 = open('5CL.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(CL5), reply_markup=markup)	
			if call.data == '6':	
				markup = types.InlineKeyboardMarkup(row_width=1)
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back1')
				markup.add(item)
				CL6 = open('6CL.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(CL6), reply_markup=markup)
			if call.data == '7':	
				markup = types.InlineKeyboardMarkup(row_width=1)
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back1')
				markup.add(item)
				CL7 = open('7CL.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(CL7), reply_markup=markup)		
			if call.data == '8':	
				markup = types.InlineKeyboardMarkup(row_width=1)
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back1')
				markup.add(item)
				CL8 = open('8CL.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(CL8), reply_markup=markup)
			if call.data == '9':	
				markup = types.InlineKeyboardMarkup(row_width=1)
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back1')
				markup.add(item)
				CL9 = open('9CL.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(CL9), reply_markup=markup)
			if call.data == '10':	
				markup = types.InlineKeyboardMarkup(row_width=1)
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back1')
				markup.add(item)
				CL10 = open('10CL.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(CL10), reply_markup=markup)	
			if call.data == '11':	
				markup = types.InlineKeyboardMarkup(row_width=1)
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back1')
				markup.add(item)
				CL11 = open('11CL.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(CL11), reply_markup=markup)		

			if call.data == 'less':
				markup = types.InlineKeyboardMarkup(row_width=3)
				item5 = types.InlineKeyboardButton("5", callback_data='5')
				item6 = types.InlineKeyboardButton("6", callback_data='6')
				item7 = types.InlineKeyboardButton("7", callback_data='7')
				item8 = types.InlineKeyboardButton("8", callback_data='8')
				item9 = types.InlineKeyboardButton("9", callback_data='9')
				item10 = types.InlineKeyboardButton("10", callback_data='10')
				item11 = types.InlineKeyboardButton("11", callback_data='11')
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back')
				markup.add(item5, item6, item7, item8, item9, item10, item11, item)
				bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
					caption='Выберите номер вашего класса#️⃣', reply_markup=markup)

			elif call.data == 'bell':
				markup = types.InlineKeyboardMarkup(row_width=1)
				item = types.InlineKeyboardButton("⬅️Назад⬅️", callback_data='back')
				markup.add(item)
				fotka2 = open('fotka2.jpg', 'rb')
				bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, 
					media=types.InputMediaPhoto(fotka2), reply_markup=markup)

				
				
	
	except Exception as e:
		print(repr(e))


bot.infinity_polling()