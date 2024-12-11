from typing import List, Tuple


# filename = "test_input.txt"
filename = "input.txt"


with open(filename) as f:
    lines = f.readlines()

lines = [list(line.strip()) for line in lines]

map = []

for line in lines:
    map.append([int(x) for x in line])

trailheads = []
peaks = []

rows = len(map)
cols = len(map[0])

for i in range(rows):
    for j in range(cols):
        if map[i][j] == 0:
            trailheads.append((i, j))
        elif map[i][j] == 9:
            peaks.append((i, j))


def next_positions(i, j) -> List[Tuple[int, int]]:
    return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]


trailhead_scores = {x: 0 for x in trailheads}

for trailhead in trailheads:
    stack = []
    ends = set()
    stack.append(trailhead)
    while stack:
        pos = stack.pop()
        if pos in peaks:
            ends.add(pos)
            continue
        i, j = pos
        moves = next_positions(i, j)
        for move in moves:
            ni, nj = move
            if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                continue
            elif move not in ends and map[ni][nj] - map[i][j] == 1:
                stack.append(move)
    trailhead_scores[trailhead] = len(ends)

sum = 0
for score in trailhead_scores.values():
    sum += score

print(sum)
