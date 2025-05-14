from lib import *


class Object:

	def __init__(self,r=O,v=O,a=O,theta=0,phi=0,w_theta=0,w_phi=0):
		self.time = 0
		self.r = r
		self.v = v
		self.a = a
		self.theta = theta
		self.phi = phi
		self.w_theta = w_theta
		self.w_phi = w_phi

	def evolve(self,dt,game):
		self.r+=self.v*dt
		self.theta+=self.w_theta*dt
		self.phi+=self.w_phi*dt
		self.v+=self.a*dt
		self.time+=dt

	def get_lines(self):
		N = 4
		base = [unit_vector(i*TAU/N) for i in range(N)]
		return make_polygon(base,color=CYAN)+join_polygon_point(base,K,color=MAGENTA)

	