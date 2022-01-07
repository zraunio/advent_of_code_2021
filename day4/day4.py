import sys

#PART1
#bingo system. this is an algorythm you know i hate those why
#they require i keep things stored in my head and i can't do that
#if we wind the number, replace with SYMBOL (X), check every row every time for 5 x X

file = open("/Users/raunzo/adv_of_code_22/day4/scoreboard", "r")
numbers_drawn = file.readline().split(",")

bingos = file.read().split("\n")
list_len = len(bingos)
line_len = len(bingos[1])
sets = bingos
x = 0
set_nr = 1
while x < list_len:
    sets[x] = bingos[x].split(" ", 5)
    x += 1
x = 0
while x < list_len:
    mark = 0
    # print("SET NR ", set_nr, '\n')
    while x < list_len:
        index = 0
        while index < line_len:
            if sets[x][index] == '\n' or sets[x][index] == '':
                index += 1
            else:
                print(int(sets[x][index]), " ")
            index += 1
        # if int(bingos[x][index]) == int(numbers_drawn[x]):
        #     bingos[x][index] = 'X'
    x += 1
    if x % 5 == 0:
        set_nr += 1
