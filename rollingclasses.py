from Tkinter import *

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
	def create_widgets(self):
		self.type_label = Label(self, text = "What type of roll would you like to make?")
		self.type_label.grid()
		self.atk_button = Button(self, text = "Attack")
		self.atk_button.grid()
		self.init_button= Button(self, text = "Initiative")
		self.init_button.grid()
		self.skill_button = Button(self, text = "Skill")
		self.skill_button.grid()