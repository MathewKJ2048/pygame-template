from game import *
from controls import *
from render import *


def init():
	pygame.init()
	pygame.display.set_caption(NAME)
	pygame.display.set_icon(pygame.image.load("assets/icon.ico"))
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	return screen


def play():
	game = Game()
	screen = init()
	while game.running:
		dt = CLOCK.tick(MAX_FRAME_RATE)/1000

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.exit()
			elif event.type == pygame.KEYDOWN:
				process_keydown_event(event,game)
		process_pressed_keys(game)

		game.evolve(dt)
		screen.blit(render(game),(0,0))
		pygame.display.flip()

play()