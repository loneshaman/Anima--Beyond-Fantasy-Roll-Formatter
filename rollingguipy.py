from Tkinter import *

choice_str = None

def get_choice():
	#choice_str = button_choice.get()
	root.destroy()

def generate(skil_var):
	#print skil_var
	if button_choice.get() == 'atk':
		weapon = wpn_box.get()
		target = tgt_box.get()
		attack = atk_box.get()
		#print(weapon + " " + target + " " + attack)
		paste_string = "[u]Attack[/u]\nRoll: " + str(roll_val) +"\nWeapon: " + weapon + "\nTarget: " + target + "\nAttack: " + attack
		final_score = int(attack)+int(roll_val)
		paste_string = paste_string + "\nFinal Score: [b]" + str(final_score) + "[/b]"

		print paste_string
	if button_choice.get() == 'init':
		#paste_string = "null"
		weapon = wpn_box.get()
		initiative = init_box.get()
		paste_string = "[u]Initiative[/u]\nRoll: " + str(roll_val) +"\nWeapon: " + weapon + "\nInitiative: " + initiative
		final_score = int(initiative)+int(roll_val)
		paste_string = paste_string + "\nFinal Score: [b]" + str(final_score) + "[/b]"

	if button_choice.get() == 'skil':
		skill_name = skil_var.get()
		skill_val = skil_val_box.get()
		paste_string = "[u]" + skill_name + "[/u]\nRoll: " + str(roll_val) + "\nSkill Value: " + skill_val
		final_score = int(skill_val)+int(roll_val)
		paste_string = paste_string + "\nFinal Score: [b]" + str(final_score) + "[/b]"

	root2.clipboard_clear()
	root2.clipboard_append(paste_string)
	print paste_string
	root2.destroy()

SKILLS = ["Acrobatics", "Athleticism", "Climb", "Jump", "Ride", "Swim", "Art", 
"Dance", "Forging", "Music", "Sleight of Hand", "Animals", "Appraisal", "Herbal Lore", 
"History", "Memorize", "Magic Appraisal", "Medicine", "Navigation", "Occult", "Sciences", "Notice", 
"Search", "Track", "Intimidate", "Leadership", "Persuasion", "Style", "Disguise",
"Hide", "Lock Picking", "Poisons", "Theft", "Stealth", "Trap Lore", "Composure", 
"Feats of Strength", "Withstand Pain"]

root = Tk()
root.title("Anima Roll Formatter")
root.geometry("375x120")
button_choice = StringVar()
app = Frame(root)
roll_val_str = StringVar()
roll_val_str.set("0")
#app.pack_propagate(0) # don't shrink
app.grid()
roll_req = Label(app, text = "Please enter your roll (Default is 0):")
roll_req.grid(row = 1, sticky = W)
roll_box = Entry(app, textvariable = roll_val_str)
roll_box.grid(row = 1, column = 1)
start_label = Label(app, text = "Choose the type of roll you wish to make:")
start_label.grid(row = 2, sticky = W)
atk_button = Radiobutton(app, width=31, indicatoron = 0, text="Attack", variable=button_choice, value="atk", command = get_choice)
atk_button.grid(row = 3, sticky = W)
init_button= Radiobutton(app, width=31, indicatoron = 0, text="Initiative", variable=button_choice, value="init", command = get_choice)
init_button.grid(row = 4, sticky = W)
skill_button = Radiobutton(app, width=31, indicatoron = 0, text="Skill", variable=button_choice, value="skil", command = get_choice)
skill_button.grid(row = 5, sticky = W)
root.mainloop()
roll_val = int(roll_val_str.get())
if roll_val == 0:
	raise SystemExit(0)
print roll_val
root2 = Tk()
#print("window")
root2.geometry("250x100")
#print("Geo")
skill_var = StringVar(root2)
skill_var.set(SKILLS[0])
app2 = Frame(root2)
app2.grid()
if button_choice.get() == 'atk':
	print("Attack chosen")
	root2.title("Attack Formatter")
	wpns = Label(app2, text = "Weapon:")
	wpns.grid(row = 1, sticky = W)
	wpn_box = Entry(app2)
	wpn_box.grid(row = 1, column = 1)
	tgts = Label(app2, text = "Target(s):")
	tgts.grid(row = 2, sticky = W)
	tgt_box = Entry(app2)
	tgt_box.grid(row = 2, column = 1)
	atk_val = Label(app2, text = "Attack:")
	atk_val.grid(row = 3, sticky = W)
	atk_box = Entry(app2)
	atk_box.grid(row = 3, column = 1)
if button_choice.get() == 'init':
	print("Initiative chosen")
	root2.title("Initiative Formatter")
	wpns = Label(app2, text = "Weapon:")
	wpns.grid(row = 1, sticky = W)
	wpn_box = Entry(app2)
	wpn_box.grid(row = 1, column = 1)
	init_val = Label(app2, text = "Initiative:")
	init_val.grid(row = 2, sticky = W)
	init_box = Entry(app2)
	init_box.grid(row = 2, column = 1)
if button_choice.get() == 'skil':
	print("Skill chosen")
	root2.title("Skill Formatter")
	#skil_box = Entry(app2)
	skil_val = Label(app2, text = "Skill value:")
	skil_val.grid(row = 2, sticky = "w")
	skil_val_box = Entry(app2)
	skil_val_box.grid(row = 2, column = 1)
	skil = Label(app2, text = "Skill name:")
	skil.grid(row = 1, sticky = W)
	skil_box = OptionMenu(app2, skill_var, *SKILLS)
	skil_box["width"] = 15
	skil_box.grid(row = 1, column = 1)
gen_button = Button(app2, text = "Generate", command = lambda: generate(skill_var))
gen_button.grid(sticky = "s")
app2.grid_rowconfigure(1, weight = 2)
app2.grid_rowconfigure(2, weight = 2)
root2.mainloop()
