from lib import *
from object import *
from camera import *

class Game:
	def __init__(self):
		self.objects = [Object()]
		self.camera = Camera()
		self.running = True

	def evolve(self,dt):
		for o in self.objects:
			o.evolve(dt,self)

	def exit(self):
		self.running = False