from camera import *

def project(r,camera):
	side = -camera.n.cross(camera.up)
	rd = r-camera.r
	component_up = rd.dot(camera.up)
	component_side = rd.dot(side)
	component_dist = rd.dot(camera.n)
	X = camera.zoom*component_side/component_dist
	Y = camera.zoom*component_up/component_dist
	return (WIDTH/2+X,HEIGHT/2-Y)

def render_object(o,camera,surface):
	for p in o.get_lines():
		pygame.draw.line(surface,p.color,project(p.start,camera),project(p.end,camera),width=p.thickness)

def render(game):
	surface = pygame.Surface((WIDTH,HEIGHT))
	surface.fill(BACKGROUND)
	for o in game.objects:
		render_object(o,game.camera,surface)
	return surface
