import time
import eel
import moisture_reading
from plant import Plant

moisture_reading.create_table()

eel.init('web')
eel.start('index.html')
