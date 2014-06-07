from Tkinter import Tk
from colour import Color
import string

roll1_type = raw_input("What type of roll? ")
paste_string = "[u]" + roll1_type + "[/u]"
roll_type = string.lower(roll1_type)
roll = raw_input("Roll value? ")
paste_string = paste_string + '\n' + "Roll: " + roll
init_string = "initiative"
atk_string = "attack"
#skill_string = "skill"
if roll_type == init_string:
	weapon_type = raw_input("What weapon? ")
	paste_string = paste_string + '\n' + "Weapon: [b]" + weapon_type + "[/b]"
	init_score = raw_input("What's the initiative for the weapon? " )
	paste_string = paste_string + '\n' + "Initiative: [color=#ff0000]" + str(init_score) + "[/color]"
	final = int(roll) + int(init_score)
	paste_string = paste_string + '\n' + "Final Score: [b]" + str(final) + "[/b]"
elif roll_type == atk_string:
	weapon_type = raw_input("What weapon? ")
	paste_string = paste_string + '\n' + "Weapon: " + weapon_type
	target = raw_input("Who are you attacking? ")
	paste_string = paste_string + '\n' + "Target: " + target
	atk_score = raw_input("What's the attack for the weapon? " )
	paste_string = paste_string + '\n' + "Attack: [color=#ff0000]" + str(atk_score) + "[/color]"
	final = int(roll) + int(atk_score)
	paste_string = paste_string + '\n' + "Final Score: [b]" + str(final) + "[/b]"
else: #skill use
	skill_value = raw_input("What's the value of the skill? ")
	paste_string = paste_string + '\n' + roll1_type + " score: [color=#ff0000]" + str(skill_value) + "[/color]"
	final = int(roll) + int(skill_value)
	paste_string = paste_string + '\n' + "Final Score: [b]" + str(final) + "[/b]"

print(paste_string)
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(paste_string)
r.destroy()

