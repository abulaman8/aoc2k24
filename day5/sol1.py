filename = "test_input.txt"
# filename = "input.txt"


rules = []
data = []

pre_reqs = {}

with open(filename, "r") as f:
    lines = f.readlines()

data_index = 0

for i in range(len(lines)):
    line = lines[i].strip()
    if line == "":
        data_index = i + 1
        break
    rules.append(line)
    nums = line.split("|")
    pre_reqs[int(nums[1])] = pre_reqs.get(
        int(nums[1]), []) + [int(nums[0])]


for i in range(data_index, len(lines)):
    data.append(lines[i].strip())


updates = []
for dp in data:
    temp = []
    nums = dp.split(",")
    for n in nums:
        temp.append(int(n))
    updates.append(temp)

correct_updates = []
incorrect_updates = []


def has_pre_reqs(num, seen, update):
    num_pre_reqs = pre_reqs.get(num, [])
    for pre_req in num_pre_reqs:
        if pre_req not in seen and pre_req in update:
            return False
    return True


for update in updates:
    seen = []
    for num in update:
        pre_req_check = has_pre_reqs(num, seen, update)
        if not pre_req_check:
            incorrect_updates.append(update)
            break
        seen.append(num)
    else:
        correct_updates.append(update)
sum = 0


for update in correct_updates:
    middle = update[len(update) // 2]
    sum += middle

__import__('pprint').pprint(pre_reqs)

print(sum)
