import telebot
from telebot import types
import time
import requests

#список для id пользователей
dict = []

#токен
bot = telebot.TeleBot('6402385826:AAGDzYKLNwxi0LrzAdrOtkiQr-9F_w7-EZY')

#получить id любого сообщения
@bot.message_handler(commands=['id'])
def id(message):
    bot.send_message(message.chat.id, 'Пришлите сообщение')
    bot.register_next_step_handler(message, all)
def all(message):
    video_id = message
    print(video_id)

#начало бота
@bot.message_handler(commands=['start'])
def start(message):
    dict.append(message.chat.id)
    kb = types.InlineKeyboardMarkup(row_width=1)
    bt = types.InlineKeyboardButton(text="ПОСМОТРЕТЬ ВИДЕО", callback_data='bt1')
    kb.add(bt)
    bot.send_video_note(message.chat.id, "DQACAgIAAxkBAAMfZNj5_HqiCGG--eVxku7UoxSTK4kAAtExAAIXl5lKV0HJi3iC5fQwBA")
    time.sleep(2)
    bot.send_message(message.chat.id, '''Привет, моя зайка❤️

Я Алина - твоя любимая Мамми Продаж, наставник по продажам через прокачку мышления и четкую систему

Я подготовила для тебя видео материалы , как на микроблоге зарабатывать 1.000.000 рублей системно каждый месяц 

Немного обо мне:
— я почти не веду экспертной контент в сторис
— я не уговариваю людей купить у меня 
— я не веду блог 24/7

Клиенты сами приходят и хотят у меня купить, потому что я выстроила четкую систему в блоге 

Клиенты покупают у меня за чек 150.000-350.000 легко и без возражений (но сразу скажу, что к этому я шла несколько лет, а тебе облегчу и сокращу путь) 

И именно системой я с тобой поделюсь 

После просмотра материалов, ты получишь от меня 🎁, так что иди до конца❤️

Нажимай на кнопку ниже и смотри первое видео 
''', reply_markup=kb)
    time.sleep(10)
    if message.chat.id in dict:
        bot.send_message(message.chat.id, '''Дорогая, ты тут?
Наверное, забыла нажать на кнопку
Ничего страшного, я позаботилась о тебе и присылаю видео''')
        time.sleep(2)
        bot.send_video(message.chat.id, 'BAACAgIAAxkBAAMlZNj9CXrq__8SEy9aqjopJ3dZUqwAAn82AALUn8hK2jsNWQn0QaowBA')
        time.sleep(20)
        bot.send_message(message.chat.id, '''Мы с тобой познакомились поближе, а теперь к системе:
Самая первая ошибка, которая не дает тебе зарабатывать 300.000-1.000.000 с блога:
— у тебя нет стратегии и дорогого продукта

Более подробно рассказала об этом в видео ниже''')
        time.sleep(2)
        bot.send_video(message.chat.id,'BAACAgIAAxkBAAMlZNj9CXrq__8SEy9aqjopJ3dZUqwAAn82AALUn8hK2jsNWQn0QaowBA')
        time.sleep(20)
        kb1 = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton(text="Посмотреть видео", callback_data='bt2')
        bt2 = types.InlineKeyboardButton(text="Записаться на разбор",
                                         url="https://docs.google.com/forms/d/e/1FAIpQLSf0j8v3t83Wu7UhJhiLxv8EAktqZhixFXbyfSh80DAJE4r9BA/viewform")
        kb1.add(bt1, bt2)
        bot.send_message(message.chat.id, '''Как тебе информация?
Если тебе уже понятно, что у тебя серьезный вопрос со стратегией, не знаешь, как отстроиться от конкурентов и как создать свой уникальный образ, продукт - записывайся на разбор ко мне либо получай 2 видео''', reply_markup=kb1)

#ответы на нажатия кнопок
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'bt1':
        bot.send_video(callback.message.chat.id, 'BAACAgIAAxkBAAMlZNj9CXrq__8SEy9aqjopJ3dZUqwAAn82AALUn8hK2jsNWQn0QaowBA')
        dict.remove(callback.message.chat.id)
        time.sleep(20)
        bot.send_message(callback.message.chat.id, '''Мы с тобой познакомились поближе, а теперь к системе:
Самая первая ошибка, которая не дает тебе зарабатывать 300.000-1.000.000 с блога:
— у тебя нет стратегии и дорогого продукта

Более подробно рассказала об этом в видео ниже''')
        time.sleep(2)
        bot.send_video(callback.message.chat.id, 'BAACAgIAAxkBAAMlZNj9CXrq__8SEy9aqjopJ3dZUqwAAn82AALUn8hK2jsNWQn0QaowBA')
        time.sleep(20)
        kb1 = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton(text="Посмотреть видео", callback_data='bt2')
        bt2 = types.InlineKeyboardButton(text="Записаться на разбор", url="https://docs.google.com/forms/d/e/1FAIpQLSf0j8v3t83Wu7UhJhiLxv8EAktqZhixFXbyfSh80DAJE4r9BA/viewform")
        kb1.add(bt1, bt2)
        bot.send_message(callback.message.chat.id, '''Как тебе информация?
Если тебе уже понятно, что у тебя серьезный вопрос со стратегией, не знаешь, как отстроиться от конкурентов и как создать свой уникальный образ, продукт - записывайся на разбор ко мне либо получай 2 видео''', reply_markup=kb1)

    if callback.data == 'bt2':
        bot.send_message(callback.message.chat.id, '''Дорогая моя, ты отвлекалась и пошла себе стратегию писать? Или уже записалась
Это конечно все здорово, но не торопись, тебе нужно до конца дойти, чтобы понять полную картину, как выйти на 300.000-1.000.000.
Присылаю тебе видео''')
        time.sleep(2)
        bot.send_video(callback.message.chat.id, 'BAACAgIAAxkBAAMlZNj9CXrq__8SEy9aqjopJ3dZUqwAAn82AALUn8hK2jsNWQn0QaowBA')
        time.sleep(20)
        kb2 = types.InlineKeyboardMarkup(row_width=1)
        bt3 = types.InlineKeyboardButton(text="Посмотреть видео", callback_data='bt4')
        kb2.add(bt3)
        bot.send_message(callback.message.chat.id, '''Зая, ты уже прошла 2 шага и близка к 300.000-1.000.000
Осталось пройти один шаг
Ты готова?😍

В этом видео ты узнаешь про навык, который помогает мне продавать на высокие чеки свой продукт

Смотри видео ниже''', reply_markup=kb2)
    if callback.data == 'bt4':
        bot.send_video(callback.message.chat.id, 'BAACAgIAAxkBAAMlZNj9CXrq__8SEy9aqjopJ3dZUqwAAn82AALUn8hK2jsNWQn0QaowBA')
        time.sleep(120)
        kb3 = types.InlineKeyboardMarkup(row_width=1)
        bt4 = types.InlineKeyboardButton(text="Записаться на разбор", url="https://docs.google.com/forms/d/e/1FAIpQLSf0j8v3t83Wu7UhJhiLxv8EAktqZhixFXbyfSh80DAJE4r9BA/viewform")
        kb3.add(bt4)
        bot.send_message(callback.message.chat.id, '''Ты прошла этот путь
Ты узнала мою систему
И да, ты можешь пойти и применять все самостоятельно и ты можешь достигнуть результатов через несколько месяцев с пробами и ошибками

А я предлагаю тебе прийти ко мне на разбор и еще ближе познакомиться со мной, где мы разберем более подробно твою ситуацию в доходе и как тебе достичь цели 300.000-1.000.000 коротким путем

Выбор всегда за тобой:

Идти одной или идти с наставником (мной) к своей цели

Я буду рада с тобой поработать и помочь тебе, если я тебе откликаюсь и ты хочешь быть в моем поле

В любом случае, сам разбор ни к чему не обязывает, это знакомство, если захочешь пойти со мной - пойдешь
Нет - значит нет)

Чтобы записаться на разбор, нужно заполнить анкету ниже
Буду рада тебя видеть ❤️''', reply_markup=kb3)

#непрерывная работа
bot.polling(none_stop=True)