from colors import *

class Line:
	def __init__(self,start,end,color=WHITE,thickness=2):
		self.start = start
		self.end = end
		self.color = color
		self.thickness = thickness


def make_polygon(base_list,color=WHITE,thickness=2):
	return [
		Line(base_list[i],base_list[(i+1)%len(base_list)],color=color,thickness=thickness) 
	for i in range(len(base_list))]

def join_polygons(l1,l2,offset=0,color=WHITE,thickness=2):
	N = len(l1)
	offset = offset+2*N
	return [Line(l1[i],l2[(i+offset)%N],color=color,thickness=thickness) for i in range(N)]

def join_polygon_point(l,u,color=WHITE,thickness=2):
	return [Line(t,u,color=color,thickness=thickness) for t in l]