def PartOne():
    file = open('input.txt', 'r')
    lines = file.readlines()

    priority = 0

    for line in lines:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        for char in firstpart:
            if char in secondpart:
                if ord(char) >= ord('a'):
                    priority += ord(char) - ord('a') + 1
                else:
                    priority += ord(char) - ord('A') + 27
                break
    return priority

def PartTwo():
    file = open('input.txt', 'r')
    lines = file.readlines()

    priority = 0

    for i in range(0, len(lines), 3):
        for char in lines[i]:
            if char in lines[i+1]:
                if char in lines[i+2]:
                    if ord(char) >= ord('a'):
                        priority += ord(char) - ord('a') + 1
                    else:
                        priority += ord(char) - ord('A') + 27
                    break

    return priority

print("Part 1 : " + str(PartOne()))
print("Part 2 : " + str(PartTwo()))
