import pygame

class Block(pygame.sprite.Sprite):


	'''
	Blocks comprise the entire grid of a level.
	Any tank's movement is defined by the block that
	they are under or trying to move to.
	'''
	def __init__(self,
		traversable,
		brittle,
		bullet_travel,
		sprite
		):

		super().__init__()
		self.image = pygame.image.load(filename).convert()
		self.rect = self.image.get_rect()

		self.traversable = traversable
		self.brittle = brittle
		self.bullet_travel = bullet_travel

	
		


