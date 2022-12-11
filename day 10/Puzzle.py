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

def part_two(key_cycles):
    cycle = 1
    x = 1
    render = ""
    for line in lines:
        instruction = line.split(' ')
        if instruction[0] == 'addx':
            render += render_pixel(x, cycle, key_cycles)
            cycle += 1
            render += render_pixel(x, cycle, key_cycles)
            cycle += 1
            x += int(instruction[1])
        else:
            render += render_pixel(x, cycle, key_cycles)                
            cycle += 1
    return render

def render_pixel(x, cycle, key_cycles):
    ret = ""
    if (cycle % 40) >= x and (cycle % 40) <= x + 2:
        ret += "#"
    else:
        ret += "."
    if cycle in key_cycles:
        ret += "\n"
    return ret

print("Part 1 - " + str(part_one([20, 60, 100, 140, 180, 220])))
print("Part 2 - \n" + part_two([40, 80, 120, 160, 200, 240]))