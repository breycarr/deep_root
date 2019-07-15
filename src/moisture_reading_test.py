import moisture_reading
import sqlite3

conn = sqlite3.connect('soil_moisture_test.db')

c = conn.cursor()

moisture_reading.create_table(c)

class TestDatabase():

    def test_create_reading(self):
        reading = moisture_reading.create(700, c)
        assert reading == (1, 700)
