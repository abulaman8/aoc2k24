import re

filename = "test_input.txt"

with open(filename) as f:
    lines = [line.strip() for line in f.readlines()]


matches = []
sum = 0

for line in lines:
    matches.extend(re.findall(r"mul\(\d{1,3},\d{1,3}\)", line))

for match in matches:
    temp = match[4:-1].split(",")
    sum += int(temp[0]) * int(temp[1])

print(sum)
