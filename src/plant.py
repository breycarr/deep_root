import board
import busio
from adafruit_seesaw.seesaw import Seesaw


class Plant():

    def soil_moisture(self):
        soil_sensor = busio.I2C(board.SCL, board.SDA)

        seesaw = Seesaw(soil_sensor, addr=0x36)

        return seesaw.moisture_read()
