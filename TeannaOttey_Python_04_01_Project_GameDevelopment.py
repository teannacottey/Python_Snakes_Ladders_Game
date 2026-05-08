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
    print(f"--- Level {level_num}: {level_name} | Maximum attempts: {max_attempts} ---\n") #\n to create space between next line of text

#--------------------------------------------------------------------------------------------------------------

#Set initial game state 

position = 0 #board game starting position = off the board 
attempts = 0 #user have yet to roll the dice/input a number 
timer_start = None #the timer hasn't started because the user has not rolled yet 
quit_game = False #allows game to continue unless user quits or exceeds maximum attempts 

#--------------------------------------------------------------------------------------------------------------

#Create game functions 

#create a function that checks snakes/ladders position 
def check_square(position): #passes player position through function 
    if position in snakes: #looks for player's landing (current) position - key 
        print(f"| 🐍 Snake! Slide down to {snakes[position]} |", end = "") 
        return snakes[position] # sends destination position (value) back to game loop, skips ladder check 
    elif position in ladders: 
        print(f"| 🪜 Ladder! Climb up to {ladders[position]} |", end = "")
        return ladders[position]
    return position #returns new position if no snakes or ladders encountered 

#create a function that gets user number input 
def get_roll(user_input, roll): 
    while True: #create loop that prompts user input until valid
        user_input = input("Roll the dice! 🎲 or enter a number (1-6).\n").strip() #prompts user to roll dice, enter number, or quit game
        if user_input.lower() == 'q': #checks if user wants to quit the game 
            return None #no number to return 
        if user_input == "": #checks if users chose to roll the dice, i.e. pressed enter
            roll = random.randint(1,6) #stores "rolled" number on dice 
            print(f"| You rolled a {roll}!")
            return roll #sends roll number back to game loop 
        try: #validating user input 
            roll = int(user_input) #convert user input to integer 
            if 1<= roll <= 6: #checks input is within dice range 
                return roll 
            print("| ⚠️ Invalid input - Please enter a number between 1 and 6.\n") #sends error message if input out of range
        except ValueError: #sends error message if input cannot be converted to an integer 
            print("| ⚠️ Invalid input - Numbers only, please! (1-6). \n")

#--------------------------------------------------------------------------------------------------------------

#Create game loop 

#Allow dice or number input for error handling purposes 