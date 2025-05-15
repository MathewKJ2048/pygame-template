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

def debug_transcript_text():
	d = get_debug_transcript()
	s = ""
	for k in d:
		s+=k+":"+str(d[k])+"\n"
	return s

def message_log_text():
	ml = get_message_log()
	messages = ["placeholder"]
	nums = [0]
	for m in ml:
		top = messages[-1]
		if m == top:
			nums[-1]+=1
		else:
			messages.append(m)
			nums.append(1)
	s = ""
	for i in range(1,len(messages)):
		s+=messages[i]+":"+str(nums[i])+"\n"
	return s



def render_object(o,camera,surface):
	for p in o.get_lines():
		pygame.draw.line(surface,p.color,project(p.start,camera),project(p.end,camera),width=p.thickness)

def render_debug_data(surface):
	text_surface = DEFAULT_FONT.render(debug_transcript_text(), True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.center = (text_rect.width//2, HEIGHT - text_rect.height//2)
	surface.blit(text_surface,text_rect)
	text_surface = DEFAULT_FONT.render(message_log_text(), True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.center = (WIDTH - text_rect.width//2, HEIGHT - text_rect.height//2)
	surface.blit(text_surface,text_rect)
	pass

def render(game):
	surface = pygame.Surface((WIDTH,HEIGHT))
	surface.fill(BACKGROUND)
	for o in game.objects:
		render_object(o,game.camera,surface)
	render_debug_data(surface)
	return surface
