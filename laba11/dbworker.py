from vedis import Vedis

from .constants import *


# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    with Vedis(db_file) as db:
        try:
            return db[user_id].decode()  # Если используете Vedis версии ниже, чем 0.7.1, то .decode() НЕ НУЖЕН
        except KeyError:  # Если такого ключа почему-то не оказалось
            return States.S_START.value  # значение по умолчанию - начало диалога


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with Vedis(db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False