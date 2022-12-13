file = open('input.txt', 'r')
lines = file.readlines()

# Part 1
packet = []
for first, second in (lines[i:i+2] for i in range(0, len(lines), 3)):
    pair = []
    pair.append(eval(first))
    pair.append(eval(second))
    packet.append(pair)

def correct_order(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return "equal"
    elif type(left) == list and type(right) == list:
        if len(left) == len(right) == 0:
            return "equal"
        elif len(left) == 0:
            return True
        elif len(right) == 0:
            return False
        res = correct_order(left[0], right[0])
        if res == "equal":
            return correct_order(left[1:], right[1:])
        else:
            return res
    elif type(left) == int:
        return correct_order([left], right)
    else:
        return correct_order(left, [right])

sum = 0
for i in range(len(packet)):
    if correct_order(packet[i][0], packet[i][1]):
        sum += i+1

print(sum)