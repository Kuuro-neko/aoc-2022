file = open('input.txt', 'r')
lines = file.readlines()

class Rope:
    def __init__(self, row, column):
        self.head_row = row
        self.head_column = column
        self.tail_row = row
        self.tail_column = column
    
    def move_head(self, direction):
        if direction == 'U':
            self.head_row -= 1
        elif direction == 'D':
            self.head_row += 1
        elif direction == 'L':
            self.head_column -= 1
        elif direction == 'R':
            self.head_column += 1
        if not self.is_tail_adjacent_to_head():
            self.move_tail_towards_head()

    def move_tail_towards_head(self):
        if self.head_row > self.tail_row:
            self.tail_row += 1
        elif self.head_row < self.tail_row:
            self.tail_row -= 1
        if self.head_column > self.tail_column:
            self.tail_column += 1
        elif self.head_column < self.tail_column:
            self.tail_column -= 1
    
    def is_tail_adjacent_to_head(self):
        return (abs(self.head_row - self.tail_row) <= 1 and abs(self.head_column - self.tail_column) <= 1)

    def get_head(self):
        return (self.head_row, self.head_column)
    
    def get_tail(self):
        return (self.tail_row, self.tail_column)
    
def rotate_direction(direction):
    if direction == 'U':
        return 'R'
    elif direction == 'R':
        return 'D'
    elif direction == 'D':
        return 'L'
    elif direction == 'L':
        return 'U'

rope = Rope(0, 0)
bridge = []
size = 1000

for i in range(0, size):
    bridge.append([])
    for j in range(0, size):
        bridge[i].append('.')
bridge[0][0] = 's'

for line in lines:
    motions = line.split(' ')
    for i in range(0, int(motions[1])):
        rope.move_head(rotate_direction(motions[0]))
        bridge[rope.tail_row][rope.tail_column] = '#'

count = 0
for row in bridge:
    for column in row:
        if column == '#':
            count += 1
            
print("Part 1 : " + str(count))