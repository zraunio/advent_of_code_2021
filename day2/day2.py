import sys

#PART1 & PART2
#make down increase depth, make up decrease depth
#reading and parsing strings, strcmp, etc.
horizon = 0
aim = 0
depth = 0
file = open("/Users/raunzo/python advent of code/day2/map", "r")

while file != None:
    line = file.readline()
    instruct = line.split(' ', 1)
    if instruct[0] == 'forward':
        horizon += int(instruct[1])
        depth += (aim * int(instruct[1])) 
    elif instruct[0] == 'down':
        aim += int(instruct[1])
    elif instruct[0] == 'up':
        aim -= int(instruct[1])
    if not line or not instruct:
        break

print("position is:", horizon * depth)
file.close()

#PART2
