import moisture_reading
import sqlite3
from datetime import datetime

conn = sqlite3.connect('soil_moisture_test.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS readings')

moisture_reading.create_table(c)

frozen_time = datetime.now()
frozen_time_string = frozen_time.strftime('%Y-%m-%d %H:%M:%S')

class MockDateTime():
    def now():
        return frozen_time

class TestDatabase():

    def test_create_reading(self):
        c.execute('DELETE FROM readings')
        reading = moisture_reading.create(700, MockDateTime, c)
        assert reading == (1, 700, frozen_time_string)

    def test_get_all_readings(self):
        c.execute('DELETE FROM readings')
        reading1 = moisture_reading.create(700, MockDateTime, c)
        reading2 = moisture_reading.create(800, MockDateTime, c)
        assert moisture_reading.all(c) == [reading1, reading2]


    def test_format_readings(self):
        c.execute('DELETE FROM readings')
        reading1 = moisture_reading.create(700, MockDateTime, c)
        reading2 = moisture_reading.create(800, MockDateTime, c)
        assert moisture_reading.format_readings(c) == [[700, 800], [frozen_time_string, frozen_time_string]]


