import sys
#PART1
#reading a file using open, could read line by line with readline
#when comparing must cast correct variable
#always close
i = 0
file = open("/Users/raunzo/python advent of code/input", "r")
line2 = file.readline()

while file != None:
    line1 = line2
    line2 = file.readline()
    if not line1 or not line2:
        print("file is done")
        print(i)
        break
    elif int(line1) < int(line2):
        i+=1

file.close()

#PART2
#count every three but come back two for next window
# 199  A      
# 200  A B    
# 208  A B C  
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G  
# 269    F G H
# 260      G H
# 263        H

i = 0
file = open("/Users/raunzo/python advent of code/input", "r")
hold1 = file.readline()
hold2 = file.readline()
hold3 = file.readline()

while file != None:
    line1 = hold1
    line2 = hold2
    line3 = hold3
    hold1 = line2
    hold2 = line3
    if line1 and line2 and line3:
        sum = int(line1) + int(line2) + int(line3)
    hold3 = file.readline()
    if hold1 and hold2 and hold3:
        comp = int(hold1) + int(hold2) + int(hold3)
    if not line1 or not line2 or not line3 or not hold1 or not hold2 or not hold3:
        print("file is done")
        print(i)
        break
    elif sum < comp:
        i+=1

file.close()



