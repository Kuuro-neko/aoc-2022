import re



def partOne():
    stacks = {
        1: ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
        2: ['T', 'B', 'M', 'Z', 'R'],
        3: ['Z', 'L', 'C', 'H', 'N', 'S'],
        4: ['S', 'C', 'F', 'J'],
        5: ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
        6: ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
        7: ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
        8: ['M', 'Z', 'R'],
        9: ['M', 'C', 'L', 'G', 'V', 'R', 'T']
    }

    file = open('input_moves.txt', 'r')
    lines = file.readlines()
    
    for line in lines:
        integers = [int(s) for s in re.findall(r'\d+', line)]
        for _ in range(0, integers[0]):
            crate = stacks[integers[1]].pop()
            stacks[integers[2]].append(crate)
    
    message = ""
    for stack in stacks.values():
        message += stack.pop()
    return message

def partTwo():
    stacks = {
        1: ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
        2: ['T', 'B', 'M', 'Z', 'R'],
        3: ['Z', 'L', 'C', 'H', 'N', 'S'],
        4: ['S', 'C', 'F', 'J'],
        5: ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
        6: ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
        7: ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
        8: ['M', 'Z', 'R'],
        9: ['M', 'C', 'L', 'G', 'V', 'R', 'T']
    }
    
    file = open('input_moves.txt', 'r')
    lines = file.readlines()
    
    for line in lines:
        temp_stack = []
        integers = [int(s) for s in re.findall(r'\d+', line)]
        for _ in range(0, integers[0]):
            crate = stacks[integers[1]].pop()
            temp_stack.append(crate)
        for _ in range(0, integers[0]):
            stacks[integers[2]].append(temp_stack.pop())
    
    message = ""
    for stack in stacks.values():
        message += stack.pop()
    return message

print("Part 1 : " + str(partOne()))
print("Part 2 : " + str(partTwo()))
