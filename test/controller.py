class Controller():

	def welcome(self):
		return "Welcome to Deep Root"


	def soil_moisture(self, plant_class):
		plant = plant_class()
		return plant.soil_moisture()

	
	def light(self, soil_moisture, light_class):
		light = light_class()
		if soil_moisture > 800:
			light.blue()
		elif soil_moisture < 500:
			light.red()
		else: 
			light.green()

