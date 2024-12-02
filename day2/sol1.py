filename = "input.txt"

with open(filename, "r") as f:
    data = f.read().splitlines()


lists = []
diffs = []
safe = []
unsafe = []

for line in data:
    nums = line.split()
    temp = []
    for num in nums:
        temp.append(int(num))
    lists.append(temp)


for l in lists:
    dif = [l[i]-l[i+1] for i in range(len(l)-1)]
    diffs.append(dif)

for dif in diffs:
    if not (all(d > 0 for d in dif) or all(d < 0 for d in dif)):
        unsafe.append(dif)
    elif all(abs(d) >= 1 for d in dif) and all(abs(d) <= 3 for d in dif):
        safe.append(dif)
    else:
        unsafe.append(dif)

print(len(safe))
