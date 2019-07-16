import board
import busio
import eel
from adafruit_seesaw.seesaw import Seesaw


class Plant():

    def soil_moisture(self):
        soil_sensor = busio.I2C(board.SCL, board.SDA)

        seesaw = Seesaw(soil_sensor, addr=0x36)

        return seesaw.moisture_read()


plant_object = Plant()

@eel.expose
def get_reading_for_eel():
    return plant_object.soil_moisture()
