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
		self.camera.r+=self.camera.v*dt

		self.debug_logs(dt)

	def exit(self):
		self.running = False

	def debug_logs(self,dt):
		log("framerate:",round(1/dt))
		log("camera_n",self.camera.n)