#--------------------------------------------------------------------- Snakes and Ladders game ---------------------------------------------------------------------
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
#Create game functions 

#create a function that checks snakes/ladders position 
def check_square(position): #passes player position through function, variable defined outside of function  
    if position in snakes: #looks for player's landing (current) position - key 
        print(f"| 🐍 Snake! Slide down to {snakes[position]} |", end = "") 
        return snakes[position] # sends destination position (value) back to game loop, skips ladder check 
    elif position in ladders: #only checks ladder position if no snake position found 
        print(f"| 🪜 Ladder! Climb up to {ladders[position]} |", end = "")
        return ladders[position]
    return position #returns new position if no snakes or ladders encountered 

"""replace snake/ladder block with - position = check_square(position)"""

#create a function that gets user number input 
def get_roll(): 
    while True: #create loop that prompts user input until valid
        user_input = input("-- Roll the dice! 🎲 or enter a number (1-6). --\n").strip() #prompts user to roll dice, enter number, or quit game
        if user_input.lower() == 'q': #checks if user wants to quit the game 
            return None #no number to return 
        if user_input == "": #checks if users chose to roll the dice, i.e. pressed enter
            roll = random.randint(1,6) #stores "rolled" number on dice 
            print(f"| You rolled a {roll}! |", end = "")
            return roll #sends roll number back to game loop 
        try: #validating user input 
            roll = int(user_input) #convert user input to integer 
            if 1<= roll <= 6: #checks input is within dice range 
                return roll 
            print("⚠️ Invalid input - Please enter a number between 1 and 6.\n") #sends error message if input out of range
        except ValueError: #sends error message if input cannot be converted to an integer 
            print("⚠️ Invalid input - Numbers only, please! (1-6).\n")

#--------------------------------------------------------------------------------------------------------------
#Introduce game to user 

print("------------------------------------------------ 🐍 Snakes and Ladders 🪜 ------------------------------------------------\n")                                          

#Give user game instructions 
print("----------------- Complete all 3 levels to win the game! -----------------\n \n -------------- Each level has fewer attemps so 👀... try to avoid the snakes 🐍, if you can! --------------\n")

#instructions to start the game 
print("-------- Ready to begin? 🤔 Press enter on your keyboard to roll the dice 🎲 or type 'q' to exit the game. --------\n")

#present level details to user 
#create levels loop that allows users to pass through each level upon completing the level prior, setting new conditions for each level

for level_num, level in enumerate(levels, start=1): #enumerate creates index number for each level, level_num = index, level = dictionary 

    max_attempts = level["max_attempts"] #create variable to assign level max_attempt key's value 
    level_name = level["name"] #create variable to assign level name key's value

    print(f"--- Level {level_num}: {level_name} | Maximum attempts: {max_attempts} ---\n") #\n to create space between next line of text

#--------------------------------------------------------------------------------------------------------------

    #Set initial game state, inside for loop and level_complete loop to reset on each level/ level attempt   
    position = 0 #board game starting position = off the board 
    attempts = 0 #user have yet to roll the dice/input a number 
    timer_start = None #the timer hasn't started because the user has not rolled yet 
    quit_game = False #allows game to continue unless user quits or exceeds maximum attempts     

     #Create games loop 

    #allows a maximum position of 100, ends the game once reached
    while position < 100: 

        #get user input 
        roll = get_roll() #gets output from function 
        if roll is None: #no value, player chose to quit the game. if false, moves on to next body of code
            print("Goodbye 😢 Thanks for playing!\n")
            quit_game = True 
            break #exits game loop 
            
        #starts time on first valid roll     
        if timer_start is None: #checks if timer has started, ignores if false  
            timer_start = time.time() #calculates start time of game in seconds 

        #position and attempts check 
        attempts += 1 #increases with each loop iteration 
        prev_position = position #position prior to current loop iteration 
        position = min(position + roll, 100) #new position after rolling the dice, position capped at 100 
        print(f" You moved from {prev_position} → {position}\n")

        #snakes and ladders check 
        position = check_square(position) #calls function to check/reassign position accordingly 

        #display final position after each attempt 
        print(f" New Position: {position}\n")

        #attempt limit check 
        if attempts >= max_attempts: #checks if max attempts reached, ignores if false 
            time_taken = round(time.time() - timer_start, 1) #calculates total time taken to reach attempt limit 
            print(f"❌ Oh no! You have ran out of attempts | You reached position {position} in {time_taken}s.\n")
            print(f"👾 Game Over | Failed to complete Level {level_num}: {level_name}\n")
            quit_game = True
            break #exits game loop when attempts exceeded     
        
    if quit_game: #will be true if attempts exceeded or player quits, ignores if false  
        break #exits level loop and ends the game 

    #User completes level, i.e. position exceeded 100 but didn't quit or exceed limits
    time_taken = round(time.time() - timer_start, 1)
    print(f"✅ Level {level_num} complete! You reached 100 in {attempts} attempts and {time_taken}s.\n")

    #Checks if there are any levels left for the user to play 
    if level_num == len(levels): #number of levels
        print("🥳 Congratulations, you completed all levels - you're a Snakes and Ladder champion! 🏆")
    else: 
        print(f"Get ready for the next level!\n")    