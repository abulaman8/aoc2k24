filename = "input.txt"

with open(filename, "r") as f:
    data = f.read().splitlines()

lists = []
safe = []
unsafe = []
for line in data:
    nums = line.split()
    temp = [int(num) for num in nums]
    lists.append(temp)


def is_safe(l):
    ascending = l[0] < l[1]
    descending = l[0] > l[1]
    for i in range(len(l)-1):
        if ascending and l[i] > l[i+1]:
            return False, i
        elif descending and l[i] < l[i+1]:
            return False, i
        if abs(l[i] - l[i+1]) < 1 or abs(l[i] - l[i+1]) > 3:
            return False, i

    return True, 0


for l in lists:
    offense = 0
    b, i = is_safe(l)
    if b:
        safe.append(l)
    else:
        l2 = [num for num in l]
        l3 = [num for num in l]
        l4 = [num for num in l]
        l2.pop(i)
        l3.pop(i+1)
        l4.pop(i-1)
        b2, i2 = is_safe(l2)
        b3, i3 = is_safe(l3)
        b4, i4 = is_safe(l4)
        if b2 or b3 or b4:
            safe.append(l)
        else:
            unsafe.append(l)

print(len(safe))
# __import__('pprint').pprint(safe)
