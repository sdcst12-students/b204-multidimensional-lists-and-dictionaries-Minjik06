#!python3

# data from
# Advanced Dungeons and Dragons Dungeon Masters Guide p74 Cleric Table
# https://s3.amazonaws.com/arena-attachments/804915/348b48a0cbd967122dcb76f5cc6f5a01.pdf
"""
This list of lists contains Table 1a Attack Matrix for Clerics, Druids and Monks 
The index specifies the level of the character, and the entry within the row specifies the target to hit Armor Class with 10 on the far left, and -10 on the far right.

Write a function that finds the target based on the level and the armor class
Check the assertion tests for expected output.

Note that this could also be done with a single list and a formula to modify the list content!
"""

table = [
    [],
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25],
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25],
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25],
    [9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24],
    [9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24],
    [9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24],
    [8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23],
    [8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23],
    [8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23],
    [7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22],
    [7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22],
    [7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22],
    [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21],
    [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21],
    [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21],
    [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20],
    [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20],
    [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20],
]

# 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
def target(lvl,ac):
    k=table[lvl]
    if ac==abs(ac):
        ind=10-ac
    else :
        ind=10-(ac)
    return table[lvl][ind]

def tests():
    assert target(5,7) == 12
    assert target(10,-10) == 22
    assert target(17,-3) == 18

tests()