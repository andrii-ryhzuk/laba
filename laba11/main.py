import telebot

from . import dbworker as db
from .constants import *
from .exchanger import exchange

bot = telebot.TeleBot(TOKEN)

start_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
empty_keyboard = telebot.types.ReplyKeyboardRemove()

start_keyboard.row(button_captions[1], button_captions[3])
start_keyboard.row(button_captions[2], button_captions[4])

exchange_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
exchange_keyboard.row(button_captions[5])


@bot.message_handler(commands=['start'])
def handle_start_command(message):
    state = db.get_current_state(message.chat.id)
    print(state)    # debug current state
    if state == States.S_ENTER_VALUE.value:
        db.set_state(message.chat.id, States.S_CHOOSE_BTN.value)
        bot.send_message(message.chat.id, choose_btn, reply_markup=start_keyboard)
    elif state == States.S_BACK.value:
        bot.send_message(message.chat.id, back__message)
    else:
        bot.send_message(message.chat.id, hello_message, reply_markup=start_keyboard)
        db.set_state(message.chat.id, States.S_CHOOSE_BTN.value)


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == States.S_CHOOSE_BTN.value)
def user_choose_btn(message):
    global user_choice
    if message.text == button_captions[1]:
        user_choice = 1
        bot.send_message(
            message.chat.id,
            f"{for_exchange_message}(сумма в {button_captions[user_choice].split('-')[0]})",
            reply_markup=empty_keyboard
        )
    elif message.text == button_captions[2]:
        user_choice = 2
        bot.send_message(
            message.chat.id,
            f"{for_exchange_message}(сумма в {button_captions[user_choice].split('-')[0]})",
            reply_markup=empty_keyboard
        )
    elif message.text == button_captions[3]:
        user_choice = 3
        bot.send_message(
            message.chat.id,
            f"{for_exchange_message}(сумма в {button_captions[user_choice].split('-')[0]})",
            reply_markup=empty_keyboard
        )
    elif message.text == button_captions[4]:
        user_choice = 4
        bot.send_message(
            message.chat.id,
            f"{for_exchange_message}(сумма в {button_captions[user_choice].split('-')[0]})",
            reply_markup=empty_keyboard
        )
    db.set_state(message.chat.id, States.S_ENTER_VALUE.value)


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == States.S_ENTER_VALUE.value)
def user_entering_value(message):
    if not message.text.isdigit():
        bot.send_message(
            message.chat.id,
            error_message
        )
    else:
        bot.send_message(
            message.chat.id,
            f"{after_exchange_message}{button_captions[user_choice]}\nСумма: "
            f"{str(exchange(user_choice, float(message.text)))} {button_captions[user_choice].split('-')[1]}",
            reply_markup=exchange_keyboard
        )
        db.set_state(message.chat.id, States.S_BACK.value)


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == States.S_BACK.value)
def user_back(message):
    if message.text == button_captions[5]:
        bot.send_message(
            message.chat.id,
            hello_message,
            reply_markup=start_keyboard
        )
        db.set_state(message.chat.id, States.S_CHOOSE_BTN.value)
    else:
        bot.send_message(
            message.chat.id,
            error_message
        )


bot.polling()
