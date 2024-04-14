#A few assumptions:
#1. There are only up to 3 digit numbers
#2. All symbols in the "symbols" variable are the only ones that count

with open("input.txt") as file:

    symbols = "!@#$%^&*()-+?_=,<>/"

    lines = []
    for line in file:
        lines.append(line.strip())

    partnums = []

    column_num = len(lines[0])
    row_num = len(lines)
    s_indexes = []
    s = []
    num_indexes = []
    nums = []

    for i in range(row_num):
        j = 0
        while j < column_num:
            if lines[i][j] in symbols:
                s_indexes.append([i,j])
                s.append(lines[i][j])

            if lines[i][j].isdigit():
                num = []
                num_index = []
                try:
                    while lines[i][j].isdigit():
                        num.append(lines[i][j])
                        num_index.append([i,j])
                        j += 1
                except IndexError:
                    None
                num_indexes.append(num_index)
                nums.append(num)
            else:
                j += 1

    for i in range(len(nums)):
        num = nums[i]
        matrix = [-1,0,1]
        for j in range(len(num)):
            num_index = num_indexes[i][j]
            for horizontal_shift in matrix:
                for vertical_shift in matrix:
                    adjacenth = num_index[1] + horizontal_shift
                    adjacentv = num_index[0] + vertical_shift
                    if [adjacentv,adjacenth] in s_indexes:
                        partnums.append(int("".join(num)))
                        break
                else:
                    continue
                break
            else:
                continue
            break

    #part 2
    gear_ratios = []
    stars = []
    star_indexes = []
    #TODO: Check if a star is adjacent to 2 numbers, find those numbers and multiply them, then add to gear ratio sum
    matrix = [-1,0,1]
    for i in range(len(s)):
        if s[i] != '*':
            continue
        s_index = s_indexes[i]

        adjacent_matrix = []
        for horizontal_shift in matrix:
            for vertical_shift in matrix:
                adjacenth = s_index[1] + horizontal_shift
                adjacentv = s_index[0] + vertical_shift
                adjacent_matrix.append([adjacentv,adjacenth])

        count = 0
        gear_nums = []
        for j in range(len(nums)):
            num = nums[j]
            for k in range(len(num)):
                num_index = num_indexes[j][k]
                if num_index in adjacent_matrix:
                    gear_nums.append(int("".join(num)))
                    count += 1
                    break
        if count == 2:
            gear_ratios.append(gear_nums[0] * gear_nums[1])
            print(gear_nums)

#print(star_indexes)
print(sum(gear_ratios))
print(sum(partnums))
