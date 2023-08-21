import telebot
from telebot import types

bot = telebot.TeleBot('6482673854:AAEEJTL9JYHF16SqQIulMLPJYeje7ta0gDs')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Проверить тематику")
    btn2 = types.KeyboardButton("Требования к целевой страницы")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помощник по проверке страниц TikTok!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Проверить тематику':
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
        btn23 = types.KeyboardButton('Продукты/косметика')
        btn24 = types.KeyboardButton('Обучения за границей')
        btn25 = types.KeyboardButton('Азартные игры')
        btn26 = types.KeyboardButton('Алкоголь')
        btn27 = types.KeyboardButton('Финансы')
        btn28 = types.KeyboardButton('Органы/ткани человека')
        btn29 = types.KeyboardButton('Торговля людьми')
        btn30 = types.KeyboardButton('Криптовалюта')
        btn31 = types.KeyboardButton('Особые товары')
        btn32 = types.KeyboardButton('Фильмы, видеоролики')
        btn33 = types.KeyboardButton('VPN-сервисы')
        btn34 = types.KeyboardButton('Службы знакомств')
        btn35 = types.KeyboardButton('Кино и игры')
        btn36 = types.KeyboardButton('Музыка')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30, btn31, btn32, btn33, btn34, btn35, btn36)
        bot.send_message(message.from_user.id, 'Выберите тематику', reply_markup=markup) #ответ бота


    elif message.text == 'Животные':
        bot.send_message(message.from_user.id, 'Продвижение, продажа или предложение животных, включая живых животных, домашний скот, домашних животных, туши или продукты животного происхождения или их части, а также содействие в доступе к ним. Подробнее - https://ads.tiktok.com/help/article/ad-review-checklist-landing-page?lang=en', parse_mode='Markdown')
                         
    elif message.text == '18+':
        bot.send_message(message.from_user.id, 'Продвижение, продажа, предложение порнографических материалов, секс-игрушек и расходных материалов к ним, например смазок, эротических костюмов (фетиш-костюмы или костюмы для сексуальных фантазий), а также содействие в доступе к ним.', parse_mode='Markdown')

    elif message.text == 'Казино':
        bot.send_message(message.from_user.id, 'Продвижение, продажа, предложение услуг казино, азартных игр, размещения и приема ставок на спортивные события, услуг фэнтези-спорта, лотерей (в виде веб-сайта или физического учреждения, в котором доступны услуги монетизации и обналичивания денег), а также содействие в доступе к ним.', parse_mode='Markdown')


    if message.text == 'Требования к целевой страницы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn40 = types.KeyboardButton('Конфиденциальность')
        btn41 = types.KeyboardButton('Тест1')
        btn42 = types.KeyboardButton('Тест2')
        markup.add(btn40, btn41, btn42)
        bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=markup) #ответ бота

    elif message.text == 'Конфиденциальность':
        bot.send_message(message.from_user.id, 'Конф', parse_mode='Markdown')

bot.polling(none_stop=True) #обязательная для работы бота часть

