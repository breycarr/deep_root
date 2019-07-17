import time
import eel
import moisture_reading
from controller import Controller
from plant import Plant
from light import Light

moisture_reading.create_table()
app = Controller()
plant = Plant()

print(app.welcome())

moisture_reading = app.soil_moisture(Plant)
app.light(moisture_reading, Light)
print(moisture_reading)

eel.init('web')
eel.start('index.html')

# while True:
# moisture_reading = app.soil_moisture(Plant)
# app.light(moisture_reading, Light)
# time.sleep(60)

