#Импортируем библиотеку телебот
import telebot
#Из телебота достаём типы кнопок
from telebot import types
#Прописываем токен
TOKEN = '5644564394:AAHP4lmU9ePD1Q3KlhF-vXu-ao99Flgtl9o'
#приписываем токен боту
bot = telebot.TeleBot(TOKEN)
#Вызываем команду старт
@bot.message_handler(commands=['start'])
#Создаём функцию для кнопок
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)#Добавляем кнопкам переменные
    item1 = types.KeyboardButton('О компании')
    item2 = types.KeyboardButton('Услуги')
    item3 = types.KeyboardButton('Новости')
    item4 = types.KeyboardButton('Объекты')
    item5 = types.KeyboardButton('Лицензии')
    item6 = types.KeyboardButton('Вакансии')
    item7 = types.KeyboardButton('Контакты')
    item8 = types.KeyboardButton('Главная')
#Добавляем кнопки
    markup.add(item1, item2, item3, item4, item5, item6,item7, item8)
#Отправляем приветственное сообщение
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)
#Вызываем хендлер для будущих ответов
@bot.message_handler(content_types=['text'])
def bot_message(message): #Создаём функцию для ответа на конкретные сообщения
    if message.chat.type == 'private':#Для личных сообщений
        #Прописываем условия при нажатии каких кнопок будут отправляться сообщения ботом
        if message.text == 'О компании':
            bot.send_message(message.chat.id, 'Всю актуальную информацию по сотрудникам, компании и многом другом можно прочитать тут: \nhttps://um-electro.ru/company/ ')

        elif message.text == 'Новости':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Новости')
            if message.text == 'Новости':
                bot.send_message(message.chat.id, 'Все актуальные новости можно найти на нашем сайте: \nhttps://um-electro.ru/category/news/')
            back = types.KeyboardButton('Главная')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'Новости', reply_markup = markup)
        elif message.text == 'Услуги':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Услуги')
            if message.text == 'Услуги':
                bot.send_message(message.chat.id,
                                 'Все актуальные услуги можно найти на нашем сайте: \nhttps://um-electro.ru/category/uslugi/')
            back = types.KeyboardButton('Главная')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'Услуги', reply_markup=markup)
        elif message.text == 'Объекты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Объекты')
            back = types.KeyboardButton('Главная')
            if message.text == 'Объекты':
                bot.send_message(message.chat.id, 'https://um-electro.ru/category/objects/')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'Объекты', reply_markup = markup)
        elif message.text == 'Главная':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('О компании')
            item2 = types.KeyboardButton('Услуги')
            item3 = types.KeyboardButton('Новости')
            item4 = types.KeyboardButton('Объекты')
            item5 = types.KeyboardButton('Лицензии')
            item6 = types.KeyboardButton('Вакансии')

            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Главная', reply_markup = markup)
        elif message.text == 'Лицензии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Лицензии')
            if message.text == 'Лицензии':
                bot.send_message(message.chat.id, 'Все лицензии тут: \nhttps://um-electro.ru/documents/')
            back = types.KeyboardButton('Главная')
            markup.add(item1,back)
            bot.send_message(message.chat.id, 'Лицензии', reply_markup = markup)

        elif message.text == 'Вакансии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Вакансии')
            if message.text == 'Вакансии':
                bot.send_message(message.chat.id, 'Все актуальные вакансии тут: \nhttps://um-electro.ru/category/vakansy/')
            back = types.KeyboardButton('Главная')
            markup.add(item1,back)
            bot.send_message(message.chat.id, 'Вакансии', reply_markup = markup)
        elif message.text == 'Контакты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Контакты')
            if message.text == 'Контакты':
                bot.send_message(message.chat.id, 'Все контакты тут: \nВсе контакты тут https://um-electro.ru/contacts/')
            back = types.KeyboardButton('Главная')
            markup.add(item1,back)
            bot.send_message(message.chat.id, 'Контакты', reply_markup = markup)


#Делаем работу бота практически бесконечной
bot.polling(none_stop = True)
