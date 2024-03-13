file = open("elfcalib.txt")
sum = 0
for line in file:
    chars = line.strip()
    length = len(chars)

    for i in range(length):
        if chars[i].isdigit():
            first = chars[i]
            break
    j = length - 1
    while j >= 0:
        if chars[j].isdigit():
            last = chars[j]
            break
        j += -1
    number = int(f"{first}{last}")
    sum += number
    print(number)

print(sum)
