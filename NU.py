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
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение, продажа или предложение животных, включая живых животных, домашний скот, домашних животных, туши или продукты животного происхождения или их части, а также содействие в доступе к ним. ИСКЛЮЧЕНИЯ: товары для животных (игрушки, одежда, ошейники, клетки, еда и т. д.); услуги для домашних животных, такие как выгул собак, уход за домашними животными, зоомагазины, услуги мойки, дрессировка и т. д.; рекламный контент, связанный с адопцией животных, разрешен для НПО, НКО и приютов для животных. Однако запрещено продвижение, продажа, предложение или содействие в доступе к следующему: пристройство племенных или породистых питомцев;  скрещивание домашних животных. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')
                         
    elif message.text == '18+':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение, продажа, предложение порнографических материалов, секс-игрушек и расходных материалов к ним, например смазок, эротических костюмов (фетиш-костюмы или костюмы для сексуальных фантазий), а также содействие в доступе к ним. Продвижение, продажа, предложение развлечений для взрослых (хост/хостесс-клубы, стриптиз-клубы), сексуальных услуг (эскорт-услуг, проституции, эротического массажа) или подобного, а также содействие в доступе к ним. Продвижение, продажа, предложение приложений или служб знакомств, которые предполагают, подразумевают, описывают или поощряют отношения по расчету, супружескую измену, сексуальные контакты или подобное, а также содействие в доступе к ним. Продвижение, продажа, предложение возможности повышения сексуальной активности, получения удовольствий или улучшения внешнего вида за счет потребления наркотических веществ, медикаментов, использования инструментов, устройств или любых подобных продуктов и услуг, а также содействие в доступе к ним. Например, увеличение полового члена, увеличение груди. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Казино':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение, продажа, предложение услуг казино, азартных игр, размещения и приема ставок на спортивные события, услуг фэнтези-спорта, лотерей (в виде веб-сайта или физического учреждения, в котором доступны услуги монетизации и обналичивания денег), а также содействие в доступе к ним. Продвижение, продажа, предложение следующих услуг, а также содействие в доступе к ним: бесплатные кредиты, ваучеры, купоны в любой форме, включая печатные или цифровые коды, для использования в казино и азартных играх; веб-сайты, программное обеспечение, товары или услуги, которые поддерживают или осуществляют направление трафика на страницы казино и азартных игр, а также связанного с ними контента, включая калькулятор шансов, советы и рекомендации, правила и стратегии, горячие предложения и прогнозы; игры на удачу или случай, например скретч-лотереи, бинго или любые другие подобные игры или приложения, которые могут принести денежный или ценный приз; приспособления, инструменты, устройства, реквизит или любые другие аксессуары или принадлежности для использования в казино и азартных играх. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Сигареты':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение, продажа или предложение сигарет, сигар, табака, электронных сигарет или любых других альтернатив курению или потреблению табака, а также содействие в доступе к ним. Продвижение, продажа или предложение принадлежностей для курения, включая курительные трубки, папиросную бумагу, фильтры, испарители или любые другие устройства, приспособления и агрегаты, предназначенные для курения. Реклама объекта, места или заведения для курения или потребления табака, включая сигарные бары, кальянные или любые другие места для аналогичных целей. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Пиратская продукция':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение, продажа или предложение контрафактных товаров, копий, имитаций, включая пиратские цифровые продукты, без разрешения владельца бренда или товарного знака, а также содействие в доступе к ним. К таким продуктам относятся следующие: подделки, выдаваемые за подлинные товары владельца бренда или товарного знака; товары, описанные как копии, имитации или что-либо подобное. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Наркотики':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО Продвижение, продажа или предложение запрещенных наркотических веществ, подлежащих контролю лекарственных и наркотических средств, отпускаемых по рецепту лекарств (запрещенных на некоторых рынках), рекреационных, гомеопатических, укрепляющих, стимулирующих препаратов, в том числе для потери веса, а также содействие в доступе к ним. Продвижение, продажа или предложение принадлежностей для употребления наркотиков, аксессуаров или расходных материалов к ним, а также содействие в доступе к ним. Продвижение несанкционированных аптекарских магазинов, аптек или диспансеров, а также содействие в доступе к ним. Изображение или демонстрация употребления наркотиков, злоупотребления ими или злоупотребления наркотическими веществами, отпускаемыми по рецепту. Описание или использование слов, символов или изображений, связанных с наркотиками, в форме визуального или аудиоконтента или подобного. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')
    
    elif message.text == 'Военное снаряжение':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение, продажа или предложение полицейской или военной формы, жилетов, наручников, дубинок, ботинок или подобных аксессуаров, оборудования или принадлежностей, а также содействие в доступе к ним. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Социальная реклама':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Кандидатам или кандидатам на государственные должности, политическим партиям, а также избранным или назначенным государственным служащим запрещена реклама. Супругам кандидатов, избранным или назначенным государственным служащим с официальными обязанностями или должностями запрещается. Члены королевской семьи с официальными государственными полномочиями также запрещены. Государственные учреждения могут иметь право размещать рекламу, если они работают с торговым представителем TikTok. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Неприемлемые методы':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение, продажа или предложение товаров и услуг, которые могут быть или признаны обманчивыми, вводящими в заблуждение или незаконными, а также содействие в доступе к ним. К таким товарам и услугам можно отнести следующие: незаконный обход технических или иных ограничений доступа с целью нарушения прав интеллектуальной собственности или иных прав собственности; кража личных данных или любой личной информации, в том числе с использованием вредоносных программ, шпионского ПО или любых несанкционированных или незаконных способов получения информации; фальсификация, подделка, искажение документов и т. д.; неподтвержденные заявления и дезинформация, в том числе несовпадение сведений о ценах, скидках или акциях, отсутствие страницы с политикой конфиденциальности, условиями и положениями и любыми другими подобными документами; ложные заявления, опускание информации о сборах, платежах и тарифах, предложение вредоносных бизнес-моделей и т. д. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Беременность':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Услуги по прерыванию беременности. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Ритуальные услуги':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение ритуальных услуг. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

    elif message.text == 'Химические вещества':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Провижение опасных химических веществ. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1', parse_mode='Markdown')

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

