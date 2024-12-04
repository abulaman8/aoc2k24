import re

# filename = "test_input.txt"
filename = "input.txt"

with open(filename) as f:
    lines = f.readlines()

data = []

for line in lines:
    data.append(list(line.strip()))

rows = len(data)
cols = len(data[0])

row_matches = 0
col_matches = 0
tl_br_diag_matches = 0
tr_bl_diag_matches = 0

for line in data:
    temp, matches = "".join(line), []
    xmas_matches = re.findall(r"XMAS", temp)
    samx_matches = re.findall(r"SAMX", temp)
    matches = xmas_matches + samx_matches
    row_matches += len(matches)

for i in range(rows):
    temp, matches = "", []
    for j in range(cols):
        temp += data[j][i]
        xmas_matches = re.findall(r"XMAS", temp)
        samx_matches = re.findall(r"SAMX", temp)
        matches = xmas_matches + samx_matches
    col_matches += len(matches)


for k in range(cols):
    temp, matches = "", []
    for i, j in zip(range(k + 1), range(k, -1, -1)):
        temp += data[i][j]
        xmas_matches = re.findall(r"XMAS", temp)
        samx_matches = re.findall(r"SAMX", temp)
        matches = xmas_matches + samx_matches

    tl_br_diag_matches += len(matches)


for k in range(1, rows):
    temp, matches = "", []
    for i, j in zip(range(k, rows), range(cols - 1, k - 2, -1)):
        temp += data[i][j]
        xmas_matches = re.findall(r"XMAS", temp)
        samx_matches = re.findall(r"SAMX", temp)
        matches = xmas_matches + samx_matches
    tl_br_diag_matches += len(matches)


for k in range(cols - 1, -1, -1):
    temp, matches = "", []
    for i, j in zip(range(rows), range(k, cols)):
        temp += data[i][j]
        xmas_matches = re.findall(r"XMAS", temp)
        samx_matches = re.findall(r"SAMX", temp)
        matches = xmas_matches + samx_matches
    tr_bl_diag_matches += len(matches)


for k in range(1, rows):
    temp, matches = "", []
    for i, j in zip(range(k, rows), range(cols)):
        temp += data[i][j]
        xmas_matches = re.findall(r"XMAS", temp)
        samx_matches = re.findall(r"SAMX", temp)
        matches = xmas_matches + samx_matches
    tr_bl_diag_matches += len(matches)

print(row_matches)
print(col_matches)
print(tl_br_diag_matches)
print(tr_bl_diag_matches)

print(row_matches + col_matches + tl_br_diag_matches + tr_bl_diag_matches)
