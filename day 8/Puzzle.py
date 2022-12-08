import re

file = open('input.txt', 'r')
lines = file.readlines()

# Create a 2D array of the trees
trees = []
for line in lines:
    tree_row = []
    for char in line:
        if char != '\n':
            tree_row.append(int(char))
    trees.append(tree_row)

# Return a list of the trees in the row, for the given range
def get_trees_in_row_range(row, start, end):
    trees_in_row_range = []
    for i in range(start, end):
        trees_in_row_range.append(trees[row][i])
    return trees_in_row_range

# Return a list of the trees in the column, for the given range
def get_trees_in_column_range(column, start, end):
    trees_in_column_range = []
    for i in range(start, end):
        trees_in_column_range.append(trees[i][column])
    return trees_in_column_range

# Return the viewing distance in the row, for the given range. Direction = 1 for left to right, -1 for right to left
def get_viewing_distance_in_row(row, column, start, end, direction):
    viewing_distance = 0
    last_tree = 0
    for i in range(start, end, direction):
        # while the last tree is lower than the current tree, add 1 to the viewing distance
        if trees[row][column] <= last_tree:
            break
        viewing_distance = viewing_distance + 1
        last_tree = trees[row][i]
    return viewing_distance

# Return the viewing distance in the column, for the given range. Direction = -1 for top to bottom, 1 for bottom to top
def get_viewing_distance_in_column(row, column, start, end, direction):
    viewing_distance = 0
    last_tree = 0
    for i in range(start, end, direction):
        # while the last tree is lower than the current tree, add 1 to the viewing distance
        if trees[row][column] <= last_tree:
            break
        viewing_distance = viewing_distance + 1
        last_tree = trees[i][column]
    return viewing_distance

# Return true if all the numbers in the int_list are strictly lower than the int
def all_lower(int, int_list):
    for i in int_list:
        if int <= i:
            return False
    return True

tree_count = 0
highest_scenic_score = 0
for row in range(len(trees)):
    for column in range(len(trees[row])):
        visible = False
        if row == 0 or row == len(trees) or column == 0 or column == len(trees[row]): # edges of the square
            tree_count = tree_count + 1
            visible = True
        else: # not an edge, if any of the 4 surrounding direction have all the trees lower, then it is visible
            if all_lower(trees[row][column], get_trees_in_row_range(row, 0, column)) or all_lower(trees[row][column], get_trees_in_row_range(row, column + 1, len(trees[row]))) or all_lower(trees[row][column], get_trees_in_column_range(column, 0, row)) or all_lower(trees[row][column], get_trees_in_column_range(column, row + 1, len(trees))):
                tree_count = tree_count + 1
                visible = True
        # Calculate the scenic score and compare it to the highest scenic score
        if visible:
            west = get_viewing_distance_in_row(row, column, column-1, -1, -1)
            east = get_viewing_distance_in_row(row, column, column+1, len(trees[row]), 1)
            north = get_viewing_distance_in_column(row, column, row-1, -1, -1)
            south = get_viewing_distance_in_column(row, column, row+1, len(trees), 1)
            current_scenic_score = west * east * north * south
            if current_scenic_score > highest_scenic_score:
                highest_scenic_score = current_scenic_score
        

print("Part 1 - " + str(tree_count))
print("Part 2 - " + str(highest_scenic_score))