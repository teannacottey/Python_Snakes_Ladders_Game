#Snakes and Ladders game 

#Import python modules to use in game

import random #allows code to create a dice to use in the game 
import time #allows code to create a game timer 

#--------------------------------------------------------------------------------------------------------------

#Creating the game board - incl snakes and ladders landing and destination positions 
"""stored in dictionaries as each variable(snakes and ladders) contain mulptiple pair elements
+ reduces potentially lengthy code with e.g.'snake = 22 if position == 22: position -= 17' """

#key = landing position, value = destination position 
snakes = {22:5, 40:3, 43:18, 54:31, 66:45, 89:53, 95:77, 99:41} #snake landing position sends user back to a lower board position
ladders = {4:25, 13:46, 42:63, 50:69, 62:81, 74:92} #ladder landing position sends user up to a higher board position

#Creating game levels - incl difficulty and maximum attempts 
#stored as a list of dictionaries to account for multiple elements with multiple levels 

levels = [
    {"name": "Easy", "max_attempts": 60}, 
    {"name": "Medium", "max_attempts": 40}, 
    {"name": "Hard", "max_attempts": 20}
]
#--------------------------------------------------------------------------------------------------------------

#Introduce game to user 
print("🐍 Snakes and Ladders 🪜\n")                                          

#Give user game instructions 
print("Complete all 3 levels to win the game. \n \nEach level has fewer attemps so 👀... try to avoid the snakes, if you can!\n")

#instructions to start the game 
print("Ready to begin? Press enter on your keyboard to roll the dice 🎲 or type 'q' to exit the game.\n")

#present level details to user 
"""create loop that allows users to pass through each level upon completing the level prior 
setting new conditions for each level""" 

for level_num, level in enumerate(levels, start=1): #enumerate creates index number for each level, level_num = index, level = dictionary 
    max_attempts = level["max_attempts"] #create variable to assign level max_attempt key's value 
    level_name = level["name"] #create variable to assign level name key's value
    print(f"--- Level {level_num}: {level_name} | Maximum attempts: {max_attempts} ---\n")

#--------------------------------------------------------------------------------------------------------------

#Set initial game state 

position = 0 #board game starting position = off the board 
attempts = 0 #user have yet to roll the dice/input a number 
timer_start = None #the timer hasn't started because the user has not rolled yet 
quit_game = False #allows game to continue unless user quits or exceeds maximum attempts 

#--------------------------------------------------------------------------------------------------------------
#VERSION CONTROL - COMMIT INITIAL CHANGES IN GIT

#Allow dice or number input for error handling purposes 