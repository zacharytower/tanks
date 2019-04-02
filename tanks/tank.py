import pygame

class Tank(pygame.sprite.Sprite):

	def __init__(self, filename, x_pos, y_pos):

		super().__init__()
		self.image = pygame.image.load(filename).convert()
		self.rect = self.image.get_rect()
		self.pos = (x_pos, y_pos)

	def move(self, speed = (1,1)):
		self.pos = (z + speed[i] for i, z in enumerate(self.pos))
		self.wrap_pos()

	def wrap_pos(self):
		# wrap the position to the screen dimensions
		# (which will always be 600 by 600 pixels)

		# I know this is an ugly implementation
		# of wrapping, but I really don't have
		# the willpower to figure out a more
		# robust way to do it :p

		if self.pos[0] < 0:
			self.pos = (0, self.pos[1])

		if self.pos[1] < 0:
			self.pos = (self.pos[0], 0)

		if self.pos[0] >= 600:
			self.pos = (599, self.pos[1])

		if self.pos[1] >= 600:
			self.pos = (self.pos[0], 599)

	

