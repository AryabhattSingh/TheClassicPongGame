# The Classic Pong Game

![Screenshot (707)](https://github.com/AryabhattSingh/TheClassicPongGame/assets/63608694/6c040ed6-b88f-4b9f-98d9-6ba594565858)

Welcome to the Classic Pong Game repository! This is a simple yet exciting game built using Python and the Turtle graphics library. In this classic arcade-style game, you'll control paddles to bounce a ball back and forth with your opponent. Let's dive into the details of the game.

## Game Overview

- **Game Window Dimensions:** 800 X 600 pixels.
- **Paddles:** Two paddles - left and right - each measuring 20 pixels in width and 100 pixels in height.
- **Ball:** A circular ball with dimensions of 20 X 20 pixels.

## Gameplay

Here's how the game works:

1. The game starts with the ball in the center, moving in the top-left direction with an initial speed of 0.2.
2. Players control their respective paddles to bounce the ball back and forth.
3. The ball's speed increases by 0.9 after each successful hit, making the game progressively challenging.
4. Score a point when your opponent misses the ball.
5. After a miss, the ball restarts from the center and moves in the opposite direction.
6. The game continues until you decide to close it.

## Controls

- **Player 1 (Left Paddle):**
  - Move Up: Press `W` key
  - Move Down: Press `S` key
- **Player 2 (Right Paddle):**
  - Move Up: Press the `Up Arrow` key
  - Move Down: Press the `Down Arrow` key

## Project Structure

This repository contains the following Python files:

- **main.py:** Contains the game logic and necessary key bindings for paddle controls.
- **ball.py:** Defines the structure of the ball and its movement, including interactions with walls, paddles, and misses.
- **paddle.py:** Defines each paddle's characteristics, such as shape, size, position, and movement behavior on key presses.
- **scoreboard.py:** Displays the scores of each player at the top of the game window using a specified font style and size. The scores are updated each time a player misses the ball.

## Getting Started

To play the Classic Pong Game on your local machine, follow these steps:

1. Clone or download this repository.
2. Make sure you have Python installed (Python 3.x is recommended).
3. Run the `main.py` script using Python.

## License

This Classic Pong Game is open-source and released under the MIT License. You are welcome to use, modify, and distribute this code for personal or educational purposes.

Have fun playing the Classic Pong Game, and may the best player win! 🏓
