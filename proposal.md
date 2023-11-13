# Two-Player Dice Game

## Repository
<https://github.com/EthanDesjardins/Final-Project.git>

## Description
It is a two player game, where two players try to get each others HP
from 100 to zero using randomly rolled dice. The gimmick of the game 
is that you roll a six sided dice until you get a 1, which ends your
turn, and determines how much damage you do to the other player.(Turn-based)

## Features
- Feature 1(Dice)
	- The Feature uses a random 6-sided die, and keeps rolling
    the die until you get a 1 or a 6, and then adds all rolls together as
    damage to the other player
- Feature 2(Player)
	- Creates Player health and adds and subtracts it. If I have time 
    I would like to add a block and attack input that helps make the game more complex
- Feature 3 (inputs & generated prompts)
	- Creates prompted messages based on actions and inputs of players(maybe a class?)

## Challenges
- Need to learn how to create a randomly rolling dice and add them/subtract them.
- Need to learn how to create two player characters
- Need to learn how to use multiple inputs in the game before it ends

## Outcomes
Ideal Outcome:
- A Two player game where they roll a dice and try to get the others health to zero.
  If I can I would like to add options to attack and defend for added nuance to the game.

Minimal Viable Outcome:
- A game where the two players take turns rolling dice until the others health is zero

## Milestones

- Week 1
  1. Create a function to roll a dice with random outputs each time
  2. Start the main function. where it continues to roll until its a 1 or a 6

- Week 2
  1. Create and complete the Player class
  2. Make the game run continously until one player loses

- Week 3 (Final)
  1. Make game use inputs to determine whether player is attacking or defending
  2. Playtest game, and make sure you can quit without playing/finishing