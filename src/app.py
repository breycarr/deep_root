import time
from controller import Controller
from plant import Plant
from light import Light

app = Controller()

print(app.welcome())

while True:
    moisture_reading = app.soil_moisture(Plant)
    app.light(moisture_reading, Light)
    time.sleep(60)
