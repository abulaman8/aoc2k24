# filename = "test_input.txt"
filename = "input.txt"


with open(filename, "r") as f:
    lines = f.readlines()

line = lines[0].strip().split()

nums = [int(x) for x in line]


counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1

for i in range(75):
    temp = {}
    keys = list(counts.keys())
    keys = [key for key in keys if counts[key] > 0]
    for key in keys:
        skey = str(key)
        len_skey = len(skey)
        if key == 0:
            temp[1] = counts[key] + temp.get(1, 0)
            counts[key] = 0
        elif len_skey % 2 == 0:
            l = len_skey
            first_half = int(skey[:l//2])
            second_half = int(skey[l//2:])

            temp[first_half] = temp.get(first_half, 0) + counts[key]
            temp[second_half] = temp.get(second_half, 0) + counts[key]
            counts[key] = 0
        else:
            temp[key * 2024] = temp.get(key * 2024, 0) + counts[key]
            counts[key] = 0
    for k in temp.keys():
        counts[k] = temp[k] + counts.get(k, 0)

sum = 0

for k in counts:
    sum += counts[k]

print(sum)
