import pygame
from config import *
import shelve
import random
from screenshot import screenshota as scrt

pygame.init()

pygame.mixer.music.load(MUSIC)

pygame.mixer.music.play()

asp = []

'''def create_window(w, h):
	screen = pygame.display.set_mode((w, h),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
	return screen

sc = create_window(WIDTH, HEIGHT)'''
clock = pygame.time.Clock()

class Player:
	def __init__(self, x, y, speed, col):
		self.x = x
		self.y = y
		self.speed = speed
		self.col = col
		self.jump_on = False
		self.jump_counter = 30
	def draw(self):
		pygame.draw.rect(sc, self.col, (self.x, self.y, 120, 200))
	def jump(self):
		if self.jump_counter >= -30:
			self.y -= self.jump_counter
			self.jump_counter -= 1
		else:
			self.jump_counter = 30
			self.jump_on = False
	def get_collision(self, target):
		if abs(self.x - target.x) <= 120 and abs(self.y - target.y) <= 200:
			return True
		else:
			return False
	def check_score(self, target):
		if self.x == target.x and target.y - self.y > 200:
			return True
		else:
			return False

class Platform:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.col = GREEN
	def draw(self):
		pygame.draw.rect(sc, self.col, (self.x, self.y, self.w, self.h))

class Cactus:
	def __init__(self, x, y, h):
		self.x = x
		self.y = y
		self.h = h
		self.col = BLUE
	def draw(self):
		pygame.draw.rect(sc, self.col, (self.x, self.y, 120, self.h))

class Txt:
	def __init__(self, x, y, val):
		self.x = x
		self.y = y
		self.val = val
		self.col = WHITE
	def draw(self):
		fontObj = pygame.font.Font(None, 50)
		textSurfaceObj = fontObj.render(self.val, True, self.col)
		sc.blit(textSurfaceObj, [self.x, self.y])

class Save:
	def __init__(self, max_score):
		self.file = shelve.open('data')
		self.max_score = max_score
	def save(self, max_score, amount):
		self.file['max_score'] = max_score
		self.file['amount'] = amount
	def load(self):
		try:
			return [self.file['max_score'], self.file['amount']]
		except:
			return [0, 0]
	def __del__(self):
		self.file.close()

max_score = 0

save_var = Save(max_score)

score = 0
max_score = save_var.load()[0]

ball = Player(100, HEIGHT-300, 20, RED)
asp.append(ball)

plat = Platform(0, HEIGHT-100, 2000, 300)
asp.append(plat)

a = Cactus(3000, HEIGHT-300, 200)
cacti = []
cacti.append(a)
asp.append(a)

scoretxt = Txt(0, 0, 'SCORE: ' + str(score))
asp.append(scoretxt)

maxtxt = Txt(1000, 0, 'MAX SCORE: ' + str(max_score))
asp.append(maxtxt)

hold_left = False

# scrt.amount = save_var.load()[1]

run = True
pause = False
while run:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				ball.jump_on = True
			elif event.key == pygame.K_ESCAPE:
				run = False
			elif event.key == pygame.K_p:
				if pause == False:
					pause = True
				else:
					pause = False
			elif event.key == pygame.K_s:
				scrt.make_sc = True
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if click[0] and not hold_left:
		if scrt.make_sc:
			scrt.set_lt(mouse[0], mouse[1])
		hold_left = True
	if click[0] and hold_left:
		nnm = scrt.incr_area(mouse[0], mouse[1])
		pygame.draw.rect(sc, WHITE, nnm, 1)
	if hold_left and not click[0]:
		if scrt.make_sc:
			scrt.end_area()
		hold_left = False
	if pause != True:
		if ball.jump_on:
			ball.jump()
		for cactus in cacti:
			cactus.x -= ball.speed
		for cactus in cacti:
			collision = ball.get_collision(cactus)
			if collision:
				run = False
		for cactus in cacti:
			scoreplus = ball.check_score(cactus)
			if scoreplus:
				score += 1
			scoretxt.val = 'SCORE: ' + str(score)
		if score > max_score:
			max_score = score
		maxtxt.val = 'MAX SCORE: ' + str(max_score)
		for cactus in cacti:
			if cactus.x < -120:
				cactus.x = 1900
				cactus.h = random.randint(100, 300)
				cactus.y = HEIGHT-(100 + cactus.h)
		r = random.randint(0, 700)
		if 0 <= r <= 1:
			a = Cactus(4000, HEIGHT-300, 200)
			cacti.append(a)
			asp.append(a)
	sc.fill(BLACK)
	for i in asp:
		i.draw()
	pygame.display.flip()

if score > max_score:
	max_score = score

save_var.save(max_score, scrt.amount)

pygame.quit()