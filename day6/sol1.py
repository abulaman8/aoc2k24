import os
from time import sleep

filename = "test_input.txt"
# filename = "input.txt"


with open(filename, "r") as f:
    lines = f.readlines()
data = []
for line in lines:
    data.append(list(line.strip()))

seen = set()
start = (0, 0)
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "^":
            start = (i, j)
            break
seen.add(start)


def print_matrix(matrix):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in matrix:
        print(" ".join(map(str, row)))


def move(i, j):
    if data[i][j] == "^":
        return (i-1, j)
    if data[i][j] == "v":
        return (i+1, j)
    if data[i][j] == ">":
        return (i, j+1)
    if data[i][j] == "<":
        return (i, j-1)
    else:
        raise Exception("Gaurd not found")


def move_right(i, j):
    if data[i][j] == "^":
        data[i][j] = ">"
        return (i, j+1)
    if data[i][j] == "v":
        data[i][j] = "<"
        return (i, j-1)
    if data[i][j] == ">":
        data[i][j] = "v"
        return (i+1, j)
    if data[i][j] == "<":
        data[i][j] = "^"
        return (i-1, j)
    else:
        raise Exception("Gaurd not found")


current_position = (start[0], start[1])
while True:
    # print(f"current position {current_position}")
    i, j = move(current_position[0], current_position[1])
    if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]):
        break
    if data[i][j] == "#":
        i, j = move_right(current_position[0], current_position[1])
        # print(f"trying right from {current_position} to ({i}, {j})")
    if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]):
        break
    seen.add((i, j))
    data[i][j] = data[current_position[0]][current_position[1]]
    print_matrix(data)
    sleep(0.5)
    current_position = (i, j)

print(len(seen))
