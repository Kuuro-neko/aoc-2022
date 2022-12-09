file = open('input.txt', 'r')
lines = file.readlines()

# i liked this one :)

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
        if length < 1:
            raise Exception('Rope length must be at least 1')
        self.rope = []
        self.rope.append(self.Knot('H', row, column))
        for n in range(1, length):
            knot = self.Knot(str(n), row, column)
            knot.set_prev(self.rope[n - 1])
            self.rope[n - 1].set_next(knot)
            self.rope.append(knot)
    
    def move_head(self, direction):
        for knot in self.rope:
            if knot.name == 'H':
                # move the head
                if direction == 'U':
                    self.rope[0].row -= 1
                elif direction == 'R':
                    self.rope[0].column += 1
                elif direction == 'D':
                    self.rope[0].row += 1
                elif direction == 'L':
                    self.rope[0].column -= 1
            elif not self.is_knot_adjacent_to_its_prev(knot):
                # move each knot diagonally towards its previous knot if it is not adjacent to it
                if knot.column < knot.prev.column:
                    knot.column += 1
                elif knot.column > knot.prev.column:
                    knot.column -= 1
                if knot.row < knot.prev.row:
                    knot.row += 1
                elif knot.row > knot.prev.row:
                    knot.row -= 1

    def is_knot_adjacent_to_its_prev(self, knot):
        if knot.prev == None:
            raise Exception('Knot ' + knot.name + ' has no previous knot')
        return abs(knot.column - knot.prev.column) <= 1 and abs(knot.row - knot.prev.row) <= 1
    
    def get_tail_row(self):
        return self.rope[len(self.rope) - 1].row
    
    def get_tail_column(self):
        return self.rope[len(self.rope) - 1].column

def compute_aoc(rope_length, size):
    bridge = []
    start = size//2
    rope = Rope(start, start, rope_length)
    for i in range(0, size):
        bridge.append([])
        for j in range(0, size):
            bridge[i].append('.')
    bridge[start][start] = 's'

    for line in lines:
        motions = line.split(' ')
        for i in range(0, int(motions[1])):
            rope.move_head(motions[0])
            bridge[rope.get_tail_row()][rope.get_tail_column()] = '#'

    count = 0
    for row in bridge:
        for column in row:
            if column == '#':
                count += 1
    return count

print("Part 1 : " + str(compute_aoc(2, 1000)))
print("Part 2 : " + str(compute_aoc(10, 1000)))