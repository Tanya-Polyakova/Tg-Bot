import telebot
from telebot import types

bot = telebot.TeleBot('6482673854:AAEEJTL9JYHF16SqQIulMLPJYeje7ta0gDs')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Проверить страницу")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помощник по проверке страниц TikTok!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Проверить страницу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Животные')
        btn2 = types.KeyboardButton('18+')
        btn3 = types.KeyboardButton('Казино')
        btn4 = types.KeyboardButton('Сигареты')
        btn5 = types.KeyboardButton('Пиратская продукция')
        btn6 = types.KeyboardButton('Наркотики')
        btn7 = types.KeyboardButton('Военное снаряжение')
        btn8 = types.KeyboardButton('Социальная реклама')
        btn9 = types.KeyboardButton('Неприемлемые методы')
        btn10 = types.KeyboardButton('Беременность')
        btn11 = types.KeyboardButton('Ритуальные услуги')
        btn12 = types.KeyboardButton('Химические вещества')
        btn13 = types.KeyboardButton('Человеческие органы')
        btn14 = types.KeyboardButton('Кастинг моделей')
        btn15 = types.KeyboardButton('Пол ребенка')
        btn16 = types.KeyboardButton('Спорная деятельность')
        btn17 = types.KeyboardButton('Оружие')
        btn18 = types.KeyboardButton('Эзотерика')
        btn19 = types.KeyboardButton('Лекарства')
        btn20 = types.KeyboardButton('Медицина')
        btn21 = types.KeyboardButton('БАД')
        btn22 = types.KeyboardButton('Детская смесь')
        btn23 = types.KeyboardButton('Продукты/косметика для сжигания жира')
        btn24 = types.KeyboardButton('Обучения за границей')
        btn25 = types.KeyboardButton('Азартные игры')
        btn26 = types.KeyboardButton('Алкоголь')
        btn27 = types.KeyboardButton('Денежные ценности')
        btn28 = types.KeyboardButton('Внебиржевые финансовые инструменты')
        btn29 = types.KeyboardButton('Органы/ткани человека')
        btn30 = types.KeyboardButton('Торговля людьми')
        btn31 = types.KeyboardButton('Криптографическая защита информации')
        btn32 = types.KeyboardButton('Товары, подлежащие обязательному подтверждению')
        btn33 = types.KeyboardButton('Товары, запрещенные к производству')
        btn34 = types.KeyboardButton('Фильмы, видеоролики')
        btn35 = types.KeyboardButton('VPN-сервисы')
        btn36 = types.KeyboardButton('Финансовые услуги')
        btn37 = types.KeyboardButton('Приложения или службы знакомств')
        btn38 = types.KeyboardButton('Кино и игры')
        btn39 = types.KeyboardButton('Музыкальное представление')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30, btn31, btn32, btn33, btn34, btn35, btn36, btn37, btn38, btn39)
        bot.send_message(message.from_user.id, 'Выберите тематику', reply_markup=markup) #ответ бота


    elif message.text == 'Животные':
        bot.send_message(message.from_user.id, 'Продвижение, продажа или предложение животных, включая живых животных, домашний скот, домашних животных, туши или продукты животного происхождения или их части, а также содействие в доступе к ним.', parse_mode='Markdown')

    elif message.text == '18+':
        bot.send_message(message.from_user.id, 'Продвижение, продажа, предложение порнографических материалов, секс-игрушек и расходных материалов к ним, например смазок, эротических костюмов (фетиш-костюмы или костюмы для сексуальных фантазий), а также содействие в доступе к ним.', parse_mode='Markdown')

    elif message.text == 'Казино':
        bot.send_message(message.from_user.id, 'Продвижение, продажа, предложение услуг казино, азартных игр, размещения и приема ставок на спортивные события, услуг фэнтези-спорта, лотерей (в виде веб-сайта или физического учреждения, в котором доступны услуги монетизации и обналичивания денег), а также содействие в доступе к ним.', parse_mode='Markdown')


@bot.message_handler(commands=['step1'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Требования к целевой страницы")
    markup.add(btn2)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Конфиденциальность')
        btn2 = types.KeyboardButton('Тест1')
        btn3 = types.KeyboardButton('Тест2')

bot.polling(none_stop=True) #обязательная для работы бота часть

