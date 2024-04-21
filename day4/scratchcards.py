import re

with open("input4.txt") as file:
    lines = file.read().strip().split('\n')

    cards = dict()
    for _ in range(len(lines)):
        cards[_] = [1,0]

    #Part 1
    tot1 = 0
    for i, line in enumerate(lines):
        nums = line[10:].split(" | ")
        winners = nums[0].split(" ")
        gambles = nums[1].split(" ")

        wins = []

        for gamble in gambles:
            if gamble in winners and gamble != "":
                wins.append(int(gamble))
        
        wincount = len(wins)
        if len(wins) != 0:
            tot1 += 2**(len(wins)-1)

        #Part 2
        for j in range(i+1, i+1+wincount):
            cards[j][0] += cards[i][0]

    tot2 = 0
    for card in cards.values():
        tot2 += card[0]

    print("Part 1:", tot1) 
    print("Part 2:", tot2)


    


        
