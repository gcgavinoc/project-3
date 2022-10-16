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
 - [Gitpod problems](#gitpod-problems)
 - [PEP8](#pep8)
 - [Manual testing](#manual-testing)

[Deployment](#deployment)

[Project Screenshots](#project-screenshots)

[Acknowledgements](#acknowledgements)

# How to play
[Go to top](#table-of-contents)

The game opens with a welcome message that asks the player to enter rules to see the game rules, or press the enter key to start playing the game. If the player types rules and the enter, the game rules will appear in order from the start of the game to the end.

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
 - Many thanks to my mentor Marcel for his help and guidance