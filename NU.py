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

    elif message.text == 'Человеческие органы':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Торговля человеческими органами или тканями, трансплантация или подобная деятельность. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B2%20%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85%20%D0%BE%D0%B1%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%D1%85.-,%D0%9D%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B4%D0%B5%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B%20%D0%B8%20%D1%83%D1%81%D0%BB%D1%83%D0%B3%D0%B8,-%D0%A3%D1%81%D0%BB%D1%83%D0%B3%D0%B8%20%D0%BF%D0%BE%20%D0%BF%D1%80%D0%B5%D1%80%D1%8B%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E', parse_mode='Markdown')

    elif message.text == 'Кастинг моделей':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Услуги по прохождению кастинга в модели или продвижению в качестве инфлюенсера. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B2%20%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85%20%D0%BE%D0%B1%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%D1%85.-,%D0%9D%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B4%D0%B5%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B%20%D0%B8%20%D1%83%D1%81%D0%BB%D1%83%D0%B3%D0%B8%C2%A0,-%D0%A3%D1%81%D0%BB%D1%83%D0%B3%D0%B8%20%D0%BF%D0%BE%20%D0%BF%D1%80%D0%B5%D1%80%D1%8B%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E', parse_mode='Markdown')

    elif message.text == 'Пол ребенка':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Определение пола ребенка до рождения. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B2%20%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85%20%D0%BE%D0%B1%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%D1%85.-,%D0%9D%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B4%D0%B5%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B%20%D0%B8%20%D1%83%D1%81%D0%BB%D1%83%D0%B3%D0%B8%C2%A0,-%D0%A3%D1%81%D0%BB%D1%83%D0%B3%D0%B8%20%D0%BF%D0%BE%20%D0%BF%D1%80%D0%B5%D1%80%D1%8B%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E', parse_mode='Markdown')

    elif message.text == 'Спорная деятельность':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Любая другая коммерческая деятельность, продукты и услуги, которые являются весьма спорными, вызывающими чувство отторжения, насильственными или опасными, будут рассматриваться как несовместимые с Рекламной платформой TikTok. В этот список входят объявления, в которых упоминается чувствительная тема или событие (например, чья-либо смерть, природные или техногенные катастрофы, насильственные атаки, гражданские беспорядки и т. д.) и содержатся личные нападки, неправомерное использование хештега, реклама товаров или услуг, политическая агитация, соблазнение подписчиков либо любой другой неприемлемый контент. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B2%20%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85%20%D0%BE%D0%B1%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%D1%85.-,%D0%9D%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B4%D0%B5%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B%20%D0%B8%20%D1%83%D1%81%D0%BB%D1%83%D0%B3%D0%B8%C2%A0,-%D0%A3%D1%81%D0%BB%D1%83%D0%B3%D0%B8%20%D0%BF%D0%BE%20%D0%BF%D1%80%D0%B5%D1%80%D1%8B%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E', parse_mode='Markdown')
    
    elif message.text == 'Оружие':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Продвижение, продажа или предложение оружия, которое может быть использовано для причинения вреда людям или для самообороны, а также содействие в доступе к ним, включая: лезвия, ножи и любые подобные острые предметы; взрывчатые, легковоспламеняющиеся или горючие вещества, включая бомбы и принадлежности для изготовления бомб, огнеметы, фейерверки или любое другое подобное оборудование; стрелковое оружие, детали стрелкового оружия и боеприпасы, включая пейнтбольные ружья, пневматические пистолеты; дубинки, нунчаки, электрошокеры, перцовые баллончики или любое подобное оружие для самообороны. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Эзотерика':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама услуг в области паранормальных явлений, гадания, спиритизма, астрологии, магии, предсказаний, а также лиц, утверждающих, что они могут предсказывать будущее, влиять на людей, духовную жизнь, имущество, окружающую среду, используя сверхъестественные способности или силы, и тренинги по таким услугам. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry-eastern-europe?lang=ru#:~:text=%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D1%8C%20/%20BY-,%D0%97%D0%B0%D0%BF%D1%80%D0%B5%D1%89%D0%B5%D0%BD%D0%BE,-%D0%A0%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%B0%20%D1%83%D1%81%D0%BB%D1%83%D0%B3%20%D0%B2', parse_mode='Markdown')

    elif message.text == 'Лекарства':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама рецептурных препаратов. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Медицина':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама медицинских услуг, лекарств, медицинских приборов или методов оказания медицинской помощи, не одобренных Министерством здравоохранения Республики Беларусь. Реклама медицинских устройств, использование которых требует профессиональных знаний, и услуг в сфере здравоохранения, которые официально не признаются медицинскими услугами. ОГРАНИЧНО: Реклама препаратов, отпускаемых без рецепта, продукции медицинского назначения и медицинских изделий должна соответствовать действующему законодательству. Требуется наличие свидетельства о регистрации или лицензии. Объявления должны содержать надлежащий отказ от ответственности и соответствовать всем применимым требованиям властей о раскрытии информации. Реклама может быть нацелена только на пользователей не моложе 18 лет. Запрещена реклама клинических испытаний. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'БАД':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама биологически активных добавок к пище, не одобренных Министерством здравоохранения Республики Беларусь. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Детская смесь':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама детских смесей. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Продукты/косметика':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама пищевых продуктов и косметики, которые, как утверждается, напрямую сжигают жир или преобразуют жир в другие вещества. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Обучения за границей':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Рекламные объявления о возможностях обучения за рубежом, не одобренные Министерством внутренних дел и Министерством образования Республики Беларусь. ОГРАНИЧЕНО: Следует запросить согласование в Министерстве внутренних дел и Министерстве образования Республики Беларусь. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Азартные игры':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама услуг, связанных с азартными играми / симуляторами азартных игр, или любых услуг, которые воспроизводят практику азартных игр. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Алкоголь':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама алкогольных напитков. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Финансы':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама с привлечением денежных средств или иного имущества с последующей выплатой дохода лицом, не зарегистрированным в качестве юридического лица или индивидуального предпринимателя в Республике Беларусь. Реклама операций с безвозвратными внебиржевыми финансовыми инструментами, осуществляемых лицами, не являющимися форекс-компаниями, Национальным форекс-центром, банками, небанковскими кредитными и финансовыми учреждениями. Реклама определенных финансовых услуг, включая, помимо прочего: пирамиды, схемы быстрого обогащения, услуги консолидации долгов, бинарные опционы, займы между физическими лицами (P2P), микрокредиты, криптовалюту и т. д. ОГРАНИЧЕНО: Реклама банковских, страховых и других разрешенных финансовых услуг должна соответствовать действующему законодательству. Вам может потребоваться наличие лицензии или свидетельства о регистрации. Реклама может быть нацелена только на пользователей не моложе 18 лет. Обратитесь к разделу «Запрещенные товары или услуги» для получения более подробной информации о запрещенных финансовых продуктах. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Органы/ткани человека':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама, связанная с продажей или покупкой человеческих органов или тканей. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Торговля людьми':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама, пропагандирующая торговлю людьми или вовлекающая ее потенциальных жертв. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Криптовалюта':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама услуг, связанных с криптографической защитой информации и способами ее секретного получения. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Особые товары':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама товаров, подлежащих обязательному подтверждению соответствия в Республике Беларусь. Нельзя демонстрировать рекламу, если такое подтверждение отсутствует. Реклама товаров, запрещенных к производству или продаже в соответствии с законодательством, либо деятельности, запрещенной на законодательном уровне. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Фильмы, видеоролики':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама фильмов, видео или других произведений, пропагандирующих насилие и жестокость. \nПодробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'VPN-сервисы':
        bot.send_message(message.from_user.id, 'ЗАПРЕЩЕНО: Реклама VPN-сервисов. \nПодробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Службы знакомств':
        bot.send_message(message.from_user.id, 'ОГРАНИЧЕНО: Необходимо применять таргетинг по возрасту на аудиторию не моложе 18 лет. Такого рода реклама не должна иметь ярко выраженный сексуальный характер или упоминать отношения по расчету или измены и т. д. Реклама приложений для знакомств не должна быть непристойного содержания (концентрироваться на телах, использовать непристойные выражения, содержать намеки сексуального характера и т. д.). Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Кино и игры':
        bot.send_message(message.from_user.id, 'ОГРАНИЧЕНО: Рекламное видео должно содержать возрастной рейтинг (0+, 6+, 12+, 16+, 18+) с применением таргетинга по возрасту. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    elif message.text == 'Музыка':
        bot.send_message(message.from_user.id, 'ОГРАНИЧЕНО: Если музыкальное мероприятие проводится не онлайн, требуется сертификат на право проведения культурно-развлекательного мероприятия в Республике Беларусь. Рекламные объявления должны содержать информацию о наличии или отсутствии фонограммы, возрастной рейтинг (0+, 6+, 12+, 16+, 18+) с применением таргетинга по возрасту. Кроме того, в объявлениях необходимо указать такую обязательную информацию, как название, адрес, номера телефонов организатора, а также информацию о сертификате на право организации культурно-развлекательного мероприятия в Республике Беларусь. Подробнее - https://ads.tiktok.com/help/article/tiktok-advertising-policies-industry-entry?redirected=1#:~:text=%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BB%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.-,%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%C2%A0,-%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%20%D0%B8%D0%BB%D0%B8', parse_mode='Markdown')

    if message.text == 'Требования к целевой страницы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn40 = types.KeyboardButton('Информация о компании')
        btn41 = types.KeyboardButton('Удобность для моб.устр.')
        btn42 = types.KeyboardButton('Запрещенные товары')
        btn43 = types.KeyboardButton('Конфиденциальность')
        markup.add(btn40, btn41, btn42, btn43)
        bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=markup) #ответ бота

    elif message.text == 'Информация о компании':
        bot.send_message(message.from_user.id, 'Целевые страницы для рекламы электронной коммерции и финансовых услуг должны отображать достоверную информацию о компании в видимом месте, включая, помимо прочего, информацию о том, кто управляет сайтом, ее правилах, ценах, отображаемых в местной валюте, условиях и бизнес-лицензии. Чтобы гарантировать, что объявления пройдут проверку, включите эту информацию в видном месте на каждой странице/URL-адресе. В идеале эта информация должна отображаться на каждой странице сайта.',  parse_mode='Markdown')
        photo = open('stranica.PNG', 'rb')
        bot.send_message(call.message.chat.id, text=Информация о компании, photo=photo,reply_markup=keyboard)


    elif message.text == 'Удобность для моб.устр.':
        bot.send_message(message.from_user.id, 'Целевая страница должна быть адаптирована для мобильных устройств. Посетители должны иметь возможность просматривать ваш веб-сайт на мобильном устройстве в горизонтальной и вертикальной ориентации, и им не нужно увеличивать масштаб, чтобы прочитать текст или использовать кнопки.', parse_mode='Markdown')

    elif message.text == 'Запрещенные товары':
        bot.send_message(message.from_user.id, 'Целевые страницы не могут отображать запрещенные товары, даже если вы не рекламируете их с помощью рекламы. Например, реклама приемлемого продукта, такого как мобильная игра, не может привести к тому, что на целевой странице будут показаны запрещенные продукты, такие как электронные сигареты.', parse_mode='Markdown')
    
    elif message.text == 'Конфиденциальность':
        bot.send_message(message.from_user.id, 'Целевая страница не может запрашивать у посетителей конфиденциальную информацию для доступа к сайту, включая, помимо прочего, личную информацию, финансовую информацию, информацию о здоровье или биометрические данные. Например, ваша целевая страница не может требовать от пользователей предоставления информации о кредитной карте перед доступом к вашему сайту.', parse_mode='Markdown')

bot.polling(none_stop=True) #обязательная для работы бота часть

