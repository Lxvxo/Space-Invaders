# SpaceInvaders Game

## Introduction
This is a SpaceInvaders game project developed in Python 3.9.
![game](https://github.com/Lxvxo/Space-Invaders/assets/113984090/7a80a18a-07b6-4140-b9a6-c187fd04505f)

## Requirements
- Python 3.9
  
### Installation of Required Modules
```bash
python -m pip install tkinter random Pillow
```
## How to Run
To launch the game, execute the following command:
```bash
python main.py  
```

### Known Issues
During the game launch, some errors may appear in the console, but they do not affect the gameplay experience.

## Constraints of the Project :

List: Multiple lists are used in the project. An example is the list storing aliens in the Game class: self.aliens.
Stack: There are three stacks used in the project. In the View class, stacks are used to store scores for each level and display the last score of each level on the Home page.
Queue: No interesting ways to use a queue were found in the project. Therefore, queues were omitted to avoid adding unnecessary elements.
Game Description
This SpaceInvaders game is launched from the Python file "main.py". The window size can be modified from this Python file (width and height).

## Objective
Destroy all aliens including the boss and achieve the highest score possible. The game ends if an alien touches the vertical boundary of the canvas or if the spaceship runs out of lives.

## Explanation of Different Classes
View Class: This class is responsible for displaying pages on the Tkinter window and elements like buttons.

### Home
Contains paths to different levels and displays the last score of each level. Additionally, clicking on the score displays the previous score (using a stack).
Game 1-3: Contains levels 1 to 3 respectively.
Game Class: This class coordinates all elements within the canvas, including their display, movements over time, interactions, etc.

### Spaceship Class
Manages the behavior of the spaceship, including its life, speed, attack, and reaction to various events. The spaceship inflicts 10 attack points per shot.

### Aliens Class
Manages the behavior of aliens. They move horizontally and then vertically when reaching the boundary, alternating directions.

### Obstacle Class
Manages obstacles that protect the spaceship. If an alien hits an obstacle, the alien is destroyed, and the obstacle takes damage.

### Repartition_Objects Class
Manages the distribution of aliens and obstacles on the canvas for each level.

### Shot Class
Manages projectiles for both the spaceship and aliens.

### UFO Class
Manages the behavior of the flying saucer.

### Object_Lives Class
Manages a life bonus that appears at the top of the canvas.

### Object_Shot_God Class
Manages a powerful shooting bonus.

## Disclaimer
Certain details have not been discussed in this explanation as they are not crucial for understanding the game. Refer to the commented program for more details. Errors may appear in the console at times but do not affect the game's functionality. These errors are often due to the destruction of elements in different frames.
