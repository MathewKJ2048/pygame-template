from lib import *

def process_pressed_keys(game):
	pressed_keys = pygame.key.get_pressed()
	"""
	if pressed_keys[pygame.K_q]:
		game.running = False
	"""
	game.camera.v = O
	if pressed_keys[pygame.K_UP]:
		game.camera.v = game.camera.n
	if pressed_keys[pygame.K_DOWN]:
		game.camera.v = -game.camera.n
	if pressed_keys[pygame.K_LEFT]:
		game.camera.n = rotate(game.camera.n,0.1)
	if pressed_keys[pygame.K_RIGHT]:
		game.camera.n = rotate(game.camera.n,-0.1)

	
def process_keydown_event(event,game):
	
	"""
	if event.key == pygame.K_q:
		game.running = False
	"""
	pass
	