class Controller():

	def welcome(self):
		return "Welcome to Deep Root"

	def soil_moisture(self, obj_class):
		plant = obj_class()
		return plant.soil_moisture()