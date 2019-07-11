import board
import busio
from adafruit_seesaw.seesaw import Seesaw

class Plant():

    def soil_moisture(self):

        i2c_bus = busio.I2C(board.SCL, board.SDA)

        ss = Seesaw(i2c_bus, addr=0x36)

        return ss.moisture_read()

        # while True:
            
        #     # temp = ss.get_temp()
        #     try:
        #         f = open("moisture_readings.txt", "a")
        #         f.write("moisture: " + str(moisture_level) + "\n")
        #     finally:
        #         f.close()	
        #     print("moisture: " + str(moisture_level))
        #     time.sleep(60)
        #     return moisture_level
