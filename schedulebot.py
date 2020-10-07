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
