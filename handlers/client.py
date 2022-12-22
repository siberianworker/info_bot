from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_kb
from information import base

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, base.welcome, reply_markup=client_kb.ikb)

#отлавливает контакты
@dp.callback_query_handler(lambda callback: "contacts" in callback.data)
async def contacts_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb2)

#отлавливает категорию "Автотематика"
@dp.callback_query_handler(lambda callback: "s1" in callback.data)
async def automobile_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb3)

#отлавливает информацию
@dp.callback_query_handler(lambda callback: "info" in callback.data)
async def info_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb4)

#отлавливает категорию "Госучереждения"
@dp.callback_query_handler(lambda callback: "s2" in callback.data)
async def gos_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb5)

#отлавливает категорию "Деньги"
@dp.callback_query_handler(lambda callback: "s3" in callback.data)
async def money_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb6)

#отлавливает категорию "Продажи"
@dp.callback_query_handler(lambda callback: "s4" in callback.data)
async def shop_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb7)

#отлавливает категорию "Ремонт"
@dp.callback_query_handler(lambda callback: "s5" in callback.data)
async def make_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb8)

#отлавливает категорию "Интернет"
@dp.callback_query_handler(lambda callback: "s6" in callback.data)
async def voice_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb9)

#отлавливает категорию "Интернет магазины"
@dp.callback_query_handler(lambda callback: "s9" in callback.data)
async def voice_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb21)

#отлавливает категорию "Услуги"
@dp.callback_query_handler(lambda callback: "s7" in callback.data)
async def remake_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb10)

#отлавливает категорию "Прочее"
@dp.callback_query_handler(lambda callback: "s8" in callback.data)
async def other_callback(callback):
    await callback.message.edit_reply_markup(client_kb.ikb11)

#отлавливает все callback
@dp.callback_query_handler()
async def first_call(callback : types.CallbackQuery):
    #Контакты  из категории "Автотематика"
    if callback.data == 't1': #Автовокзал
        await callback.message.edit_text(text=base.bus_station, reply_markup=client_kb.ikb12)
    elif callback.data == 't2': #Автомойки
        await callback.message.edit_text(text=base.auto_clear, reply_markup=client_kb.ikb12)
    elif callback.data == 't3': #Автосервис
        await callback.message.edit_text(text=base.auto_service, reply_markup=client_kb.ikb12)
    elif callback.data == 't4': #Автошкола
        await callback.message.edit_text(text=base.auto_school, reply_markup=client_kb.ikb12)
    elif callback.data == 't5': #Автоэлектрик
        await callback.message.edit_text(text=base.auto_elect, reply_markup=client_kb.ikb12)
    elif callback.data == 't6': #Грузовое такси
        await callback.message.edit_text(text=base.freight_taxi, reply_markup=client_kb.ikb12)
    elif callback.data == 't7': #Куплю авто
        await callback.message.edit_text(text=base.parts, reply_markup=client_kb.ikb12)
#    elif callback.data == 't8': #
#        await callback.message.edit_text(text=base.buy_auto, reply_markup=client_kb.ikb12)
    elif callback.data == 't9': #Манипулятор
        await callback.message.edit_text(text=base.manipulator, reply_markup=client_kb.ikb12)
    elif callback.data == 't10': #Мини экскаватор
        await callback.message.edit_text(text=base.excavator, reply_markup=client_kb.ikb12)
    elif callback.data == 't11': #Отогрев авто
        await callback.message.edit_text(text=base.heating_auto, reply_markup=client_kb.ikb12)
    elif callback.data == 't12': #Полировка авто
        await callback.message.edit_text(text=base.polishing, reply_markup=client_kb.ikb12)
    elif callback.data == 't13': #Такси
        await callback.message.edit_text(text=base.taxi, reply_markup=client_kb.ikb12)
    elif callback.data == 't14': #Техосмотр
        await callback.message.edit_text(text=base.techview, reply_markup=client_kb.ikb12)
    elif callback.data == 't15': #Трезвый водитель
        await callback.message.edit_text(text=base.driver, reply_markup=client_kb.ikb12)
    elif callback.data == 't16': #Услуги самослава
        await callback.message.edit_text(text=base.dump_truck, reply_markup=client_kb.ikb12)
    elif callback.data == 't17': #Шиномонтаж
        await callback.message.edit_text(text=base.wheels, reply_markup=client_kb.ikb12)
    elif callback.data == 't18': #Штрафстоянка
        await callback.message.edit_text(text=base.fine_parking, reply_markup=client_kb.ikb12)
    elif callback.data == 't19': #Эвакуатор
        await callback.message.edit_text(text=base.evic, reply_markup=client_kb.ikb12)

    #Контакты из категории "Госучереждения"
    elif callback.data == 'a1': #Библиотека
        await callback.message.edit_text(text=base.bibliot, reply_markup=client_kb.ikb13)
    elif callback.data == 'a2': #Гибдд Шалинское
        await callback.message.edit_text(text=base.gibdd, reply_markup=client_kb.ikb13)
    elif callback.data == 'a3': #Дом творчества
        await callback.message.edit_text(text=base.house_creat, reply_markup=client_kb.ikb13)
    elif callback.data == 'a4': #ЕДДС
        await callback.message.edit_text(text=base.edds, reply_markup=client_kb.ikb13)
    elif callback.data == 'a5': #ЖКХ
        await callback.message.edit_text(text=base.jkh, reply_markup=client_kb.ikb13)
    elif callback.data == 'a6': #ЗАГС
        await callback.message.edit_text(text=base.zags, reply_markup=client_kb.ikb13)
    elif callback.data == 'a7': #Лесничество
        await callback.message.edit_text(text=base.forestry, reply_markup=client_kb.ikb13)
    elif callback.data == 'a8': #Лесопожарный центр
        await callback.message.edit_text(text=base.fores_centre, reply_markup=client_kb.ikb13)
    elif callback.data == 'a9': #Манская РБ
        await callback.message.edit_text(text=base.man_rb, reply_markup=client_kb.ikb13)
    elif callback.data == 'a10': #«Медицина катастроф» Кускун
        await callback.message.edit_text(text=base.meddis, reply_markup=client_kb.ikb13)
    elif callback.data == 'a11': #Медицинское такси
        await callback.message.edit_text(text=base.med_taxi, reply_markup=client_kb.ikb13)
    elif callback.data == 'a12': #Мировой суд
        await callback.message.edit_text(text=base.magist, reply_markup=client_kb.ikb13)
    elif callback.data == 'a13': #МФЦ
        await callback.message.edit_text(text=base.mfc, reply_markup=client_kb.ikb13)
    elif callback.data == 'a14': #Налоговая №26
        await callback.message.edit_text(text=base.tax, reply_markup=client_kb.ikb13)
    elif callback.data == 'a15': #Отделение полиции
        await callback.message.edit_text(text=base.police, reply_markup=client_kb.ikb13)
    elif callback.data == 'a16': #Паспортный стол
        await callback.message.edit_text(text=base.passport, reply_markup=client_kb.ikb13)
    elif callback.data == 'a17': #Пенсионный фонд
        await callback.message.edit_text(text=base.pen_fund, reply_markup=client_kb.ikb13)
    elif callback.data == 'a18': #Пожарная Шалинская
        await callback.message.edit_text(text=base.fireman, reply_markup=client_kb.ikb13)
    elif callback.data == 'a19': #ПОЧТА
        await callback.message.edit_text(text=base.pochta, reply_markup=client_kb.ikb13)
    elif callback.data == 'a20': #Сельский совет
        await callback.message.edit_text(text=base.sel_sovet, reply_markup=client_kb.ikb13)
    elif callback.data == 'a21': #Соцзащита
        await callback.message.edit_text(text=base.socz, reply_markup=client_kb.ikb13)
    elif callback.data == 'a22': #Судебные приставы
        await callback.message.edit_text(text=base.bailiffs, reply_markup=client_kb.ikb13)
    elif callback.data == 'a23': #Управление сельхоз
        await callback.message.edit_text(text=base.upr_sel, reply_markup=client_kb.ikb13)
    elif callback.data == 'a24': #Центр занятости
        await callback.message.edit_text(text=base.emp_center, reply_markup=client_kb.ikb13)
    elif callback.data == 'a25': #Шалинская "ДШИ"
        await callback.message.edit_text(text=base.dchi, reply_markup=client_kb.ikb13)
    elif callback.data == 'a26': #Шалинский архив
        await callback.message.edit_text(text=base.arhiv, reply_markup=client_kb.ikb13)
    elif callback.data == 'a27': #Школа
        await callback.message.edit_text(text=base.shcool, reply_markup=client_kb.ikb13)

    #Контакты из категории "Деньги"
    elif callback.data == 'b1': #Банк
        await callback.message.edit_text(text=base.bank, reply_markup=client_kb.ikb14)
    elif callback.data == 'b2': #Займы
        await callback.message.edit_text(text=base.zaem, reply_markup=client_kb.ikb14)
    elif callback.data == 'b3': #Страхование
        await callback.message.edit_text(text=base.save, reply_markup=client_kb.ikb14)

    #Контакты из категории "Продажи"
    elif callback.data == 'd1': #Аптеки
        await callback.message.edit_text(text=base.pharmacies, reply_markup=client_kb.ikb15)
    elif callback.data == 'd2': #Горбыль
        await callback.message.edit_text(text=base.gorbil, reply_markup=client_kb.ikb15)
    elif callback.data == 'd3': #Доставка
        await callback.message.edit_text(text=base.dostavka, reply_markup=client_kb.ikb15)
    elif callback.data == 'd4': #Дрова
        await callback.message.edit_text(text=base.firewood, reply_markup=client_kb.ikb15)
    elif callback.data == 'd5': #Кафе
        await callback.message.edit_text(text=base.cafe, reply_markup=client_kb.ikb15)
    elif callback.data == 'd6': #Котлы
        await callback.message.edit_text(text=base.kotel, reply_markup=client_kb.ikb15)
    elif callback.data == 'd7': #Магазины
        await callback.message.edit_text(text=base.shop, reply_markup=client_kb.ikb15)
    elif callback.data == 'd8': #Мебель
        await callback.message.edit_text(text=base.mebel, reply_markup=client_kb.ikb15)
    elif callback.data == 'd10': #Пиломатериал
        await callback.message.edit_text(text=base.lumber, reply_markup=client_kb.ikb15)
    elif callback.data == 'd11': #Прием металла
        await callback.message.edit_text(text=base.metal, reply_markup=client_kb.ikb15)
    elif callback.data == 'd12': #Скот
        await callback.message.edit_text(text=base.skot, reply_markup=client_kb.ikb15)
    elif callback.data == 'd13': #Суши
        await callback.message.edit_text(text=base.sushi, reply_markup=client_kb.ikb15)
    elif callback.data == 'd14': #Уголь
        await callback.message.edit_text(text=base.coal, reply_markup=client_kb.ikb15)
    elif callback.data == 'd15': #Цветы-светильники
        await callback.message.edit_text(text=base.make_light, reply_markup=client_kb.ikb15)
    elif callback.data == 'd16': #Шашлык
        await callback.message.edit_text(text=base.shashlik, reply_markup=client_kb.ikb15)
    elif callback.data == 'd17': #Мегафон
        await callback.message.edit_text(text=base.megafon, reply_markup=client_kb.ikb15)
    elif callback.data == 'd18': #МТС
        await callback.message.edit_text(text=base.mts, reply_markup=client_kb.ikb15)
    elif callback.data == 'd19': #Золото
        await callback.message.edit_text(text=base.gold, reply_markup=client_kb.ikb15)
    elif callback.data == 'd20': #Золото
        await callback.message.edit_text(text=base.cakes, reply_markup=client_kb.ikb15)

    #Контакты из категории "Ремонт"
    elif callback.data == 'e1': #Ателье
        await callback.message.edit_text(text=base.atelie, reply_markup=client_kb.ikb16)
    elif callback.data == 'e2': #Внутренняя отделка
        await callback.message.edit_text(text=base.inside_fix, reply_markup=client_kb.ikb16)
    elif callback.data == 'e3': #Мастер на час
        await callback.message.edit_text(text=base.master_hour, reply_markup=client_kb.ikb16)
    elif callback.data == 'e4': #Монтаж
        await callback.message.edit_text(text=base.montag, reply_markup=client_kb.ikb16)
    elif callback.data == 'e5': #Натяжные потолки
        await callback.message.edit_text(text=base.tension_ceilings, reply_markup=client_kb.ikb16)
    elif callback.data == 'e6': #Печник
        await callback.message.edit_text(text=base.stove_man, reply_markup=client_kb.ikb16)
    elif callback.data == 'e7': #Разбор построек
        await callback.message.edit_text(text=base.crash, reply_markup=client_kb.ikb16)
    elif callback.data == 'e8': #Ремонт техники
        await callback.message.edit_text(text=base.repair, reply_markup=client_kb.ikb16)
    elif callback.data == 'e9': #Сантехник
        await callback.message.edit_text(text=base.plumber, reply_markup=client_kb.ikb16)
    elif callback.data == 'e10': #Строительство
        await callback.message.edit_text(text=base.construction, reply_markup=client_kb.ikb16)
    elif callback.data == 'e11': #Электрик
        await callback.message.edit_text(text=base.electrician, reply_markup=client_kb.ikb16)

    #Контакты из категории "Интернет"
    elif callback.data == 'g1': #Фринет
        await callback.message.edit_text(text=base.internet, reply_markup=client_kb.ikb17)
    elif callback.data == 'g2': #Ростелеком
        await callback.message.edit_text(text=base.rostel, reply_markup=client_kb.ikb17)
    elif callback.data == 'g3': #Игра-Сервис
        await callback.message.edit_text(text=base.game_service, reply_markup=client_kb.ikb17)

    #Контакты из категории "Услуги"
    elif callback.data == 'h1': #Аниматор
        await callback.message.edit_text(text=base.animator, reply_markup=client_kb.ikb18)
    elif callback.data == 'h2': #База отдыха
        await callback.message.edit_text(text=base.house_relax, reply_markup=client_kb.ikb18)
    elif callback.data == 'h3': #Бурение
        await callback.message.edit_text(text=base.drilling, reply_markup=client_kb.ikb18)
    elif callback.data == 'h4': #Ветеринары
        await callback.message.edit_text(text=base.veterinar, reply_markup=client_kb.ikb18)
    elif callback.data == 'h5': #Видеонаблюдение
        await callback.message.edit_text(text=base.video, reply_markup=client_kb.ikb18)
    elif callback.data == 'h6': #Доставка баллонов
        await callback.message.edit_text(text=base.gas, reply_markup=client_kb.ikb18)
    elif callback.data == 'h7': #Ключи
        await callback.message.edit_text(text=base.keys, reply_markup=client_kb.ikb18)
    elif callback.data == 'h8': #Кондиционеры
        await callback.message.edit_text(text=base.air_conditioning, reply_markup=client_kb.ikb18)
    elif callback.data == 'h9': #Логопед
        await callback.message.edit_text(text=base.logoped, reply_markup=client_kb.ikb18)
    elif callback.data == 'h10': #Массаж
        await callback.message.edit_text(text=base.massage, reply_markup=client_kb.ikb18)
    elif callback.data == 'h11': #Откачка септиков
        await callback.message.edit_text(text=base.septic, reply_markup=client_kb.ikb18)
    elif callback.data == 'h12': #Парикмахерские
        await callback.message.edit_text(text=base.hairdresser, reply_markup=client_kb.ikb18)
    elif callback.data == 'h13': #Плотник
        await callback.message.edit_text(text=base.carpenter, reply_markup=client_kb.ikb18)
    elif callback.data == 'h14': #Ритуальные услуги
        await callback.message.edit_text(text=base.ritual, reply_markup=client_kb.ikb18)
    elif callback.data == 'h15': #Сварка
        await callback.message.edit_text(text=base.welding, reply_markup=client_kb.ikb18)
    elif callback.data == 'h16': #Стоматолог
        await callback.message.edit_text(text=base.dentist, reply_markup=client_kb.ikb18)
    elif callback.data == 'h17': #Тепловизор
        await callback.message.edit_text(text=base.view_house, reply_markup=client_kb.ikb18)
    elif callback.data == 'h18': #Токарь
        await callback.message.edit_text(text=base.tokar, reply_markup=client_kb.ikb18)
    elif callback.data == 'h19': #Услуги красоты
        await callback.message.edit_text(text=base.beautiful, reply_markup=client_kb.ikb18)
    elif callback.data == 'h20': #Услуги межевания
        await callback.message.edit_text(text=base.surveying, reply_markup=client_kb.ikb18)
    elif callback.data == 'h21': #Фотоуслуги
        await callback.message.edit_text(text=base.foto, reply_markup=client_kb.ikb18)
    elif callback.data == 'h22': #Химчистка
        await callback.message.edit_text(text=base.him_clear, reply_markup=client_kb.ikb18)
    elif callback.data == 'h23': #Чистка подушек
        await callback.message.edit_text(text=base.clear_pillows, reply_markup=client_kb.ikb18)
    elif callback.data == 'h24': #Юруслуги
        await callback.message.edit_text(text=base.lawyer, reply_markup=client_kb.ikb18)
    elif callback.data == 'h25': #Окна
        await callback.message.edit_text(text=base.windows, reply_markup=client_kb.ikb15)

    #Контакты из категории "Прочее"
    elif callback.data == 'i1': #БТИ
        await callback.message.edit_text(text=base.bti, reply_markup=client_kb.ikb19)
    elif callback.data == 'i2': #Метеостанция
        await callback.message.edit_text(text=base.meteo, reply_markup=client_kb.ikb19)
    elif callback.data == 'i3': #Редакция
        await callback.message.edit_text(text=base.newspaper, reply_markup=client_kb.ikb19)
    elif callback.data == 'i4': #Ростех
        await callback.message.edit_text(text=base.rostech, reply_markup=client_kb.ikb19)
    elif callback.data == 'i5': #РЭС
        await callback.message.edit_text(text=base.res, reply_markup=client_kb.ikb19)
    elif callback.data == 'i6': #Храм Шалинское
        await callback.message.edit_text(text=base.hram, reply_markup=client_kb.ikb19)
    elif callback.data == 'i7': #Энергосбыт
        await callback.message.edit_text(text=base.energy, reply_markup=client_kb.ikb19)

    #Информация
    elif callback.data == 'f1': #COVID19
        await callback.message.edit_text(text=base.covid, reply_markup=client_kb.ikb20)
    elif callback.data == 'f2': #Код АТС
        await callback.message.edit_text(text=base.atc, reply_markup=client_kb.ikb20)
    elif callback.data == 'f3': #Экстренные службы
        await callback.message.edit_text(text=base.other, reply_markup=client_kb.ikb20)
    elif callback.data == 'f4': #Расписание автобусов
        await callback.message.edit_text(text=base.bus, reply_markup=client_kb.ikb20)
    elif callback.data == 'f5': #Расписание электричек
        await callback.message.edit_text(text=base.electric, reply_markup=client_kb.ikb20)

    # Информация
    elif callback.data == 'j1':  # Faberlic
        await callback.message.edit_text(text=base.faberlic, reply_markup=client_kb.ikb22)
    elif callback.data == 'j2':  # Wildberries
        await callback.message.edit_text(text=base.wildberries, reply_markup=client_kb.ikb22)
    elif callback.data == 'j3':  # Ozon
        await callback.message.edit_text(text=base.ozon, reply_markup=client_kb.ikb22)
#    elif callback.data == 'f4':  # Расписание автобусов
#        await callback.message.edit_text(text=base.bus, reply_markup=client_kb.ikb20)
#    elif callback.data == 'f5':  # Расписание электричек
#        await callback.message.edit_text(text=base.electric, reply_markup=client_kb.ikb20)


    elif callback.data == 'start':
        await callback.message.edit_text(text=base.welcome, reply_markup=client_kb.ikb)
    elif callback.data == 'back':
        await callback.message.edit_reply_markup(client_kb.ikb2)
    elif callback.data == 'back_auto':
        await callback.message.edit_reply_markup(client_kb.ikb3)
    elif callback.data == 'back_gos':
        await callback.message.edit_reply_markup(client_kb.ikb5)
    elif callback.data == 'back_money':
        await callback.message.edit_reply_markup(client_kb.ikb6)
    elif callback.data == 'back_shop':
        await callback.message.edit_reply_markup(client_kb.ikb7)
    elif callback.data == 'back_make':
        await callback.message.edit_reply_markup(client_kb.ikb8)
    elif callback.data == 'back_internet':
        await callback.message.edit_reply_markup(client_kb.ikb9)
    elif callback.data == 'back_service':
        await callback.message.edit_reply_markup(client_kb.ikb10)
    elif callback.data == 'back_other':
        await callback.message.edit_reply_markup(client_kb.ikb11)
    elif callback.data == 'back_info':
        await callback.message.edit_reply_markup(client_kb.ikb4)
    elif callback.data == 'back_internetshop':
        await callback.message.edit_reply_markup(client_kb.ikb21)




def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
