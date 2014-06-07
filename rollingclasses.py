from Tkinter import *

class ChoiceWindow(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.button_choice = StringVar()
		self.button_choice.set("None")
		#self.button_chosen = False
		self.create_widgets()
	def create_widgets(self):
		self.type_label = Label(self, text = "What type of roll would you like to make?")
		self.type_label.grid(row = 1, sticky = W)
		self.atk_button = Radiobutton(self, text="Attack", variable=self.button_choice, value="atk")
		self.atk_button.grid(row = 2, sticky = W)
		self.init_button= Radiobutton(self, text="Initiative", variable=self.button_choice, value="init")
		self.init_button.grid(row = 3, sticky = W)
		self.skill_button = Radiobutton(self, text="Skill", variable=self.button_choice, value="skil")
		self.skill_button.grid(row = 4, sticky = W)