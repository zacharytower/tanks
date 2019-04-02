import pygame

class Level:
	def __init__(self, block_layout, tank_list):
		self.image = pygame.Surface((600,600))

		for i, row in enumerate(block_layout):
			self.block_layout.append(list())
			for block in row:
				self.block_layout[i] = block

		self.tank_list = tank_list


	def draw_level(self):

		for x, row in enumerate(self.block_layout):
			for y, item in enumerate(row):

				self.image.blit(item.image, (24 * x, 24 * y))

		for tank in self.tank_list:
			self.image.blit(tank, tank.pos)

	