import eel
import sqlite3
from datetime import datetime
from plant import Plant

conn = sqlite3.connect('soil_moisture.db')

c = conn.cursor()

def create_table(cursor = c):
    cursor.execute("""CREATE TABLE IF NOT EXISTS readings (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   reading INTEGER,
                   datetime TEXT
                   )""")

@eel.expose
def create(reading, current_time = datetime.now(), cursor = c):
    with conn:
        datetime_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(f"INSERT INTO readings(reading, datetime) VALUES ({reading}, '{datetime_string}')")
        query = f'SELECT * FROM readings WHERE id={cursor.lastrowid}'
        res = cursor.execute(query)
        return res.fetchall()[0]

@eel.expose
def all(cursor = c):
    cursor.execute('SELECT * FROM readings')
    return cursor.fetchall()
