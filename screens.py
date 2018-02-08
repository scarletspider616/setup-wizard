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
from kivy.uix.progressbar import ProgressBar


class WelcomeScreen(Screen):
	welcome_label_text = "Click next to get started"

	def on_exit(self):
		pass # shutdown code will go here eventually 

	def on_next(self):
		pass

class InputScreen(Screen):
	input_label_text = "Please enter the following information"

	def on_back(self):
		pass

	def on_next(self):
		pass


class ProgressScreen(Screen):
	pb = ProgressBar(max=1000)
	pb.value = 500
	def on_back(self):
		pass

	def on_next(self):
		pass

class TextScreen(Screen):
	text_label_text = "Enter the text to display here"

	def on_back(self):
		pass

	def on_next(self):
		pass

class FinalScreen(Screen):
	final_label_text = "Finsihed!"

	def on_back(self):
		pass

	def on_exit(self):
		pass