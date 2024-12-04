# filename = "test_input.txt"
filename = "input.txt"

with open(filename) as f:
    lines = f.readlines()

data = []

for line in lines:
    data.append(list(line.strip()))

rows = len(data)
cols = len(data[0])

matches = 0

for i in range(rows-2):
    for j in range(cols-2):
        if data[i][j] == "M" and data[i][j+2] == "S" and data[i+1][j+1] == "A" and data[i+2][j] == "M" and data[i+2][j+2] == "S":
            matches += 1
        elif data[i][j] == "S" and data[i][j+2] == "M" and data[i+1][j+1] == "A" and data[i+2][j] == "S" and data[i+2][j+2] == "M":
            matches += 1
        elif data[i][j] == "M" and data[i][j+2] == "M" and data[i+1][j+1] == "A" and data[i+2][j] == "S" and data[i+2][j+2] == "S":
            matches += 1
        elif data[i][j] == "S" and data[i][j+2] == "S" and data[i+1][j+1] == "A" and data[i+2][j] == "M" and data[i+2][j+2] == "M":
            matches += 1


print(matches)
