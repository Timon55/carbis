import sqlite3
import sys
try:
    connection = sqlite3.connect('user_settings.db', timeout=20)
    cursor = connection.cursor()
    print('Введите координаты')

except sqlite3.Error as error:
    print('* Ошибка подключения к базе данных *')
    print(error)
