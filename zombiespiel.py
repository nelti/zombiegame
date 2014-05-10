import random

# Startscreen

text =    "***********************"
text += "\n*     Zombie Game     *"
text += "\n*                     *"
text += "\n*                     *"
text += "\n*   - Nelti Games -   *"
text += "\n*                     *"
text += "\n***********************"

print(text)

def menu():
	"""The menu"""
	text = "What would you like to do next?"
	text += "\n"
	text += "\nA. Show Stats"
	text += "\nB. Eat"
	text += "\nC. Sleep"
	text += "\nD. Travel"
	text += "\nE. Travel fast!"
	text += "\nQ. Quit Game"
	return text
	

def game():
	"""The game"""
	# Initialize Values
	done = False
	player_traveled = 0
	player_hitpoints = 20
	player_food = 5
	player_attack = 5
	player_defense = 5
	text = ""
	
	
	
	while done == False:
		text += menu()
		print(text)
		
		
		
		
if __name__ == "__main__":
	game()
	
