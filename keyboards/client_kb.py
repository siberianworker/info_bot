from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
home = InlineKeyboardButton(text='В начало 🔝', callback_data='start')
proger = InlineKeyboardButton(text='Связаться с разработчиком 🧑‍💻', url='https://t.me/SiberianWorker')

#Кнопки контакты и информация
ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Контакты ☎️', callback_data='contacts')
ib2 = InlineKeyboardButton(text='Информация 📝', callback_data='info')
ikb.add(ib1, ib2).add(proger)

#Кнопки категория контактов
ikb2 = InlineKeyboardMarkup(row_width=2)
ibs1 = InlineKeyboardButton(text='Автотематика 🚘', callback_data='s1')
ibs2 = InlineKeyboardButton(text='Госучереждения 🇸🇮', callback_data='s2')
ibs3 = InlineKeyboardButton(text='Деньги 💵', callback_data='s3')
ibs4 = InlineKeyboardButton(text='Продажи 🤝', callback_data='s4')
ibs5 = InlineKeyboardButton(text='Ремонт 🛠', callback_data='s5')
ibs6 = InlineKeyboardButton(text='Интернет 💻', callback_data='s6')
ibs9 = InlineKeyboardButton(text='Интернет магазины', callback_data='s9')
ibs7 = InlineKeyboardButton(text='Услуги 🙋‍♂️', callback_data='s7')
ibs8 = InlineKeyboardButton(text='Прочее 🌐', callback_data='s8')
ikb2.add(ibs1, ibs2, ibs3, ibs4, ibs5, ibs6, ibs9, ibs7, ibs8).add(home)

#Контакты  из категории "Автотематика"
ikb3 = InlineKeyboardMarkup(row_width=2)
ibt1 = InlineKeyboardButton(text='Автовокзал', callback_data='t1')
ibt2 = InlineKeyboardButton(text='Автомойки', callback_data='t2')
ibt3 = InlineKeyboardButton(text='Автосервис', callback_data='t3')
ibt4 = InlineKeyboardButton(text='Автошкола', callback_data='t4')
ibt5 = InlineKeyboardButton(text='Автоэлектрик', callback_data='t5')
ibt6 = InlineKeyboardButton(text='Грузовое такси', callback_data='t6')
ibt7 = InlineKeyboardButton(text='Куплю авто', callback_data='t7')
#ibt8 = InlineKeyboardButton(text='Куплю авто', callback_data='t8')
ibt9 = InlineKeyboardButton(text='Манипулятор', callback_data='t9')
ibt10 = InlineKeyboardButton(text='Экскаватор', callback_data='t10')
ibt11 = InlineKeyboardButton(text='Отогрев авто', callback_data='t11')
ibt12 = InlineKeyboardButton(text='Полировка', callback_data='t12')
ibt13 = InlineKeyboardButton(text='Такси', callback_data='t13')
ibt14 = InlineKeyboardButton(text='Техосмотр', callback_data='t14')
ibt15 = InlineKeyboardButton(text='Трезвый водитель', callback_data='t15')
ibt16 = InlineKeyboardButton(text='Услуги самосвала', callback_data='t16')
ibt17 = InlineKeyboardButton(text='Шиномонтаж', callback_data='t17')
ibt18 = InlineKeyboardButton(text='Штрафстоянка', callback_data='t18')
ibt19 = InlineKeyboardButton(text='Эвакуатор', callback_data='t19')
ikb3.add(ibt1, ibt2, ibt3, ibt4, ibt5, ibt6, ibt7, ibt9, ibt11, ibt12, ibt13, ibt14, ibt15, ibt16, ibt17, ibt18, ibt19, ibt10).add(back, home)

#информация
ikb4 = InlineKeyboardMarkup(row_width=2)
ibf1 = InlineKeyboardButton(text='COVID19', callback_data='f1')
ibf2 = InlineKeyboardButton(text='Код АТС', callback_data='f2')
ibf3 = InlineKeyboardButton(text='Экстренные службы', callback_data='f3')
ibf4 = InlineKeyboardButton(text='Расписание автобусов', callback_data='f4')
ibf5 = InlineKeyboardButton(text='Расписание электричек', callback_data='f5')
ikb4.add(ibf1, ibf2, ibf3, ibf4, ibf5).add(home)

#контакты из категории "Госучереждения"
ikb5 = InlineKeyboardMarkup(row_width=2)
iba1 = InlineKeyboardButton(text='Библиотека', callback_data='a1')
iba2 = InlineKeyboardButton(text='Гибдд Шалинское', callback_data='a2')
iba3 = InlineKeyboardButton(text='Дом творчества', callback_data='a3')
iba4 = InlineKeyboardButton(text='ЕДДС', callback_data='a4')
iba5 = InlineKeyboardButton(text='ЖКХ', callback_data='a5')
iba6 = InlineKeyboardButton(text='ЗАГС', callback_data='a6')
iba7 = InlineKeyboardButton(text='Лесничество', callback_data='a7')
iba8 = InlineKeyboardButton(text='Лесопожарный центр', callback_data='a8')
iba9 = InlineKeyboardButton(text='Манская РБ', callback_data='a9')
iba10 = InlineKeyboardButton(text='Медицина катастроф', callback_data='a10')
iba11 = InlineKeyboardButton(text='Медицинское такси', callback_data='a11')
iba12 = InlineKeyboardButton(text='Мировой суд', callback_data='a12')
iba13 = InlineKeyboardButton(text='МФЦ', callback_data='a13')
iba14 = InlineKeyboardButton(text='Налоговая', callback_data='a14')
iba15 = InlineKeyboardButton(text='Отделение полиции', callback_data='a15')
iba16 = InlineKeyboardButton(text='Паспортный стол', callback_data='a16')
iba17 = InlineKeyboardButton(text='Пенсионный фонд', callback_data='a17')
iba18 = InlineKeyboardButton(text='Пожарная шалинская', callback_data='a18')
iba19 = InlineKeyboardButton(text='Почта', callback_data='a19')
iba20 = InlineKeyboardButton(text='Сельский совет', callback_data='a20')
iba21 = InlineKeyboardButton(text='Соцзащита', callback_data='a21')
iba22 = InlineKeyboardButton(text='Судебные приставы', callback_data='a22')
iba23 = InlineKeyboardButton(text='Управление сельхоз', callback_data='a23')
iba24 = InlineKeyboardButton(text='Центр занятости', callback_data='a24')
iba25 = InlineKeyboardButton(text='Шалинская "ДШИ"', callback_data='a25')
iba26 = InlineKeyboardButton(text='Манский архив', callback_data='a26')
iba27 = InlineKeyboardButton(text='Школа', callback_data='a27')
ikb5.add(iba1, iba2, iba3, iba4, iba5, iba6, iba7, iba8, iba9, iba26, iba10, iba11, iba12, iba13, iba14, iba15, iba16, iba17, iba18, iba19,
    iba20, iba21, iba22, iba23, iba24, iba25, iba27).add(back, home)

#контакты из категории "Деньги"
ikb6 = InlineKeyboardMarkup(row_width=2)
ibb1 = InlineKeyboardButton(text='Банк', callback_data='b1')
ibb2 = InlineKeyboardButton(text='Займы', callback_data='b2')
ibb3 = InlineKeyboardButton(text='Страхование', callback_data='b3')
ikb6.add(ibb1, ibb2, ibb3).add(back, home)

#контакты из категории "Продажи"
ikb7 = InlineKeyboardMarkup(row_width=2)
ibd1 = InlineKeyboardButton(text='Аптеки', callback_data='d1')
ibd19 = InlineKeyboardButton(text='Золото', callback_data='d19')
ibd2 = InlineKeyboardButton(text='Горбыль', callback_data='d2')
ibd3 = InlineKeyboardButton(text='Доставка', callback_data='d3')
ibd4 = InlineKeyboardButton(text='Дрова', callback_data='d4')
ibd5 = InlineKeyboardButton(text='Кафе', callback_data='d5')
ibd6 = InlineKeyboardButton(text='Котлы', callback_data='d6')
ibd7 = InlineKeyboardButton(text='Магазины', callback_data='d7')
ibd8 = InlineKeyboardButton(text='Мебель', callback_data='d8')
ibd17 = InlineKeyboardButton(text='Мегафон', callback_data='d17')
ibd18 = InlineKeyboardButton(text='МТС', callback_data='d18')
ibd10 = InlineKeyboardButton(text='Пиломатериал', callback_data='d10')
ibd11 = InlineKeyboardButton(text='Прием металла', callback_data='d11')
ibd12 = InlineKeyboardButton(text='Скот', callback_data='d12')
ibd13 = InlineKeyboardButton(text='Суши', callback_data='d13')
ibd20 = InlineKeyboardButton(text='Торты домашние', callback_data='d20')
ibd14 = InlineKeyboardButton(text='Уголь', callback_data='d14')
ibd15 = InlineKeyboardButton(text='Цветы-светильники', callback_data='d15')
ibd16 = InlineKeyboardButton(text='Шашлык', callback_data='d16') #20
ikb7.add(ibd1, ibd19, ibd2, ibd3, ibd4, ibd5, ibd6, ibd7, ibd8, ibd17, ibd18, ibd10, ibd11, ibd12, ibd13, ibd20, ibd14, ibd15, ibd16).add(back, home)

#контакты из категории "Ремонт"
ikb8 = InlineKeyboardMarkup(row_width=2)
ibe1 = InlineKeyboardButton(text='Ателье', callback_data='e1')
ibe2 = InlineKeyboardButton(text='Внутренняя отделка', callback_data='e2')
ibe3 = InlineKeyboardButton(text='Мастер на час', callback_data='e3')
ibe4 = InlineKeyboardButton(text='Отопление', callback_data='e4')
ibe5 = InlineKeyboardButton(text='Натяжные потолки', callback_data='e5')
ibe6 = InlineKeyboardButton(text='Печник', callback_data='e6')
ibe7 = InlineKeyboardButton(text='Разбор построек', callback_data='e7')
ibe8 = InlineKeyboardButton(text='Ремонт техники', callback_data='e8')
ibe9 = InlineKeyboardButton(text='Сантехник', callback_data='e9')
ibe10 = InlineKeyboardButton(text='Строительство', callback_data='e10')
ibe11 = InlineKeyboardButton(text='Электрик', callback_data='e11')
ikb8.add(ibe1, ibe2, ibe3, ibe4, ibe5, ibe6, ibe7, ibe8, ibe9, ibe10, ibe11).add(back, home)

#контакты из категории "Интернет"
ikb9 = InlineKeyboardMarkup(row_width=2)
ibg1 = InlineKeyboardButton(text='Фринет', callback_data='g1')
ibg2 = InlineKeyboardButton(text='Ростелеком', callback_data='g2')
ibg3 = InlineKeyboardButton(text='Игра-Сервис', callback_data='g3')
ikb9.add(ibg1, ibg2, ibg3).add(back, home)

#контакты из категории "Услуги"
ikb10 = InlineKeyboardMarkup(row_width=2)
ibh1 = InlineKeyboardButton(text='Аниматор', callback_data='h1')
ibh2 = InlineKeyboardButton(text='База отдыха', callback_data='h2')
ibh3 = InlineKeyboardButton(text='Бурение', callback_data='h3')
ibh4 = InlineKeyboardButton(text='Ветеринары', callback_data='h4')
ibh5 = InlineKeyboardButton(text='Видеонаблюдение', callback_data='h5')
ibh6 = InlineKeyboardButton(text='Доставка баллонов', callback_data='h6')
ibh7 = InlineKeyboardButton(text='Ключи', callback_data='h7')
ibh8 = InlineKeyboardButton(text='Кондиционеры', callback_data='h8')
ibh9 = InlineKeyboardButton(text='Логопед', callback_data='h9')
ibh10 = InlineKeyboardButton(text='Массаж', callback_data='h10')
ibh25 = InlineKeyboardButton(text='Окна', callback_data='h25')
ibh11 = InlineKeyboardButton(text='Откачка септиков', callback_data='h11')
ibh12 = InlineKeyboardButton(text='Парикмахерские', callback_data='h12')
ibh13 = InlineKeyboardButton(text='Плотник', callback_data='h13')
ibh14 = InlineKeyboardButton(text='Ритуальные услуги', callback_data='h14')
ibh15 = InlineKeyboardButton(text='Сварка', callback_data='h15')
ibh16 = InlineKeyboardButton(text='Стоматолог', callback_data='h16')
ibh17 = InlineKeyboardButton(text='Тепловизор', callback_data='h17')
ibh18 = InlineKeyboardButton(text='Токарь', callback_data='h18')
ibh19 = InlineKeyboardButton(text='Услуги красоты', callback_data='h19')
ibh20 = InlineKeyboardButton(text='Услуги межевания', callback_data='h20')
ibh21 = InlineKeyboardButton(text='Фотоуслуги', callback_data='h21')
ibh22 = InlineKeyboardButton(text='Химчистка', callback_data='h22')
ibh23 = InlineKeyboardButton(text='Чистка подушек', callback_data='h23')
ibh24 = InlineKeyboardButton(text='Юруслуги', callback_data='h24') #25
ikb10.add(ibh1, ibh2, ibh3, ibh4, ibh5, ibh6, ibh7, ibh8, ibh9, ibh10, ibh25, ibh11, ibh12, ibh13, ibh14, ibh15, ibh16, ibh17,
          ibh18, ibh19, ibh20, ibh21, ibh22, ibh23, ibh24).add(back, home)

#контакты из категории "Прочее"
ikb11 = InlineKeyboardMarkup(row_width=2)
ibi1 = InlineKeyboardButton(text='БТИ', callback_data='i1')
ibi2 = InlineKeyboardButton(text='Метеостанция', callback_data='i2')
ibi3 = InlineKeyboardButton(text='Редакция', callback_data='i3')
ibi4 = InlineKeyboardButton(text='РосТех', callback_data='i4')
ibi5 = InlineKeyboardButton(text='РЭС', callback_data='i5')
ibi6 = InlineKeyboardButton(text='Храм Шалинское', callback_data='i6')
ibi7 = InlineKeyboardButton(text='Энергосбыт', callback_data='i7')
ikb11.add(ibi1, ibi2, ibi3, ibi4, ibi5, ibi6, ibi7).add(back, home)

#контакты из категории "Интернет магазин"
ikb21 = InlineKeyboardMarkup(row_width=2)
ibj1 = InlineKeyboardButton(text='Faberlic', callback_data='j1')
ibj2 = InlineKeyboardButton(text='Wildberries', callback_data='j2')
ibj3 = InlineKeyboardButton(text='Ozon', callback_data='j3')
#ibj4 = InlineKeyboardButton(text='РосТех', callback_data='i4') reserved
#ibj5 = InlineKeyboardButton(text='РЭС', callback_data='i5') reserved
#ibj6 = InlineKeyboardButton(text='Храм Шалинское', callback_data='i6') reserved
#ibj7 = InlineKeyboardButton(text='Энергосбыт', callback_data='i7') reserved
ikb21.add(ibj1, ibj2, ibj3).add(back, home)

#Назад в автотематику
back_auto = InlineKeyboardButton(text='Назад 🔙', callback_data='back_auto')
ikb12 = InlineKeyboardMarkup(row_width=2)
ikb12.add(back_auto, home)

#Назад в госучереждения
back_gos = InlineKeyboardButton(text='Назад 🔙', callback_data='back_gos')
ikb13 = InlineKeyboardMarkup(row_width=2)
ikb13.add(back_gos, home)

#Назад в деньги
back_money = InlineKeyboardButton(text='Назад 🔙', callback_data='back_money')
ikb14 = InlineKeyboardMarkup(row_width=2)
ikb14.add(back_money, home)

#Назад в продажи
back_shop = InlineKeyboardButton(text='Назад 🔙', callback_data='back_shop')
ikb15 = InlineKeyboardMarkup(row_width=2)
ikb15.add(back_shop, home)

#Назад в ремонт
back_make = InlineKeyboardButton(text='Назад 🔙', callback_data='back_make')
ikb16 = InlineKeyboardMarkup(row_width=2)
ikb16.add(back_make, home)

#Назад в интернет
back_internet = InlineKeyboardButton(text='Назад 🔙', callback_data='back_internet')
ikb17 = InlineKeyboardMarkup(row_width=2)
ikb17.add(back_internet, home)

#Назад в услуги
back_service = InlineKeyboardButton(text='Назад 🔙', callback_data='back_service')
ikb18 = InlineKeyboardMarkup(row_width=2)
ikb18.add(back_service, home)

#Назад в прочее
back_other = InlineKeyboardButton(text='Назад 🔙', callback_data='back_other')
ikb19 = InlineKeyboardMarkup(row_width=2)
ikb19.add(back_other, home)

#Назад в информацию
back_info = InlineKeyboardButton(text='Назад 🔙', callback_data='back_info')
ikb20 = InlineKeyboardMarkup(row_width=2)
ikb20.add(back_info, home)

#Назад в интернет магазины
back_internetshop = InlineKeyboardButton(text='Назад 🔙', callback_data='back_internetshop')
ikb22 = InlineKeyboardMarkup(row_width=2)
ikb22.add(back_internetshop, home)