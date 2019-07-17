import time
import eel
import moisture_reading
from controller import Controller
from plant import Plant

moisture_reading.create_table()
app = Controller()

print(app.welcome())

moisture_reading = app.soil_moisture(Plant)
print(moisture_reading)

eel.init('web')
eel.start('index.html')
