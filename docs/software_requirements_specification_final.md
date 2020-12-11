# Overview
The purpose of this document is to highlight the requirments of our game and describe the test cases we used to check that these requirments were implemented the way we wanted. 

# Software Requirements
This section describes functional and non-functional requirements for our game based on what section of the game they apply to. Also linked is the test case that tests the requirement. 

## Functional Requirements

### Enemies

| FR1 | Certain enemies shall shoot projectiles at the player. | TC5 |
| FR2 | Enemies shall be injured when hit by player’s projectiles. | TC12 |
| FR3 | Enemies shall drop a key upon last enemies death. | TC17|
| FR4 | Enemies shall move differently based on their type. | TC8|
| FR5 | Boss enemies shall be harder to defeat than other enemies. | TC9|
| FR6 | Boss enemies shall be stationary.  | TBD|

### Player

| FR7 | The player shall be able to move up, down, left and right on the screen. | TC1 |
| FR8 | The player shall not walk through obstacles.  | TC16 |
| FR9 | The player shall be able to pick up power ups. | TC13, TC14, TC15, TC18|
| FR10 | The player shall lose health when touching enemies. | TC11|
| FR11 | The player shall be able to move between rooms. | TC3|
| FR12 | The player shall be able to attack enemies.  | TC2, TC12|
| FR13 | The player shall be able to shoot up, down, left, and right.  | TC2|
| FR14 | The player shall be able to interact with the environment.  | TC16|

### Bullets

| FR15 | Multiple bullets shall be allowed on the screen at once. | TC10 |
| FR16 | Bullets shall damage the player and enemy’s health if hit.  | TC11, TC12 |
| FR17 | Bullets shall not pass through obstacles. | TC16|
| FR18 | Bullets shall have a delay between .5 to 1 seconds. | TC6|
| FR19 | Fire Bullets shall have no delay between shots. | TC6|
| FR20 | Bullets from enemies shall decrease the players health by 1 heart (10 health).  | TC11|

### Power-Ups

| FR21 | Powerups shall exist that change the player’s stats. | TC13, TC15, TC18 |
| FR22 | Speed Power-ups shall be able to stack and increase the players speed.  | TC13 |
| FR23 | There shall be multiple types of Power-ups. | TC13, TC14, TC15, TC18|
| FR24 | Health Power-ups shall increase the players health by a random number from 1 to 3. | TC15|
| FR25 | Portal Power-ups shall transport the player to a randomly generated location in the room. | TC14|
| FR26 | Fire Power-ups shall last for 10 seconds.  | TC18|
| FR27 | Key Power-ups will unlock the door to the next room when used.  | TC17|

## Non-Functional Requirements

### Infastructure

| NFR1 | The game shall only handle one user. | TBD |
| NFR2 | The game shall be playable using a keyboard. | TC1, TC2 |
| NFR3 | Response time between user inputs and game reaction shall be less than .5 seconds. | TBD|
| NFR4 | The game shall run on all major OS that supports Python. | TBD|
| NFR5 | The game shall be created to allow for easy functionality improvements and additions. | TBD|
| NFR6 | The game shall be able to have the window size scaled up and down.  | TBD|
| NFR7 | Level generation shall be endless.  | TBD|

### Enemies

| NFR8 | Enemies shall path-find to the player. | TC4 |
| NFR9 | Enemies shall become more difficult as the player’s stats should increase. | TBD |
| NFR10 | The game shall have multiple enemy sprites. | TBD|
| NFR11 | Bosses shall spawn every 10 levels. | TC7|
| NFR12 | Enemies shall shoot towards the player. | TC5 |

### Power-Ups

| NFR13 | Power-ups shall only exist to help the player. | TC13, TC14, TC15, TC18 |
| NFR14 | Power-ups shall exist that are both passive and active. | TC13, TC14, TC15, TC18 |
| NFR15 | The game shall contain a UI that displays all active power-ups. | TC19|
| NFR16 | Power-ups shall carry over from previous rooms. | TC20|
| NFR17 | Power-ups shall be stored for a later use in an inventory system. | TC19, TC20|

### Player

| NFR18 | The Player’s stats shall increase as the player picks up more power-ups and progresses through the game. |  TC13, TC18 |
| NFR19 | The player shall be viewed from the top down perspective. | TBD |
| NFR20 | The player shall have a UI that outlines the state the player is currently in along with some information about the surrounding rooms and boss enemies. | TBD|
| NFR21 | The player shall be able to move back and forth between levels. | TC3|
| NFR22 | As the player moves there shall be basic animations. | TBD|
| NFR23 | As the player fires a bullet there shall be an animation. | TBD|

# Test Specification
The purpose of this section is to outline the tests we used to test our requirements. We have unit tests, integration tests and system tests to assure our game is running smoothly. Also linked is the requirement(s) the test checks for. 
## Unit tests
| TC1 | Testing whether the users input from the keyboard moves the player. | Run the game, use W, A, S, D on the keyboard, check the log file for movement as well as player moving on the screen. | User input (W, A, S, D) | Log of what direction the user is moving | Log of what direction the user is moving | Pass | FR7, NFR2 |

| TC2 | Testing whether the users input from the keyboard move the player. | Run the game, use the arrow keys on the keyboard, check the log file for bullets as well as bullets moving on the screen. | User input (arrow keys) | Log of bullet spawning and direction | Log of bullet spawning and direction | Pass | FR12, FR13 |

| TC3 | Testing whether the user moves into a new room | Run the game, defeat the level, move to the new room, check the log file | The player moving to the new room | Log of the player moving to the new room | Log of the player moving to the new room | Pass | FR11, NFR21 |

| TC4 | Testing whether the enemies attempt to pathfind to player | Run the game, let the enemy get close to you, check the log file to see the enemy offset get smaller as it comes to you. | The enemies offset to the player | A decreasng offset as the game runs in the log | A decreasng offset as the game runs in the log | Pass | NFR8 |

| TC5 | Testing whether the enemies will shoot towards the player | Run the game, play the game till you encounter a ranged enemy and they shoot at you, check the log file  | The enemy shooting | A log of the enenmy shooting at the player | A log of the enemy shooting at the player | Pass | FR1, NFR12 |

| TC6 | Testing whether there is a delay between a normal bullet and a fire bullet. | Run the game, attempt to shoot a bullet rapidly, pick up a fire power-up, attempt to shoot a bullet rapidly, check the log file | The bullet spawn time | A delay for normal bullets, no delay for a fire bullet in the log file | A delay for normal bullets, no delay for a fire bullet in the log file  | Pass | FR18, FR19 |

| TC7 | Testing that a boss spawns every 10 levels | Run the game, play the game till level 10, check the log file that the boss spawns. | The level of the game | The boss should spawn | The boss spawned | Pass | NFR11 |

| TC8 | Testing that different enemies move differently | Run the game, experience all 4 types of enemies, check the log file to see movements | Movement of each enemy | Different movement types based on enemy type. | Different movement types based on enemy type. | Pass | FR4 |

| TC9 | Testing that the boss should be harder to kill than a normal enemy | Run the game, play the game till level 10, keep attacking the boss till it dies, check the log file that the boss took more shots than a normal enemy. | The amount of damage given to the boss | The log of the amount of shots it took for the boss to die | The log of the amount of shots it took for the boss to die | Pass | FR5 |

| TC10 | Test that multiple bullets are on the screen | Run the game, get to a ranged enemy or shoot multiple times in a row,  | The amount of bullets on the screen | The log file should reflect the amount of bullets on the screen at a single time being more than 1 | The log file should reflect the amount of bullets on the screen at a single time being more than 1. | Pass | FR15 |

## Integration tests
| TC11 | Tests that enemies damage the player | Run the game, let an enemy damage you, check the log file | The enemies interaction with the player | The enemy damaging the player in the log file | The enemy damaging the player in the log file | Pass | FR10, FR16, FR20 |

| TC12 | Tests that the player can damage the enemies | Run the game, attack an enemy, check the log file | The players bullet interaction with an enemy | The enemies health decreasing in the log file | The enemies health decreasing in the log file | Pass | FR2 ,FR12, FR16|

| TC13 | Tests that the player can pick up speed power ups and increase speed | Run pytest on the powerUpTest.py file | The player and speed powerup | The player speed increasing | The player speed increased | Pass | FR9, FR21, FR22, FR23, NFR13, NFR14, NFR18|

| TC14 | Tests that the player can pick up portal power ups and it teleports player | Run pytest on the powerUpTest.py file | The player and portal powerup | The player teleporting | The player teleported | Pass | FR9, FR23, FR25, NFR13, NFR14|

| TC15 | Tests that the player can pick up health power ups | Run pytest on the powerUpTest.py file | The player and health powerup | The player being healed | The player being healed | Pass | FR9, FR21, FR23, FR24, NFR13, NFR14|
## System tests
| TC16 | To test that obstacles block enemies, bullets and the player | Run the game, run into an obstacle, have an enemy run into an obstacle, shoot at an obstacle, check the log file | The name of the entity colliding with obstacle | A log of the entity the obstacle blocked | A log of the entity the obstacle blocked | Pass | FR8, FR14, FR17 |

| TC17 | Tests that the last enemy drops a key and the player can pick it up to load the door. | Run the game, kill all the enemies in the room, pick up the key, check the log file | The key spawning and being interacted with | Door should spawn to next room in log file | Door should spawn to next room in log file | Pass | FR3, FR27 |

| TC18 | Tests that the player can pick up fire powerups | Run pytest on the powerUpTest.py file | The player and fire powerup | The player having the new bullet type | The player has the new bullet type | Pass | FR9, FR21, FR23, FR26, NFR13, NFR14, NFR18|

| TC19 | Tests that the user has an inventory that the player can activate | Run the game, pick up multiple power-ups, cycle through with left shift and apply with Q| The powerups and the player | Powerups don't activate immediatly when picked up | Powerups don't activate immediatly | Pass | NFR17, NFR18 |

| TC20 | Tests that the inventory and powerups stay consistent between rooms | Run the game, pick up powerups, activate some, go to a new room, check to make sure they're still active and check the log file. | The stored and active powerups | These stay with the player between rooms | They stay with the player between rooms | Pass | NFR16, NFR17 |

# Software Artifacts
These are the artifacts for our project that helped with the development process. Also included is our slide from our midterm presentation.
* [Power-up Use Case Description](https://github.com/hernerd/GVSU-CIS350-HFCpp/blob/master/artifacts/use_case_diagrams/power_up_use_case_desc.md)
*  [Power-up Use Case Diagram](https://github.com/hernerd/GVSU-CIS350-HFCpp/blob/master/artifacts/use_case_diagrams/power_up_use_case_diagram.png)
*  [Bullet Use Case Diagram](https://github.com/hernerd/GVSU-CIS350-HFCpp/blob/master/artifacts/use_case_diagrams/Bullet_Use_Case.png)
*   [Obstacle Use Case Diagram](https://github.com/hernerd/GVSU-CIS350-HFCpp/blob/master/artifacts/use_case_diagrams/Obstacle_Use_Case.png)
*   [Midterm Slides](https://github.com/hernerd/GVSU-CIS350-HFCpp/blob/master/docs/CIS%20350%20Midterm.pdf)
*   [Gantt Chart](https://github.com/hernerd/GVSU-CIS350-HFCpp/blob/master/docs/GanttChart.pdf)
*   [Tasks](https://github.com/hernerd/GVSU-CIS350-HFCpp/blob/master/docs/tasks.md)
*   [Proposal](https://github.com/hernerd/GVSU-CIS350-HFCpp/blob/master/docs/proposal.md)


