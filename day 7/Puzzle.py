from enum import Enum

Type = Enum('Type', ['DIR', 'FILE'])

class Node:
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
        self.children = {}
        self.parent = None
    
    def add_child(self, child):
        self.children[child.name] = child

    def set_parent(self, parent):
        self.parent = parent
    
    def get_children(self, name):
        return self.children[name]

    def exists_children(self, name):
        return name in self.children.keys()

    def to_string(self, level):
        string = ""
        for _ in range(level):
            string += "  "
        string += "- " + self.name + " " + str(self.type) + " " + str(self.size) + "\n"
        for child in self.children:
            string += str(self.children[child].to_string(level + 1))
        return string
    
    def get_size(self):
        if self.type == Type.FILE:
            return self.size
        else:
            return_size = 0
            for child in self.children:
                return_size += self.children[child].get_size()
            return return_size
    
    def part_one(self):
        if self.type == Type.DIR:
            if self.get_size() <= 100000:
                return_size = self.get_size()
            else:
                return_size = 0
            for child in self.children:
                return_size += self.children[child].part_one()
            return return_size
        else:
            return 0

        def __str__(self):
            return self.name + " " + str(self.type) + " " + str(self.size)


file = open('input.txt', 'r')
lines = file.readlines()
# deleted the first line of input.txt ($ cd /) assuming we start here
current_node = Node("/", Type.DIR, 0)
starting_node = current_node

for line in lines:
    infos = line.split()
    print(infos)
    # the only command that have effect is cd, do nothing on ls and create the file/dir when line doesn't start with $
    if infos[0] == '$':
        if infos[1] == 'cd':
            if infos[2] == '..':
                current_node = current_node.parent
            elif current_node.exists_children(infos[2]):
                current_node = current_node.get_children(infos[2])
    elif infos[0] == 'dir':
        new_dir = Node(infos[1], Type.DIR, 0)
        current_node.add_child(new_dir)
        new_dir.set_parent(current_node)
    else:
        new_file = Node(infos[1], Type.FILE, int(infos[0]))
        current_node.add_child(new_file)
        new_file.set_parent(current_node)

print("Part 1 : " + str(starting_node.part_one()))

disk_space = 70000000
needed_disk_space = 30000000
occupied_disk_space = starting_node.get_size()
disk_space_to_free = occupied_disk_space - disk_space + needed_disk_space

print("Part 2 : ")
print("Disk space : " + str(disk_space) + " | Occupied disk space : " + str(occupied_disk_space) + " | Needed disk space : " + str(needed_disk_space) + " | Disk space to free : " + str(disk_space_to_free))


