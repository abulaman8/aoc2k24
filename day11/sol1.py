# filename = "test_input.txt"
filename = "input.txt"


with open(filename, "r") as f:
    lines = f.readlines()

line = lines[0].strip().split()

nums = [int(x) for x in line]

for _ in range(25):
    temp = []
    for num in nums:
        if num == 0:
            temp.append(1)
        elif len(str(num)) % 2 == 0:
            l = len(str(num))
            first_half = str(num)[:l//2]
            second_half = str(num)[l//2:]
            temp.append(int(first_half))
            temp.append(int(second_half))
        else:
            temp.append(num * 2024)

    nums = temp

print(len(nums))
