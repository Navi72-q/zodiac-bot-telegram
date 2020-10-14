import  telebot
from telebot import types

commands = { # Описание команд использующиеся в команде /help
    'start': 'Стартовое сообщение и предложение зарегистрироваться',
    'help': 'Информация о боте и списка доступныз команд',
    'registarion': 'Выбор учебного заведения, выбор факультета и группы для вывода информации',
    'send_report': 'отправка обратной свзяи',
    'auto_positing_on <ЧЧ:ММ>': 'Подписка на автоматическую рассылку расписания',
    'auto_positing_off': 'Выключение автоматической отправки расписания'
}

def get_dete_keyboard():
    date_select = types.ReplyKeyboardMarkup(row_width=2, resize_keybord=True, one_time_keyboard=False)
    date_select.row('Сегодня')
    date_select.row('Вся неделя')
    date_select.row('Понедельник', 'Вторник')
    date_select.row('Среда', 'Четверг')
    date_select.row('Пятница', 'Суббота')

    return date_select

# Команда /registration
@bot.message_handler(commands=['registration'])
def command_registration(m):
    registration('reg:stage 1:none', m.chat.id, m.chat.first_name, m.chat.username)

# хелп страница
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = 'Доступны следующие команды \n'
    for key in commands:
        help_text+= '/ ' + key ': '
        help_text += commands[key] + '\n'
        bot.sed_message(cid, help_text, reply_markup=get_dete_keyboard())
        help_text = ('Описание кнопки: \nКнопка "сегодня" выводир расписание на сегодняший день,'
                     'причем с учётом типа недели (числитель/знаменатель, но есть один нюанс: если сегодня воскресенье'
                     'или время больше, чем 19:00, то выводится расписание на следущий день\n')
        bot.sed_message(cid, help_text, reply_markup=get_dete_keyboard())
        guide_url = "YouTube@Bloxa"
        help_text = 'Блее подробную инструкцию и помощь вы сможете узнать написав мне: {}'.format(guide_url)
        bot.sed_message(cid, help_text, reply_markup=get_dete_keyboard())

bot.polling(none_stop=True)

