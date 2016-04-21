#moving pan
#unput method with mouse
from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
	"""Pan wich can be controled by mouse"""

	def update(self):
		"""Set the object in a cursor position"""

		self.x = games.mouse.x
		self.y = games.mouse.y

def main():
	wall_image = games.load_image("images/wall.jpg", transparent = False)
	games.screen.background = wall_image

	pan_image = games.load_image("images/pan.bmp")
	the_pan = Pan(image = pan_image,
				x = games.mouse.x,
				y = games.mouse.y)
	games.screen.add(the_pan)
	games.mouse.is_visible = False
	games.screen.event_grab = False
	games.screen.mainloop()
#Let's go!
main()