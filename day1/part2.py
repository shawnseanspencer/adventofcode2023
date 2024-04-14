file = open("elfcalib.txt")

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def todigit(wordnumber):
    number = wordnumber
    for digit in digits:
        if wordnumber == digit:
            number = digits.index(wordnumber) + 1
    return number

sum = 0
for line in file:
    chars = line.strip()
    length = len(chars)
    checker = True

    firstdigit, lastdigit = 0, 0
    firstwn, lastwn = "", ""

    wordnumbers = [] #list of all numbers that are spelled out
    numberindexes = [] #only includes indexes of wordnumbers (not actual digits)
    try:
        #creating list of all wordnumbers and their indexes in the line
        for i in range(length):
            for digit in digits:
                if digit in wordnumbers:
                    break
                elif digit in chars:
                    wordnumbers.append(digit)
                    numberindexes.append(chars.index(digit))
        wordnumdict = dict(zip(numberindexes, wordnumbers))
        wnfirstindex = min(numberindexes) + 1
        wnlastindex = max(numberindexes) + 1
        firstwn = wordnumdict[wnfirstindex - 1]
        lastwn = wordnumdict[wnlastindex - 1]
    except ValueError: 
        wnfirstindex, wnlastindex = 'hi', 'bye' #just placeholders for later 'try: except' clause
        
    #finding first numerical digit
    for i in range(length):
        if chars[i].isdigit():
            firstdigit = chars[i]
            firstindex = chars.index(firstdigit)
            break


    #finding last numerical digit
    j = length - 1
    while j >= 0:
        if chars[j].isdigit():
            lastdigit = chars[j]
            lastindex = chars.index(lastdigit)
            break
        j += -1

    firstwn, lastwn = todigit(firstwn), todigit(lastwn)
    candidates = [firstwn, lastwn, firstdigit, lastdigit]
    candidateindexes =  [wnfirstindex, wnlastindex, firstindex, lastindex]
    candidatedict = dict(zip(candidateindexes, candidates))
    try:
        if checker:
            first = candidatedict[min(candidateindexes)]
            last = candidatedict[max(candidateindexes)]
        else:
            first = candidatedict[min(candidateindexes[0:2])]
            last = candidatedict[max(candidateindexes[0:2])]
    except TypeError:
        first = candidatedict[min(candidateindexes[2:4])]
        last = candidatedict[max(candidateindexes[2:4])]
    print(candidates, candidateindexes)
    number = int(f"{first}{last}")
    sum += number

    print(number)

print(sum)
