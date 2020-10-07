# Overview
This document describes the functional and non-functional requirements of the game we are currently developing.

# Functional Requirements
1. Enemies
   1. Enemies shall shoot projectiles at the player.
   1. Enemies shall be injured when hit by player’s projectiles.
1. Player
   1. The player shall not walk through obstacles.
   1. The player shall be able to pick up power ups.
   1. The player shall lose health when touching enemies.
   1. The player shall be able to move between rooms.
   1. The player shall be able to attack enemies.
   1. The player shall be able to shoot up, down, left, and right.
   1. The player shall be able to interact with the environment.
1. Bullets
   1. Multiple bullets shall be allowed on the screen at once.
   1. Bullets shall damage the player and enemy’s health if hit.
   1. Bullets aren't allowed to pass through obstacles.
1. Power Ups
   1. Powerups shall exist that changes the player’s or enemies’ stats. 

# Non-Functional Requirements
1. Infrastructure
   1. The game shall only handle one user.
   1. The game shall be playable using a keyboard.
   1. Response time between user inputs and game reaction shall be less than .5 seconds.
   1. The game shall run on all major OS that supports Python.
   1. The game shall be created in a way that allows for easy functionality improvements and additions.
1. Player Perspective
   1. The game shall be viewed from the top down perspective.
   1. The game shall contain a UI that outlines the state the player is currently in along with some information about the surrounding rooms and boss enemies.
1. Enemies
   1. Enemies shall path-find to the player.
   1. Enemies shall become more difficult as the player’s stats should increase.
   1. The game shall have multiple enemy sprites
1. Power-Ups
   1. Power-ups shall drop randomly from enemy kills.
   1. Powerups must exist that are both passive and active.
1. Player
   1. The Player’s stats shall increase as the player picks up more power-ups and progresses through the game. 
