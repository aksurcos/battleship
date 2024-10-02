<h1 align="center">the Basic Battleship Game </h1>

[Click here to check live project](https://broken-battleship-9b1b7c940597.herokuapp.com/)

This Battleships game was an opportunity to combine my love for strategy and programming. When you think about the Admiral Battle game, it may seem very simple, but when you start coding, if you expect it to move like a human, it can be very difficult to code. That's why I simplified it a bit, here it is now.

![responsive](/battleship.png)


## Index – Table of Contents
* [Design](#design)
* [Features](#features)
* [Testing](#testing)
* [Deployment](#deployment)
* [Bugs](#bugs)
* [Credits](#credits)
  

## Design
### Game Board:
board() function: Creates a 5x5 game board.
boards() function: Displays player and opponent boards side by side.

### Game Logic:
Turn-based shooting between player and computer
Ship placement: Manual or automatic options
Hit and miss tracking
Win condition: Sinking all 5 enemy ships

### How to play:
![start](/start.jpg)

- There is greetings and instructions to start. 

![manual](/manual.jpg)

- The placing ship manually needs 5 coordinates.

![finish](/finish.jpg)

- It shows how to target a coordinate. When it is finished, the winner can be seen and there is a feature to start again.

![quit](/quit.jpg)

- It also has feature to quit all the time.


### Key Funnctions:

1. `board()`: 
   - Creates and returns a 5x5 game board initialized with 'o' characters.

2. `boards(board1, board2)`:
   - Displays two game boards side by side with color-coded symbols.
   - Uses Colorama for colored output in the console.

3. `manual_ship(warzone, ship_number, coord)`:
   - Places a ship manually on the given coordinates.

4. `automatic_ship(warzone)`:
   - Randomly places a ship on the board.

5. `ship_placement(warzone, manual=True)`:
   - Handles the ship placement phase.
   - Allows for both manual and automatic placement of ships.

6. `game(your_board, its_board)`:
   - Main game loop function.
   - Manages turns between the player and the computer.
   - Handles shooting, hit/miss logic, and win conditions.

7. `main()`:
   - The main function that orchestrates the game flow.
   - Initializes boards, places ships, and starts the game loop.
   - Handles game restart logic.

## Features

Features
Colorful console interface using Colorama
Option for manual or automatic ship placement
Real-time board updates after each move
Simple AI for computer opponent
Game state tracking (hits, misses, ships remaining)

## Testing

![linter](/linter.jpg)

- These are the only errors that it has all codes. It's because of explanations or instructions for actions.

## Bugs

I could not detect any yet.

## Deployment

### Deployment steps

- Log in to your account at heroku.com if you don't have any, create one.
- Click on create a new app, give an matchless app name and then choose your region
- Click on create app
- Go to "Settings"
- Add required buildpacks. For this project, set them up as Python is on top and Node.js on bottom
- Go to "Deploy" and select "GitHub" in "Deployment method"
- Connect Heroku app to your Github account and write the repository name, click 'Search' and then 'Connect'
- Choose the branch
- If it is preferred click on "Enable Automatic Deploys" which can keep your app up to date with your GitHub repository
- Wait for the app to build. When it is ready, you will see the “App was successfully deployed” message and a 'View' button to see your deployed app.

    
## Credits

- While I was trying to make this project easier I've checked many Battleship projects.
- Got help from AI when preparing README.md and to understand classic Battleship game's logic.
- Also checked old projects for README.md

### Codes   
- Code Institute Ready Template
- The previous project for defaults and README.md
- [Udemy Sources](https://www.udemy.com/course/sifirdan-ileri-seviyeye-python/)
- [Youtube Tutors](https://www.youtube.com/@emkademy)


### Inspration and Thanking
- Thanks a lot to Code Institute Slack Community



