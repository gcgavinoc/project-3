# Battleships
Welcome! My name is Gavin O'Connor and this is my python essentials project which allows the user to play a game of Battleships. The game is played by entering commands into a terminal running on Heroku. The user plays against the computer as both players try to guess the location of the others battleships. The first player to guess all five of the others battleships wins. There is an adjustable difficulty level in the form of turns, where the user can pick the amount of turns they want, the fewer turns the harder the game.

You can access the live game [here](https://ci-project-3-gavin.herokuapp.com/).

![Image of game using Am I Responsive tool](assets/images/amiresponsive.png)

# Table of Contents
[User Experience (UX) Design](#user-experience-ux-design)
 - [User Goals](#user-goals)
 - [User Expectations](#user-expectations)
 - [Game Logic](#game-logic)

[How to Play](#how-to-play)

[Features](#features)
 - [Welcome screen](#welcome-screen)
 - [Rules screen](#rules-screen)
 - [Choose turns](#choose-turns)
 - [Place ships](#place-ships)
 - [Player and computer guesses](#guesses)
 - [Play again](#play-again)

[Validation](#validation)
 - [Rules validation](#rules-validation)
 - [Turns validation](#turns-validation)
 - [Place ships validation](#place-ships-validation)
 - [Guess validation](#guess-validation)
 - [Play again validation](#play-again-validation)

[Testing](#testing)
 - [PEP8](#pep8)
 - [Manual testing](#manual-testing)

[Technologies used](#technologies-used)

[Deployment](#deployment)

[Project Screenshots](#project-screenshots)

[Acknowledgements](#acknowledgements)

# User Experience (UX) Design
[Go to top](#table-of-contents)

## User Goals
[Go to top](#table-of-contents)

The user goals for this project are the following:
 - To provide a fun and functional game to the user with replayability in the form of variance each time the game is played based on user input
 - To provide a clear and concise overview of the rules of the game that allows the player to play through the game with no confusion
 - To make the game instructions and requests clear to the player so they know exactly how to proceed through the game
 - To provide an engaging game experience that encourages the player to try their best to beat the computer and win

## User Expectations
[Go to top](#table-of-contents)

The user expectations I expect when engaging with this game are the following:
 - The user should expect to understand fully how to play the game and what they need to do at any point in the game process
 - The user should expect to be able to win the game
 - The user should expect to have fun with the game

## Game Logic
[Go to top](#table-of-contents)

I created a logic map before starting development on the game itself, which allowed me to visualize what elements and features needed to be implemented as well as to set a scope for my game that needed to be met. The logic map was created using [Lucid Chart](https://www.lucidchart.com). The logic map can be seen below:

![Image of the logic map created for the game](assets/images/logic-map.png)

# How to play
[Go to top](#table-of-contents)

The game opens with a welcome message that asks the player to enter rules to see the game rules, or press the enter key to start playing the game. If the player types rules and the enter, the game rules will appear in order from the start of the game to the end. The rules screen then asks the player to press the enter key to start the game. Once they do, the game asks them to enter the number of turns they want to start with from 1 to 60. The game board has 64 spots so 60 was chosen as the highest turn amount if the player wants a very forgiving game experience where chance of losing by running out of turns is very low. 

Once the player enters the amount of turns they want, they are asked to enter the row of where they want to place a battleship on their board, number 1-8. Then they are asked to enter the column of where they want to place their ship, letters A-H. They are asked this five times until all five of their ships are placed on their game board. Then both the player and computer game boards are printed to the console and the player is asked to guess their opponents battleship locations. They are asked to enter the row of where they want to guess that the opponents battleship is located, and then the column. After entering the coordinates of their guess, both game boards are printed again with hit or miss marks on them to indicate if each players guess hit or missed a battleship. They are told if they hit a battleship, missed, or if they already entered those coordinates they will be asked to enter different coordinates. They are told the coordinates of where the computer guessed and if the computer hit or missed. Lastly, they are told how many turns they have remaining.

If the player hits all five of the computers battleships they will be told 'Congratulations, you sank all of the computer's battleships' and they are then asked if they want to play again. if they enter yes, the game starts over again from the welcome screen and the game boards are wiped of all markers. If they enter no a message 'Thank you for playing!' appears and the program quits running. If the computer hits all five of the players battleships the message 'The computer sank all of your battleships, you lose!' appears and the player is asked if they want to play again. If the player runs out of lives before either the player or computers battleships are all sunk, then the message 'Sorry, you have no turns left, Game Over' appears and the player is asked if they want to play again.

# Testing
[Go to top](#table-of-contents)

## PEP8
[Go to top](#table-of-contents)

Using Gitpods built in python validator, several problems were detected on project completion:

![Image of problems tab in gitpod before problems were resolved](assets/images/gitpod-problems.png)

The first type of problem was that I was missing a space after the # for my code comments. I placed a space after the # to resolve this.
The second type of problem was that I was missing a space after the ',' in my randint methods. I placed a space after the ',' to resolve this.
The third and most prominent type of problem was that several of my code lines were too long. I used line breaks on the lines that were too long to resolve this.

After I resolved the above problems, the python validator showed no red 'important' problems. There remained some warnings/recommendations, however these had no effect on my code.

![Image of problems tab in gitpod after problems were resolved](assets/images/gitpod-problems-fixed.png)

## Manual Testing
[Go to top](#table-of-contents)

I manually tested if the game was working correctly using various different methods. The first method was to enter 1 turn when prompted by the game. This would allow me to test the end of game screen and messages/inputs quickly without having to play the game for too long each time. The second method was to change the required score for the player and computer to win the game from 5 to 1. Again, this made testing the win and lose screens alot quicker and easier as I only had to play until 1 battleship was hit by either player as opposed to 5. To make this process even quicker, I temporarily added code to print the computers board to the terminal, so that I could see exactly where the computers battleships were located and guess the ships easily and quickly. 

I also ran through the game using the final code with various amounts of turns inputted to ensure the normal game experience functioned correctly. I did this on both Gitpod and Heroku numerous times through the project creation process and again upon project completion. Incorrect inputs were entered every time an input was requested to test input validation, changes to the game code were made whenever the program crashed from an invalid input.

# Technologies used
[Go to top](#table-of-contents)

[Github](https://github.com/) was used to create the repository that hosts the site and to store the project's code after it was pushed from Git.
[Gitpod](https://gitpod.io/workspaces) was used as the Code Editor used for the site.
[Heroku](https://www.heroku.com) was used to host the game terminal and game code as an app
[Am I Responsive](https://ui.dev/amiresponsive) was used to display what the game looks like on various screen sizes

# Deployment
[Go to top](#table-of-contents)

This project was deployed to Heroku from Github, Heroku was used to create the terminal in which the game is played.

These are the deployment steps:

1. Push all code to Github
2. Go to [Heroku](https://www.heroku.com)
3. Click button labeled 'Sign up for free'
4. Enter details, click 'Create free account'
5. Click link in verification email sent to entered email address
6. Create new password, click 'Set password and Login'
7. Accept terms of service
8. Click 'Create new app'
9. Enter app name and select Europe as the region, click create app
10. Click settings tab, click 'Reveal Config Vars'
11. Enter key as PORT and value as 8000
12. Click 'Add buildpack', click 'Python', click 'Save Changes'
13. Click 'Add buildpack, click 'NodeJS', click 'Save Changes'
14. Ensure 'Python' is above 'NodeJS' in the buildpack list
15. Click 'Deploy' tab, click 'Connect to Github'
16. Click 'Connect to Github', sign in to Github in window that appears
17. Search repository name in search bar 'project-3'
18. Click repository 'project-3' that appears, click 'Connect'
19. Scroll down, under 'Choose a branch to deploy' ensure 'main' is selected
20. Click 'Deploy Branch', then 'View' when deployment is complete

# Acknowledgements
[Go to top](#table-of-contents)

 - Initial battleship game tutorial found [here](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=909s&ab_channel=KnowledgeMavens)
 - Solution for when input is empty found [here](https://stackoverflow.com/questions/26247729/how-do-i-get-python-to-recognize-that-there-has-been-no-input)
 - Ascii artwork for welcome message found [here](https://asciiart.website/index.php?art=transportation/nautical)
 - How to print ascii art to the terminal found [here](https://stackoverflow.com/questions/23623288/print-full-ascii-art)
 - Function randint imported from random and sys imported
 - Many thanks to my mentor Marcel for his help and guidance