import eel
import moisture_reading
import plant

moisture_reading.create_table()

eel.init('web')
eel.start('index.html')
