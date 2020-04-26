import pygame

WIDTH = 1280
				# screen resolution
HEIGHT = 720



FPS = 60

def create_window(w, h):
	screen = pygame.display.set_mode((w, h),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
	return screen

sc = create_window(WIDTH, HEIGHT)

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

RED = (255, 0, 0)
						# colors
GREEN = (0, 255, 0)

BLUE = (0, 0, 255)



LANG = 'RUS' # change to "ENG" for set english language



MUSIC = 'audio/main-music.mp3' # you can change music