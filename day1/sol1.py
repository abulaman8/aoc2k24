filename = "input.txt"
with open(filename, "r") as f:
    data = f.read().splitlines()

l1 = []
l2 = []
diffs = []

for i in data:
    nums = i.split()
    l1.append(int(nums[0]))
    l2.append(int(nums[1]))
l1.sort()
l2.sort()

for i, j in zip(l1, l2):
    diffs.append(abs(i-j))

print(sum(diffs))
