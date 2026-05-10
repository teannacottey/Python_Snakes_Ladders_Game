# READMe - Python Game Development Project

### Snakes and Ladders Game

A command-line Snakes and Ladders game built in Python. The game features multiple difficulty levels, automated game statistics tracking, input validation, and a JSON stats file. 

### Project Overview

This project was built to demonstrate core Python fundamentals, including functions, loops, dictionaries and error handling. The game challenges the player to reach position 100 on the board across three increasingly difficult levels, each with fewer attempts. 

### Game Instructions

1. Ensure Python3 is installed, then **run the script** in your terminal: 

```jsx
python TeannaOttey_Python_04_01_Project_GameDevelopment.py
```

1. **Roll the dice** by pressing ‘Enter’ on your keyboard or a number between 1-6 
2. **Avoid snakes** - landing on a snake square will send you back to a lower position 
3. **Climb ladders** - landing on a ladder square will send you up to a higher position 
4. **Reach position 100** before you run out of attempts to complete the level 
5. Press ‘q’ on keyboard to quit the game 

### 🏆 Levels

| **Level** | **Name**  | **Max Attempts** |
| --- | --- | --- |
| 1 | Easy | 60 |
| 2 | Medium | 40 |
| 3 | Hard | 20 |

Complete all 3 levels to win the game. If you run out of attempts on a level, it will automatically restart, and your stats will be saved.

### 🐍 Snakes & 🪜 Ladders

| Snakes (land → slide to)  | Ladders (land → climb to)  |
| --- | --- |
| 22 → 5 | 4 → 25  |
| 40 → 3 | 13 → 46  |
| 43 → 18 | 42 → 63 |
| 54 → 31 | 50 → 69 |
| 66 → 45 | 62 → 81  |
| 89 → 53 | 74 → 92 |
| 95 → 77 |  |
| 99 → 41 |  |

### 📊 Game Statistics

Stats are tracked automatically and saved to *game_stats.json* on your Desktop* after every level. Stats are saved for every level played (whether failed, quit or passed), allowing you to track progress over time. 

Tracked stats include: 

- Total games played
- Total levels passed
- Total attempts across all games
- Total time across all games
- A breakdown of every level played
    - number of attempts
    - time taken
    - complete status (True/False)

A summary is printed at the end of every game session. 

*The stats file will be created automatically on your Desktop the first time you play. 

### ⚙️ Functions

| **Function**  | **Purpose** |
| --- | --- |
| get_roll() | Handles user input and validation, returns a valid dice roll (1-6) or None if the player quits. Prints an error message when an invalid user input is received.  |
| check_square(position) | Checks if the player has landed on a snake or a ladder and returns the updated position.  |
| load_stats() | Loads existing game stats from the JSON file or creates a blank stats dictionary if no file exists.  |
| save_stats(game_stats) | Saves the updated stats dictionary to the JSON file automatically.  |
| print_stats(game_stats, session_levels) | Prints a summary of stats at the end of each game session.  |

### 🛠️ Requirements

- Python 3.x
- Built-in modules:
    - random - generates random dice rolls
    - time - game timer
    - json - saves and loads stats
    - os - checks for existing stats file

### Technologies Used

- Visual Studio Code (VS)
    - Python script
- Lucid Chart
    - Flowchart
- Git
    - Version control
- GitHub
    - Publish project

### Project Files

**GitHub Repository:** https://github.com/teannacottey/Python_Snakes_Ladders_Game 

**Python Code File:** Training Materials/CH19 Submissions/04 Python Basics/Project/TeannaOttey_04PythonBasics/TeannaOttey_Python_04_01_Project_GameDevelopment.py

**Flowchart File:** Training Materials/CH19 Submissions/04 Python Basics/Project/TeannaOttey_04PythonBasics/Snakes and Ladders Chart.pdf

**Statistics File:** Training Materials/CH19 Submissions/04 Python Basics/Project/TeannaOttey_04PythonBasics/game_stats.json 

**Game Demo File:** Training Materials/CH19 Submissions/04 Python Basics/Project/Snakes and Ladders Demo.mp4

### Appendix

Image used for game reference: 

https://www.magnific.com/premium-vector/snakes-ladders-board-game-vector-illustration_364882989.htm

**Author**: Teanna Ottey
