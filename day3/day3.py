#PART1
#need to hold data constantly as parsing strings continues
#most common bit can be discovered via bit operations 
#while loop going through each line split into 2d array, traverse each line on same location
#count if 1 and if 0, print each result right away, move another step up, reset line count to 0
####This Part1 solution is insuficient to solve riddle; it does not produce the correct  opposite of gamma when using bitwise logic operators
####Using ~gamma yielded wrong results
####Compelling python to use binary numbers didn't work
####needs revision and further investigation of binary values in python
def binaryToDecimal(binary):  
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal) 

file = open("/Users/raunzo/adv_of_code_22/day3/diagnostic", "r")
list = file.read().split("\n", 999)
i = 0
x = 0
while i < 12:
    x = 0
    ones = 0
    zeros = 0
    while x < 999:
        if (int(list[x][i]) == 1):
            ones += 1
        else:
            zeros += 1
        x+=1
    if ones > zeros:
        print(1)
    else:
        print (0)
    i+=1
file.close()

print(binaryToDecimal(101000101001) * binaryToDecimal(0b010111010110))
