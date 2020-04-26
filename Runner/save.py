import shelve
from main import *

class Save:
	def __init__(self):
		self.file = shelve.open('data')
		self.max_score = max_score
	def save(self):
		self.file['max_score'] = self.max_score
	def load(self):
		try:
			return self.file['max_score']
		except:
			return 0
	def __del__(self):
		self.file.close()