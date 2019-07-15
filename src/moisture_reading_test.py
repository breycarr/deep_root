import moisture_reading
import sqlite3
from datetime import datetime

conn = sqlite3.connect('soil_moisture_test.db')

c = conn.cursor()

c.execute('DROP TABLE readings')

moisture_reading.create_table(c)

frozen_time1 = datetime.now()
frozen_time2 = datetime.now()

class TestDatabase():

    def test_create_reading(self):
        c.execute('DELETE FROM readings')
        reading = moisture_reading.create(700, frozen_time1, c)
        assert reading == (1, 700, frozen_time1.strftime('%Y-%m-%d %H:%M:%S'))

    def test_get_all_readings(self):
        c.execute('DELETE FROM readings')
        reading1 = moisture_reading.create(700, frozen_time1, c)
        reading2 = moisture_reading.create(800, frozen_time2, c)
        assert moisture_reading.all(c) == [reading1, reading2]
