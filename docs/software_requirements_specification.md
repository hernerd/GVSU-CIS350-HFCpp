# Overview
This document describes the functional and non-functional requirements of the game we are currently developing.

# Functional Requirements
1. This will actually show number 2
 1. This is 2.1
 1. and 2.2
 1. and 2.3 and so on
1. Enemies
* Enemies shall shoot projectiles at the player.
  1. Enemies shall be injured when hit by player’s projectiles.
2. Player
  2. The player shall not walk through obstacles.
  2. The player shall be able to pick up power ups.
  2. The player shall lose health when touching enemies.
  2. The player shall be able to move between rooms.
  2. The player shall be able to attack enemies.
  2. The player shall be able to shoot up, down, left, and right.
  2. The player shall be able to interact with the environment.
3. Bullets
  3. Multiple bullets shall be allowed on the screen at once.
  3. Bullets shall damage the player and enemy’s health if hit.
  3. Bullets aren't allowed to pass through obstacles.
4. Power Ups
  4. Powerups shall exist that changes the player’s or enemies’ stats. 

# Non-Functional Requirements
1. Infrastructure
  1. The game shall only handle one user.
  1. The game shall be playable using a keyboard.
  1. Response time between user inputs and game reaction shall be less than .5 seconds.
  1. The game shall run on all major OS that supports Python.
  1. The game shall be created in a way that allows for easy functionality improvements and additions.
2. Player Perspective
  2. The game shall be viewed from the top down perspective.
  2. The game shall contain a UI that outlines the state the player is currently in along with some information about the surrounding rooms and boss enemies.
3. Enemies
  3. Enemies shall path-find to the player.
  3. Enemies shall become more difficult as the player’s stats should increase.
  3. The game shall have multiple enemy sprites
4. Power-Ups
  4. Power-ups shall drop randomly from enemy kills.
  4. Powerups must exist that are both passive and active.
5. Player
  5. The Player’s stats shall increase as the player picks up more power-ups and progresses through the game. 
