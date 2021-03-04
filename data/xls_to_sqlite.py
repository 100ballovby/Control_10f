import sqlite3
import pandas as pd

con = sqlite3.connect('../buildings.db')
# подключаемся к БД my_music
wb = pd.read_excel('book.xlsx', sheet_name=None)
# читаем excel файл, не указывая названия листов в нем

for sheet in wb:
    """просматриваем каждый лист внутри таблицы"""
    wb[sheet].to_sql(sheet, con, index=False)

con.commit()  # применить изменения
con.close()  # закрываю подключение к БД