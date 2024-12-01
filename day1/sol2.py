from collections import Counter

filename = "input.txt"
with open(filename, "r") as f:
    data = f.read().splitlines()

l1 = []
l2 = []

sim_scores = []

for i in data:
    nums = i.split()
    l1.append(int(nums[0]))
    l2.append(int(nums[1]))

l2_counter = Counter(l2)

for i in l1:
    sim_scores.append(i * l2_counter[i])

print(sum(sim_scores))
