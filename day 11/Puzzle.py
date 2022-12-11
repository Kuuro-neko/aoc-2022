from math import lcm
from functools import reduce

class Monkey:
    """
        class Monkey
        name: name of the monkey
        starting_items: list of items the monkey starts with (list of integers)
        operator: operator used to compute the item throw (string)
        operand: operand used to compute the item throw (integer or string "old")
        test: test used to decide which monkey to send the item to (integer)
        RETURN TO MONKE
    """
    def __init__(self, name, starting_items, operator, operand, test, part_one=True, part_two_lcm=None):
        self.name = name
        self.items = starting_items
        self.operator = operator
        self.operand = operand
        self.test = test
        self.monkey_true = None
        self.monkey_false = None
        self.activity = 0
        self.part_one = part_one
        self.part_two_lcm = part_two_lcm
    
    def set_monkey_true(self, monkey):
        self.monkey_true = monkey
    
    def set_monkey_false(self, monkey):
        self.monkey_false = monkey
    
    def catch_item(self, item):
        self.items.append(item)
    
    def throw_all_items(self):
        for item in self.items:
            self.activity += 1
            # Monkey examines item
            if self.operand == "old":
                new_operand = item
            else:
                new_operand = self.operand
            operation = str(item) + self.operator + str(new_operand)
            new_item = eval(operation)
            # Monkey tests item
            if self.part_one == True: # Test of part one
                new_item = round(new_item // 3)
            else: # Test of part two
                remainder = new_item % self.part_two_lcm
                new_item = remainder
            # Monkey throws item to the right monkey
            if new_item % self.test == 0:
                self.monkey_true.catch_item(new_item)
            else:
                self.monkey_false.catch_item(new_item) 
        self.items = []

# Part one
monkey_0 = Monkey("Monkey 0", [89, 73, 66, 57, 64, 80], "*", 3, 13)
monkey_1 = Monkey("Monkey 1", [83, 78, 81, 55, 81, 59, 69], "+", 1, 3)
monkey_2 = Monkey("Monkey 2", [76, 91, 58, 85], "*", 13, 7)
monkey_3 = Monkey("Monkey 3", [71, 72, 74, 76, 68], "*", "old", 2)
monkey_4 = Monkey("Monkey 4", [98, 85, 84], "+", 7, 19)
monkey_5 = Monkey("Monkey 5", [78], "+", 8, 5)
monkey_6 = Monkey("Monkey 6", [86, 70, 60, 88, 88, 78, 74, 83], "+", 4, 11)
monkey_7 = Monkey("Monkey 7", [81, 58], "+", 5, 17)
monkey_0.set_monkey_true(monkey_6)
monkey_0.set_monkey_false(monkey_2)
monkey_1.set_monkey_true(monkey_7)
monkey_1.set_monkey_false(monkey_4)
monkey_2.set_monkey_true(monkey_1)
monkey_2.set_monkey_false(monkey_4)
monkey_3.set_monkey_true(monkey_6)
monkey_3.set_monkey_false(monkey_0)
monkey_4.set_monkey_true(monkey_5)
monkey_4.set_monkey_false(monkey_7)
monkey_5.set_monkey_true(monkey_3)
monkey_5.set_monkey_false(monkey_0)
monkey_6.set_monkey_true(monkey_1)
monkey_6.set_monkey_false(monkey_2)
monkey_7.set_monkey_true(monkey_3)
monkey_7.set_monkey_false(monkey_5)

monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
for _ in range(0, 20):
    for monkey in monkeys:
        monkey.throw_all_items()

activities = []
for monkey in monkeys:
    activities.append(monkey.activity)
activities.sort(reverse=True)
print("Part 1 - " + str((activities[0] * activities[1])))

# Part two
# The trick here is to divide the items by the LCM of the value of the tests and keep only the remainder so the number becomes really small but the test stays the same since it's a congruence
part_two_lcm = reduce(lcm,(13,3,7,2,19,5,11,17))
monkey_0 = Monkey("Monkey 0", [89, 73, 66, 57, 64, 80], "*", 3, 13, False, part_two_lcm)
monkey_1 = Monkey("Monkey 1", [83, 78, 81, 55, 81, 59, 69], "+", 1, 3, False, part_two_lcm)
monkey_2 = Monkey("Monkey 2", [76, 91, 58, 85], "*", 13, 7, False, part_two_lcm)
monkey_3 = Monkey("Monkey 3", [71, 72, 74, 76, 68], "*", "old", 2, False, part_two_lcm)
monkey_4 = Monkey("Monkey 4", [98, 85, 84], "+", 7, 19, False, part_two_lcm)
monkey_5 = Monkey("Monkey 5", [78], "+", 8, 5, False, part_two_lcm)
monkey_6 = Monkey("Monkey 6", [86, 70, 60, 88, 88, 78, 74, 83], "+", 4, 11, False, part_two_lcm)
monkey_7 = Monkey("Monkey 7", [81, 58], "+", 5, 17, False, part_two_lcm)
monkey_0.set_monkey_true(monkey_6)
monkey_0.set_monkey_false(monkey_2)
monkey_1.set_monkey_true(monkey_7)
monkey_1.set_monkey_false(monkey_4)
monkey_2.set_monkey_true(monkey_1)
monkey_2.set_monkey_false(monkey_4)
monkey_3.set_monkey_true(monkey_6)
monkey_3.set_monkey_false(monkey_0)
monkey_4.set_monkey_true(monkey_5)
monkey_4.set_monkey_false(monkey_7)
monkey_5.set_monkey_true(monkey_3)
monkey_5.set_monkey_false(monkey_0)
monkey_6.set_monkey_true(monkey_1)
monkey_6.set_monkey_false(monkey_2)
monkey_7.set_monkey_true(monkey_3)
monkey_7.set_monkey_false(monkey_5)

monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
for _ in range(0, 10000):
    for monkey in monkeys:
        monkey.throw_all_items()

activities = []
for monkey in monkeys:
    activities.append(monkey.activity)
activities.sort(reverse=True)
print("Part 2 - " + str((activities[0] * activities[1])))