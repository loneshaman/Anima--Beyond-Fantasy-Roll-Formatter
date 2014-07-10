from Tkinter import *


def get_choice():
	root.destroy()

root = Tk()
root.title("Anima Roll Formatter")
root.geometry("120x120")
button_choice = StringVar()
app = Frame(root)
app.pack_propagate(0) # don't shrink
app.grid()
atk_button = Radiobutton(app, indicatoron = 0, text="Attack", variable=button_choice, value="atk", command = get_choice)
atk_button.grid(row = 2, sticky = W)
init_button= Radiobutton(app, indicatoron = 0, text="Initiative", variable=button_choice, value="init", command = get_choice)
init_button.grid(row = 3, sticky = W)
skill_button = Radiobutton(app, indicatoron = 0, text="Skill", variable=button_choice, value="skil", command = get_choice)
skill_button.grid(row = 4, sticky = W)
root.mainloop()
if button_choice.get() == 'atk':
	print("Attack chosen")
if button_choice.get() == 'init':
	print("Initiative chosen")
if button_choice.get() == 'skil':
	print("Skill chosen")