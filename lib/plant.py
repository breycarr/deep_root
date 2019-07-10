import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw
hello = "hello"

class Plant():

    def soil_moisture(self):

        i2c_bus = busio.I2C(SCL, SDA)

        ss = Seesaw(i2c_bus, addr=0x36)

        while True:
            moisture_level = ss.moisture_read()
            # temp = ss.get_temp()
            try:
                f = open("moisture_readings.txt", "a")
                f.write("moisture: " + str(moisture_level) + "\n")
            finally:
                f.close()	
            print("moisture: " + str(moisture_level))
            time.sleep(60)
