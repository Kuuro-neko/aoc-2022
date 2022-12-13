import collections

"""
First day i struggle too much without help
Got help from here : https://stackoverflow.com/questions/47896461/get-shortest-path-to-a-cell-in-a-2d-array-in-python
Learnt a lot in this day :)
"""

file = open('input.txt', 'r')
lines = file.readlines()

y = 0
map = []
for line in lines:
    map.append([])
    x = 0
    for char in line:
        if char == 'S':
            start = (x, y)
            map[y].append('a')
            x += 1
        elif char != '\n':
            map[y].append(char)
            x += 1
    y += 1

def step_possible(start, end):
    height_start = ord(start) - ord('a')
    if end == 'E':
        height_end = ord('z') - ord('a')
    else:
        height_end = ord(end) - ord('a')
    return height_start+1 >= height_end

def part_one(map, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if map[y][x] == 'E':
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < len(map[0]) and 0 <= y2 < len(map) and (x2, y2) not in seen:
                if step_possible(map[y][x], map[y2][x2]):
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))

def part_two(map):
    steps = []
    for x in range(len(map[0])):
        for y in range(len(map)):
            if map[y][x] == 'a':
                try:
                    steps.append(len(part_one(map, (x, y)))-1)
                except:
                    pass # Bruh it worked
    return min(steps)

print("Part 1 - " + str(len(part_one(map, start))-1))
print("Part 2 - " + str(part_two(map)))