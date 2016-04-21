#slippery pizza
#sprites toch check
from livewires import games
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
	"""The pan which you can move with the mouse"""

	def update(self):
		"""Set the object in a cursor position"""

		self.x = games.mouse.x
		self.y = games.mouse.y
		self.check_collide()

	def check_collide(self):
		"""It check collision between pizza and the pan"""

		for pizza in self.overlapping_sprites:
			pizza.handle_collide()

class Pizza(games.Sprite):
	"""Pizza teleport"""

	def handle_collide(self):
		"""Will teleport sprite in random position"""
		self.x = random.randrange(games.screen.width)
		self.y = random.randrange(games.screen.height)

def main():
	wall_image = games.load_image("images/wall.jpg", transparent = False)
	games.screen.background = wall_image
	pizza_image = games.load_image("images/pizza.bmp")
	pizza_x = random.randrange(games.screen.width)
	pizza_y = random.randrange(games.screen.height)
	the_pizza = Pizza(image = pizza_image, x = pizza_x, y = pizza_y)
	games.screen.add(the_pizza)
	pan_image = games.load_image("images/pan.bmp")
	the_pan = Pan(image = pan_image,
				x = games.mouse.x,
				y = games.mouse.y)
	games.screen.add(the_pan)
	games.mouse.is_visible = False
	games.screen.event_grab = True
	games.screen.mainloop()

#Let's go!
main()