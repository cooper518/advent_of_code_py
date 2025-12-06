import itertools

raw_input = []
with open("day2.txt", "r") as file:
    raw_input = [l.split("-") for l in file.readline().strip().split(",")]

# ranges are expressed as X-Y
# invalid IDs are IDs within the range that are 2 identical substrings
# ex. 4545 or 13871387
# for part 1 sum all invalid IDs

def is_invalid(i: int) -> bool:
    s = str(i)
    return s[:len(s)//2] == s[len(s)//2:]

# for part 2, ID is invalid if count of any substring is > 1
def is_invalid_2(i: int) -> bool:
    s = str(i)
    pass

def part1():
    # convert ranges from input to range objects
    ranges = map(lambda x: range(int(x[0]), int(x[1])), raw_input)
    # filter ranges and sum invalids
    invalid_sum = sum([sum(filter(is_invalid, r)) for r in ranges])
    print("Day 2 Part 1: ", invalid_sum)

def part2():
    # convert ranges from input to range objects
    ranges = map(lambda x: range(int(x[0]), int(x[1])), raw_input)
    # filter ranges and sum invalids
    invalid_sum = sum([sum(filter(is_invalid_2, r)) for r in ranges])
    print("Day 2 Part 2: ", invalid_sum)

part1()