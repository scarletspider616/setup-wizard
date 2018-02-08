Setup Wizard

This project was started after frustrations and difficultly finding 
an easy-to-use/modify template for a front-end GUI that can run on
virtually ever platform. 

This project is written in python3 and requires the kivy 
framework. The kivy framework is available for Linux (ARM and x86), 
Windows, macOS and Android.

This project has been tested on the following:
    - Ubuntu MATE (ARM, 16.04)
    - Ubuntu (x86, 16.04)
    - macOS (10.13.13)
    - Windows (10)

It has NOT been tested on Android


It will include a number classes (inherited Screens) that are useful
for general setup wizard screens, transitions between these screens
and a general/familiar visual setup for a setup wizard. 


Five Screens have been provided: 
	- WelcomeScreen
	- InputScreen
	- TextScreen
	- ProgressScreen
	- FinalScreen

These screens should be inherited by the screens you wish 
to implement in your setup wizard:
eg: 
def MyWelcomeScreen(WelcomeScreen):
	...

For simple wizards, you can also simply modify these screen classes to your
liking. 

I have provided a 
Wizard.py to get your wizard running if you don't want to mess around with 
the implemented screen manager or other apps. I recommend editing this
file or indeed replacing it entirely. Just remember to include the following in the 
replacement:
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from screens import *

presentation = Builder.load_file("wizard.kv")


Each Screen has two methods:
	- on_back():
	- on_next():

Where pythonic code should be overriden in your inherited class for these methods 
to complete whatever actions need to be taken when the user clicks either the 
back or next button. 

Note that there are two exceptions, instead of an "on_back," WelcomeScreen has 
an on_exit() method, and similarly FinalScreen has an on_exit() method instead
of an "on_next" method. 


Attributions: 
The visual aspect of this project is based on the kivy documentation: 
https://kivy.org/docs/guide/widgets.html#adding-widget-background
accessed on February 7, 2018

Code snippets from Kivy Documentation were used. 
Here are specific links and the dates they were accessed: 

https://kivy.org/docs/api-kivy.uix.screenmanager.html (Feb. 8, 2018)
https://kivy.org/docs/_modules/kivy/uix/progressbar.html (Feb. 8, 2018)