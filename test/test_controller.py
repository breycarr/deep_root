from controller import Controller

class MockPlant():
	def soil_moisture(self):
		return 900

class TestController(object):

	def test_welcome_message(self):
		controller = Controller()
		assert controller.welcome() == "Welcome to Deep Root"

	
	def test_soil_moisture_reading(self):
		controller = Controller()
		assert controller.soil_moisture(MockPlant) == 900
