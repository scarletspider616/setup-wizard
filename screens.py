#############################################################################
# screens.py
#
# By: Joey-Michael Fallone
#
# This contains class declarations for screen types used in Wizard.py
# as well as some internal operations
#
#############################################################################
from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color


class WelcomeScreen(Screen):
	welcome_label_text = "Click next to get started"

	def __init__(self, **kwargs):
		super(WelcomeScreen, self).__init__(**kwargs)

		# draw border (eventually this should be in a loop for each screen)
		with self.canvas.before:
			Color(255, 255, 255, 255)
			Line(points = [55, 75, 55, 1100], close = True, width = 1)
			Line(points = [1550, 75, 1550, 1100], close = True, width = 1)
			Line(points = [1550, 75, 55, 75], close = True, width = 1)
			Line(points = [1550, 1100, 55, 1100], close = True, width = 1)

	def shutdown():
		pass # shutdown code will go here eventually 

class InputScreen(Screen):
	input_label_text = "Please enter the following information"

	def __init__(self, **kwargs):
		super(InputScreen, self).__init__(**kwargs)

		with self.canvas.before:
			Color(255, 255, 255, 255)
			Line(points = [55, 75, 55, 1100], close = True, width = 1)
			Line(points = [1550, 75, 1550, 1100], close = True, width = 1)
			Line(points = [1550, 75, 55, 75], close = True, width = 1)
			Line(points = [1550, 1100, 55, 1100], close = True, width = 1)

class ProgressScreen(Screen):
	def __init__(self, **kwargs):
		super(ProgressScreen, self).__init__(**kwargs)

		with self.canvas.before:
			Color(255, 255, 255, 255)
			Line(points = [55, 75, 55, 1100], close = True, width = 1)
			Line(points = [1550, 75, 1550, 1100], close = True, width = 1)
			Line(points = [1550, 75, 55, 75], close = True, width = 1)
			Line(points = [1550, 1100, 55, 1100], close = True, width = 1)
