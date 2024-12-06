# filename = "test_input.txt"
filename = "input.txt"


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
corrected_updates = []


def has_pre_reqs(num, seen, update):
    num_pre_reqs = pre_reqs.get(num, [])
    for pre_req in num_pre_reqs:
        if pre_req not in seen and pre_req in update:
            return False, update.index(pre_req)
    return True, 0


def farthest_pre_req(num, seen, update):
    largest_index = 0
    num_pre_reqs = pre_reqs.get(num, [])
    for pre_req in num_pre_reqs:
        if pre_req not in seen and pre_req in update:
            i = update.index(pre_req)
            if i >= largest_index:
                largest_index = i
    if largest_index == 0:
        return False, 0
    return True, largest_index


for update in updates:
    seen = []
    for num in update:
        pre_req_check, _ = has_pre_reqs(num, seen, update)
        if not pre_req_check:
            incorrect_updates.append(update)
            break
        seen.append(num)
    else:
        correct_updates.append(update)
sum = 0


def fix_incorrect_update(update):
    seen = []
    for i in range(len(update)):
        incorrect, index = farthest_pre_req(update[i], seen, update)
        if incorrect:
            temp = update.pop(i)
            update.insert(index+1, temp)
        seen.append(update[i])
    else:
        corrected_updates.append(update)


def is_correct(update):
    seen = []
    for num in update:
        pre_req_check, _ = has_pre_reqs(num, seen, update)
        if not pre_req_check:
            return False
        seen.append(num)
    return True


for update in incorrect_updates:
    while not is_correct(update):
        fix_incorrect_update(update)

for update in corrected_updates:
    middle = update[len(update) // 2]
    sum += middle

# __import__('pprint').pprint(pre_reqs)
#
# for update in corrected_updates:
#     print(update)

print(sum)
sanity_check = []


for update in corrected_updates:
    sanity_check.append(is_correct(update))

print(sanity_check.count(True))
print(sanity_check.count(False))
