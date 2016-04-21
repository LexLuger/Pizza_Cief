#pizza panick
#player must catch the pizza while it do not reach the gound
from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
	"""Pan for pizza"""

	image = games.load_image("images/pan.bmp")

	def __init__(self):
		"""Pan object initialization and Text object for scores"""

		super(Pan, self).__init__(image = Pan.image,
									x = games.mouse.x,
									bottom = games.screen.height)
		self.score = games.Text(value = 0, size = 25, color = color.black,
								top = 5, right = games.screen.width - 10)
		games.screen.add(self.score)

	def update(self):
		"""Move object in horizontal plane"""

		self.x = games.mouse.x
		if self.left < 0:
			self.left = 0
		if self.right > games.screen.width:
			self.right = games.screen.width
		self.check_catch()

	def check_catch(self):
		"""Check have olayer catch pizza or not"""

		for pizza in self.overlapping_sprites:
			self.score.value += 10
			self.score.right = games.screen.width - 10
			pizza.handle_caught()

class Pizza(games.Sprite):
	"""The Pizza circles fallen down"""

	image = games.load_image("images/pizza.bmp")
	speed = 1

	def __init__(self, x, y = 90):
		"""Pizza object initialization"""
		super(Pizza, self).__init__(image = Pizza.image,
									x = x, y = y,
									dy = Pizza.speed)

	def update(self):
		"""Does sprite's underline has toch down border of screen"""

		if self.bottom > games.screen.height:
			self.end_game()
			self.destroy()

	def handle_caught(self):
		"""Destroy the object has been caught"""

		self.destroy()

	
	def end_game(self):
		"""The end of game"""

		end_message = games.Message(value = "Game Over",
									size = 90,
									color = color.red,
									x = games.screen.width/2,
									y = games.screen.height/2,
									lifetime = 5 * games.screen.fps,
									after_death = games.screen.quit)
		games.screen.add(end_game)

class Chef(games.Sprite):
	"""Our dare chef"""

	image = games.load_image("images/chef.bmp")

	def __init__(self,  speed = 2, y = 55, odds_change = 200):
		"""Chef object initialization"""

		super(Chef, self).__init__(image = Chef.image,
									x = games.screen.width / 2,
									y = y,
									dx = speed)
		self.odds_change = odds_change
		self.time_til_drop = 0
		self.number_pizza = 0

	def update(self):
		"""It change chef's direction"""

		if self.left < 0 or self.right >games.screen.width:
			self.dx = -self.dx

		elif random.randrange(self.odds_change) == 0:
			self.dx = -self.dx

		self.check_drop()

	def check_drop(self):
		"""Reduce the interval on one or drop another
		pizza and restore previous interval"""

		if self.time_til_drop > 0 :
			self.time_til_drop -= 1
		else:
			new_pizza = Pizza(x = self.x)
			games.screen.add(new_pizza)
		#regardless fall speed of pizza the gap between fallen circles equal 30% theyself height
			self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1
		#speed up	
			self.number_pizza += 1
			if self.number_pizza == 10:
				self.dx = 4
			if self.number_pizza == 50:
				self.dx = 12



def main():
	"""The game process"""

	wall_image = games.load_image("images/wall.jpg", transparent = False)
	games.screen.background = wall_image
	the_chef = Chef()
	games.screen.add(the_chef)
	the_pan = Pan()
	games.screen.add(the_pan)
	games.mouse.is_visible = False
	games.screen.event_grab = True
	games.screen.mainloop()

#Now go
main()