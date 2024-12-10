# filename = "test_input.txt"
filename = "input.txt"

with open(filename) as f:
    lines = f.readlines()

line = list(lines[0].strip())
nums = [int(x) for x in line]

i = 0
fid = 0
diskmap = []
while i < len(nums):

    if i % 2 == 0:
        for _ in range(nums[i]):
            diskmap.append(fid)
        fid += 1
    else:
        for _ in range(nums[i]):
            diskmap.append(".")
    i += 1


total_size = len(diskmap)
free_space = 0
for i in diskmap:
    if i == ".":
        free_space += 1


movable = []


i = 1
while True:
    if len(movable) == free_space:
        break
    else:
        if diskmap[-i] != ".":
            movable.append(diskmap[-i])
        i += 1

mi = 0
i = 0
checksum = 0
while i < total_size - free_space:
    if diskmap[i] == ".":
        checksum += movable[mi] * i
        mi += 1
        i += 1
    else:
        checksum += diskmap[i] * i
        i += 1

print(checksum)
