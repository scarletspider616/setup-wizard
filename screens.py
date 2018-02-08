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

	def on_exit():
		pass # shutdown code will go here eventually 

class InputScreen(Screen):
	input_label_text = "Please enter the following information"

class ProgressScreen(Screen):
	pass
