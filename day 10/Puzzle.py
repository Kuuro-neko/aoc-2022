file = open('input.txt', 'r')
lines = file.readlines()

def part_one(key_cycles):
    cycle = 1
    x = 1
    sum = 0
    for line in lines:
        instruction = line.split(' ')
        if cycle in key_cycles:
            sum += x * cycle
        if instruction[0] == 'addx':
            cycle += 1
            if cycle in key_cycles:
                sum += x * cycle
            x += int(instruction[1])
        cycle += 1
    return sum

print("Part 1 - " + str(part_one([20, 60, 100, 140, 180, 220])))