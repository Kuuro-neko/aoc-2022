file = open('input.txt', 'r')
line = file.readlines()
string = line[0]

def partOne(string):
    for i in range(0, len(string)):
        print(string[i:i+4])
        if string.count(string[i], i, i+4) == 1 and string.count(string[i+1], i, i+4) == 1 and string.count(string[i+2], i, i+4) == 1 and string.count(string[i+3], i, i+4) == 1:
            return i+4

def true_for_all(string, i):
    for j in range(0, 13):
        if string.count(string[i+j], i, i+14) != 1:
            return False
    return True

def partTwo(string):
    string = line[0]

    for i in range(0, len(string)):
        print(string[i:i+14])
        if true_for_all(string, i):
            return i+14

print("Part 1 : " + str(partOne(string)))
print("Part 2 : " + str(partTwo(string)))
