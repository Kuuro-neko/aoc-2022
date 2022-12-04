import re

def partOne():
    file = open('input.txt', 'r')
    lines = file.readlines()

    count = 0

    for line in lines:
        integers = [int(s) for s in re.findall(r'\d+', line)]
        if integers[0] <= integers[2] and integers[1] >= integers[3]:
            count += 1
        elif integers[0] >= integers[2] and integers[1] <= integers[3]:
            count += 1
    return count

def partTwo():
    file = open('input.txt', 'r')
    lines = file.readlines()

    count = 0

    for line in lines:
        integers = [int(s) for s in re.findall(r'\d+', line)]
        if integers[0] <= integers[2] and integers[1] >= integers[2]:
            count += 1
        elif integers[0] >= integers[2] and integers[0] <= integers[3]:
            count += 1
    return count

print("Part 1 : " + str(partOne()))
print("Part 2 : " + str(partTwo()))
