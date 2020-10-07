# Overview
This document describes the functional and non-functional requirements of the game we are currently developing.

# Functional Requirements
1. Enemies
   * Enemies shall shoot projectiles at the player.
   * Enemies shall be injured when hit by player’s projectiles.
2. Player
 * The player shall not walk through obstacles.
 * The player shall be able to pick up power ups.
 * The player shall lose health when touching enemies.
 * The player shall be able to move between rooms.
 * The player shall be able to attack enemies.
 * The player shall be able to shoot up, down, left, and right.
 * The player shall be able to interact with the environment.
3. Bullets
 * Multiple bullets shall be allowed on the screen at once.
 * Bullets shall damage the player and enemy’s health if hit.
 * Bullets aren't allowed to pass through obstacles.
4. Power Ups
 * Powerups shall exist that changes the player’s or enemies’ stats. 

# Non-Functional Requirements
1. Infrastructure
 * The game shall only handle one user.
 * The game shall be playable using a keyboard.
 * Response time between user inputs and game reaction shall be less than .5 seconds.
 * The game shall run on all major OS that supports Python.
 * The game shall be created in a way that allows for easy functionality improvements and additions.
2. Player Perspective
 * The game shall be viewed from the top down perspective.
 * The game shall contain a UI that outlines the state the player is currently in along with some information about the surrounding rooms and boss enemies.
3. Enemies
 * Enemies shall path-find to the player.
 * Enemies shall become more difficult as the player’s stats should increase.
 * The game shall have multiple enemy sprites
4. Power-Ups
 * Power-ups shall drop randomly from enemy kills.
 * Powerups must exist that are both passive and active.
5. Player
 * The Player’s stats shall increase as the player picks up more power-ups and progresses through the game. 
