from lib import *

"""
Particles have a time, r, v, a and a lifetime
radius is a function
color is a function
"""

class Particle:
	def __init__(self,r=O,v=O,a=O,lifetime=1):
		self.time = 0
		self.r = r
		self.v = v
		self.a = a
		self.lifetime = lifetime
	pass



"""
Explosion produces a list of particles
Explosion makes particles with radius min to max
lifetime from min to max
velocity from min to max
phi in range[phi]
theta in range[theta]
color in [colorlist],[relative weights]
"""