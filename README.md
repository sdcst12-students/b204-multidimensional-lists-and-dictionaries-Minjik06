## SDSS Computing Studies Python Assignment


Objectives:
* Retrieve data from lists of lists 
* Retrieve data from lists of dictionaries
* Retrieve data from dictionaries with lists

Once we start needing to track more data, we need to start incorporating multiple dictionaries, or data structures that are dictionaries that might contain lists, or dictionaries that might contain dictionaries!

You can imagine a game like Pokemon, where there are multiple Pokemon that have some basic statistics, and we could track their stats with a dictionary.

Consider:
```
pokemon = {
    'name' : 'Tinkatink',
    'category' : 'Metalsmith',
    'types' : ['Fairy','Steel'],
    'hp' : 3,
    'attack' : 3,
    'defense' : 3,
    'spAtk' : 3,
    'spDef' : 4,
    'speed' : 4
}
```
Notice that we have included a list in the definition of this dictionary, because it belongs to multiple types.
However, there are many pokemon, so we might create a Pokedex to keep track of them:
```
pokedex = []
pokedex.append(pokemon)
```

So how do we access data within this array?  Let's take a look at the code in example1.py

##### Task 1 Simple extraction
data from
Advanced Dungeons and Dragons Dungeon Masters Guide p74 Cleric Table
https://s3.amazonaws.com/arena-attachments/804915/348b48a0cbd967122dcb76f5cc6f5a01.pdf

This list of lists contains Table 1a Attack Matrix for Clerics, Druids and Monks 
The index specifies the level of the character, and the entry within the row specifies the target to hit Armor Class with 10 on the far left, and -10 on the far right.

Write a function that finds the target based on the level and the armor class
Check the assertion tests for expected output.

##### Task 2 Home and Away
There are teams representing each province and territory playing in a new E-Sports league.  The records for each game are included in the list titled 'games'
Iterate throught the list and determine the wins and losses for each team.

Create a dictionary for each team and store their number of wins, games played,
goals for and goals against.  A dictionary template has been prepped for you to 
use, although you can probably build one faster using iteration or list comprehension
