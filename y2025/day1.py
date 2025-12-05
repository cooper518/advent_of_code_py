# collect raw lines of input
raw_input = []
with open("day1.txt", "r") as file:
    raw_input = [l.strip() for l in file.readlines()]

# input line format as XY where X in [R, L] and Y is int >= 0
# dial starts at 50, each line moves dial L or R Y amount
# dial overflows with range [0,99]
# part 1 count each time dial points to zero after an instruction
# part 2 count each time dial points to zero at any time

# input dial and rotation "command"
# return dial and number of times 0 was crossed
def process_rotation(dial: int, rotation: int) -> tuple[int, int]:
    zero_crossed = 0
    new_dial = dial
    direction = -1 if rotation[0] == "L" else 1
    amount = int(rotation[1:])
    for i in range(amount):
        new_dial = rotate_step(new_dial, direction)
        if new_dial == 0:
            zero_crossed += 1
    return new_dial, zero_crossed

# process one step of rotation of dial and return new dial state
def rotate_step(dial: int, direction: int):
    new_dial = dial + direction
    # handle positive overflow
    if new_dial == 100:
        new_dial = 0
    # handle negative overflow
    elif new_dial == -1:
        new_dial = 99
    return new_dial
    

def part1():
    dial = 50
    count = 0

    for line in raw_input:
        dial, _ = process_rotation(dial, line)
        count += 1 if dial == 0 else 0

    print("Day 1 Part 1: ", count)

def part2():
    dial = 50
    count = 0

    for line in raw_input:
        dial, zero = process_rotation(dial, line)
        count += zero

    print("Day 1 Part 2: ", count)

part1()
part2()