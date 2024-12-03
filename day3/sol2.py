import re

filename = "input.txt"

with open(filename) as f:
    lines = [line.strip() for line in f.readlines()]


matches = []
sum = 0

for line in lines:
    matches.extend(re.findall(
        r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line))

go_flag = True

for match in matches:
    if match == "don't()":
        go_flag = False
        continue
    if match == "do()":
        go_flag = True
        continue
    if go_flag:
        temp = match[4:-1].split(",")
        sum += int(temp[0]) * int(temp[1])


print(sum)
