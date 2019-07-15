import eel
import sqlite3

conn = sqlite3.connect('soil_moisture.db')

c = conn.cursor()

def create_table(cursor = c):
    cursor.execute("""CREATE TABLE IF NOT EXISTS readings (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   reading INTEGER
                   )""")


# @eel.expose
def create(reading, cursor = c):
    with conn:
        cursor.execute(f'INSERT INTO readings(reading) VALUES ({reading})')
        query = f'SELECT * FROM readings WHERE id={cursor.lastrowid}'
        res = cursor.execute(query)
        return res.fetchall()[0]
#
# @eel.expose
# def all():
#     c.execute('SELECT * FROM readings')
#     return c.fetchall()
