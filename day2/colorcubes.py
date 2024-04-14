#Part 1
import re

file = open("input.txt")

red, green, blue = 12, 13, 14

sum1 = 0
sum2 = 0
for item in file:
    line = item.strip()
    length = len(line)
    games = line[8:length].split(";")

    id = int(re.sub(r"\D", "", line[5:8]))
    test = True

    redmin, bluemin, greenmin = 0, 0, 0
    
    for draw in games:
        
        draw = draw.split(',')

        for part in draw:
            roll = int(re.sub(r"\D", "", part))
            color = re.sub(r"[\d\s]", "", part)

            if color == "red" and roll > red or (
                color == "blue" and roll > blue) or (
                color == "green" and roll > green):

                test = False
            
            #part 2
            if color == "red" and redmin < roll:
                redmin = roll
            if color == "blue" and bluemin < roll:
                bluemin = roll
            if color == "green" and greenmin < roll:
                greenmin = roll

            
    if test:
        sum1 += id
    sum2 += redmin * greenmin * bluemin

print("p1:", sum1)
print("p2:", sum2)

    



