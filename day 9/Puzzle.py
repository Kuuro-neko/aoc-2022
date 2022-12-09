file = open('input.txt', 'r')
lines = file.readlines()

class Rope:
    class Knot:
        def __init__(self, name, row, column):
            self.name = name
            self.row = row
            self.column = column
            self.prev = None
            self.next = None
        
        def set_next(self, next):
            self.next = next

        def set_prev(self, prev):
            self.prev = prev

    def __init__(self, row, column, length):
        self.rope = []
        self.rope.append(self.Knot('H', row, column))
        for n in range(1, length+1):
            knot = self.Knot(str(n), row, column)
            knot.set_prev(self.rope[n - 1])
            self.rope[n - 1].set_next(knot)
            self.rope.append(knot)
    
    def move_head(self, direction):
        prev_knot_row = self.rope[0].row
        prev_knot_column = self.rope[0].column
        if direction == 'U':
            self.rope[0].row -= 1
        elif direction == 'R':
            self.rope[0].column += 1
        elif direction == 'D':
            self.rope[0].row += 1
        elif direction == 'L':
            self.rope[0].column -= 1
        for knot in self.rope:
            if knot.name == 'H':
                continue
            if not self.is_knot_adjacent_to_its_prev(knot):
                current_prev_knot_row = knot.row
                current_prev_knot_column = knot.column
                knot.row = prev_knot_row
                knot.column = prev_knot_column
                prev_knot_row = current_prev_knot_row
                prev_knot_column = current_prev_knot_column

    def is_knot_adjacent_to_its_prev(self, knot):
        if knot.prev == None:
            return False
        return abs(knot.column - knot.prev.column) <= 1 and abs(knot.row - knot.prev.row) <= 1

    def get_head_row(self):
        return self.rope[0].row
    
    def get_head_column(self):
        return self.rope[0].column
    
    def get_tail_row(self):
        return self.rope[len(self.rope) - 1].row
    
    def get_tail_column(self):
        return self.rope[len(self.rope) - 1].column
    
def rotate_direction(direction):
    if direction == 'U':
        return 'R'
    elif direction == 'R':
        return 'D'
    elif direction == 'D':
        return 'L'
    elif direction == 'L':
        return 'U'

rope = Rope(0, 0, 1)
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
        bridge[rope.get_tail_row()][rope.get_tail_column()] = '#'
count = 0
for row in bridge:
    for column in row:
        if column == '#':
            count += 1
            
print("Part 1 : " + str(count))