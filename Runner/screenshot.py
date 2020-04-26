import pygame
from config import *

class Screenshot:
	def __init__(self, name):
		self.name = name
		self.tlx = self.tly = 0
		self.brx = self.bry = 0
		self.width = self.height = 0
		self.make_sc = False
		self.amount = 0
	def set_lt(self, x, y):
		self.ltx = x
		self.lty = y
	def incr_area(self, x, y):
		self.brx = x
		self.bry = y
		self.width = self.brx - self.tlx
		self.height = self.bry - self.tly
		return (self.tlx, self.tly, self.width, self.height)
	def end_area(self):
		image = pygame.Surface((self.width, self.height))
		image.blit(sc, (0, 0), (self.tlx, self.tly, self.width, self.height))
		pygame.image.save(image, "{}{}.png".format(self.name, self.amount))
		self.amount += 1
		self.make_sc = False

screenshota = Screenshot('screenshot')