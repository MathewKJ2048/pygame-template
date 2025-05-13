from lib import *


"""
parameters:
r = position
n = vector pointing along direction to look at
up = unit vector that determines up direction of screen
zoom = scaling factor for an object
"""

class Camera:
	def __init__(self,r=O,n=I,p=K,zoom=100):
		self.r = -10*I
		self.n = n
		self.up = p
		self.zoom = zoom
