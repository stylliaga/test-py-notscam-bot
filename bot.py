# coding=utf-8
import const
import telebot
import random
import pymysql.cursors

from telebot import types

bot = telebot.TeleBot(const.TOKEN)

# Функция возвращает connection.

# Вы можете изменить параметры соединения.
connection = pymysql.connect(db="proficeram_fnprs", user="proficeram_fnprs", passwd="fanpar8380ft",host="VH273.spaceweb.ru",port=3306,autocommit=True)

print("connect successful!!")
try:

    with connection.cursor() as cursor:

        # SQL
        sql = "Select * from users"

        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)

        print("cursor.description: ", cursor.description)

        print()

        for row in cursor:
            print(row)

finally:
    # Закрыть соединение (Close connection).
    connection.close()



@bot.message_handler(commands=['start'])
def startpg(message):
    # keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, '🤖Бот для заработка приветствует вас!🤖', reply_markup=keyboard)
    startmenu = types.InlineKeyboardMarkup()
    startmenubutton = types.InlineKeyboardButton("Отправить 3 пессо",
                                                 # url="https://freekassa.com",
                                                 callback_data='payed123')

    startmenu.add(startmenubutton)
    bot.send_message(message.chat.id, "\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"
                                      "Что бы получить доступ к функциям бота отправь 3 пессо!"
                                      "\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n",
                     reply_markup=startmenu)
    # startAfterPayed()


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == "payed123":
        bot.answer_callback_query(c.id, show_alert=True, text="Оплачено!")
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        startmenu = types.ReplyKeyboardMarkup(True, False)
        startmenu.row('🔥 Задания', '💲 Кошелек')
        startmenu.row('🤝 Рефералы', '🎮 Игры')
        bot.send_message(c.message.chat.id,
                         "Поздравляем!\nВам доступны все опции бота.",
                         reply_markup=startmenu)


@bot.message_handler(content_types=['text'])
def osnov(message):
    if message.text == '◀️ В начало':
        startAfterPayed(message)
    elif message.text == '🔥 Задания':
        zadanie = types.ReplyKeyboardMarkup(True, False)
        zadanie.row('🤖 Разгадывание каптчи', '📰 Подписаться на канал')
        zadanie.row('◀️ В начало')
        bot.send_message(message.chat.id, 'Выберите задание для заработка:', reply_markup=zadanie)
    # Кошелек
    elif message.text == '💲 Кошелек':
        lopatnik = types.ReplyKeyboardMarkup(True, False)
        lopatnik.row('💸 Вывод', '💳 Пополнение')
        lopatnik.row('◀️ В начало')
        bot.send_message(message.chat.id, 'Ваш баланс: <code>999</code>р.\n'
                                          'Заработано с рефералов: <code>1 000</code> р.',
                         reply_markup=lopatnik,
                         parse_mode='HTML')
    # Рефералы
    elif message.text == '🤝 Рефералы':
        refs = types.ReplyKeyboardMarkup(True, False)
        refs.row('◀️ В начало')
        bot.send_message(message.chat.id, 'Вы привлекли: <code>5</code> рефералов.\n'
                                          'Заработано с рефералов: <code>1 000</code> р.\n\n'
                                          'Ваша реферальная ссылка:\n '
                                          '<code>https://tggr.ru/NotScamBot?start=ref123</code>',
                         reply_markup=refs,
                         parse_mode='HTML')

        # if dietasm == 'dietasm':
        #     bot.send_message(message.chat.id, 'http://telegra.ph/Nabor-Myshechnoj-Massy-09-23')
    # Игры
    elif message.text == '🎮 Игры':
        games = types.ReplyKeyboardMarkup(True, False)
        games.row('🦅 Орел- 🌰 Решка', '🥇 От 0 до 10 🥉')
        games.row('◀️ В начало')
        bot.send_message(message.chat.id, 'Выберите игру:',
                         reply_markup=games)
    # Игры
    elif message.text == '🦅 Орел- 🌰 Решка':
        games = types.ReplyKeyboardMarkup(True, False)
        games.row('🥇 От 0 до 10 🥉')
        games.row('◀️ В начало')
        bot.send_message(message.chat.id, 'Здесь будет игра "🦅 Орел- 🌰 Решка"\n\n'
                                          '<i>Классическая азартная игра знакомая каждому!\n'
                                          'Ставите на орла или решку и нажимаете кнопку "💰 Бросить монетку!".</i>',
                         reply_markup=games,
                         parse_mode='HTML')
    # Игры
    elif message.text == '🥇 От 0 до 10 🥉':
        games = types.ReplyKeyboardMarkup(True, False)
        games.row('🦅 Орел- 🌰 Решка')
        games.row('◀️ В начало')
        bot.send_message(message.chat.id, 'Здесь будет игра "🥇 От 0 до 10 🥉"\n\n'
                                          '<i>🎉Делайте ставку на любое ОДНО число от 0 до 10, нажимайте кнопку '
                                          '"🎲 Запустить!" и выигрывайте!🎉</i>',
                         reply_markup=games,
                         parse_mode='HTML')
    # Вывод
    elif message.text == '💸 Вывод':
        vyvod = types.ReplyKeyboardMarkup(True, False)
        vyvod.row('◀️ В начало', '💳 Пополнение')
        bot.send_message(message.chat.id, '⚠️<i>Извините, технические неполадки!</i>⚠️\n\n'
                                          'Вывод возможен при балансе не менее 500р.\n\n'
                                          '<b>Связь с администрацией:</b> @adminNotScamBot',
                         reply_markup=vyvod,
                         parse_mode='HTML')
    # Пополнение
    elif message.text == '💳 Пополнение':
        popolnenie = types.ReplyKeyboardMarkup(True, False)
        popolnenie.row('◀️ В начало', '🎮 Игры')
        bot.send_message(message.chat.id, '⚠️<i>Минимальная сумма пополнения <code>200</code>р.</i>⚠️\n\n',
                         reply_markup=popolnenie,
                         parse_mode='HTML')
        popolnenieinline = types.InlineKeyboardMarkup()
        popolnenieinlinebutton = types.InlineKeyboardButton("Пополнить 💳 ",
                                                            url="https://freekassa.com",
                                                            callback_data='payed123')
        popolnenieinline.add(popolnenieinlinebutton)
        bot.send_message(message.chat.id, "\nПополнить баланс можно любым удобным способом - Банковской картой, QIWI,"
                                          " Яндекс.Кошелек и т.д.",
                         reply_markup=popolnenieinline)


@bot.message_handler(content_types=['text'])
def startAfterPayed(message):
    startmenu = types.ReplyKeyboardMarkup(True, False)
    startmenu.row('🔥 Задания', '💲 Кошелек')
    startmenu.row('🤝 Рефералы', '🎮 Игры')
    bot.send_message(message.chat.id,
                     "\n💎 Да, детка! Греби бабки лопатой! 💎\n",
                     reply_markup=startmenu)


# @bot.callback_query_handler(func=lambda c:True)
# def cam

bot.polling()
