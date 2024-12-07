from typing import List
from sol1 import OpTree

# filename = "test_input.txt"
filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()

data = []
for line in lines:
    parts = line.strip().split(":")
    value = int(parts[0])
    nums = parts[1].strip().split(" ")
    nums = [int(x) for x in nums]
    data.append((value, nums))

valid_equations = []
valid_values = []
invalid_equations = []


class NodePlus:
    def __init__(self,
                 value: int,
                 parent: "NodePlus | None" = None,
                 left: "NodePlus | None" = None,
                 middle: "NodePlus | None" = None,
                 right: "NodePlus | None" = None
                 ):
        self.value = value
        self.parent = parent
        self.left = left
        self.middle = middle
        self.right = right

    def __repr__(self):
        return str(self.value)


class OpTreePlus:
    def __init__(self, nums: List[int]):
        self.root = NodePlus(nums[0])
        self.construct_tree(nums[1:], self.root)

    def construct_tree(self, nums: List[int], parent: NodePlus):
        if nums:
            temp = nums[0]
            left = NodePlus(temp * parent.value, parent)
            middle = NodePlus(int(str(parent.value) + str(temp)), parent)
            right = NodePlus(temp + parent.value, parent)
            parent.left = left
            parent.middle = middle
            parent.right = right
            self.construct_tree(nums[1:], left)
            self.construct_tree(nums[1:], middle)
            self.construct_tree(nums[1:], right)

    def get_leaves(self):
        leaves = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.middle:
                queue.append(node.middle)
            if node.right:
                queue.append(node.right)
            if not node.left and not node.right and not node.middle:
                leaves.append(node)
        return leaves


for equation in data:
    op_tree = OpTree(equation[1])
    leaves = op_tree.get_leaves()
    leaves = [x.value for x in leaves]
    val = equation[0]
    if val in leaves:
        valid_equations.append(equation)
        valid_values.append(val)
    else:
        invalid_equations.append(equation)

print(sum(valid_values))
i = 1

for equation in invalid_equations:
    print(equation)
    op_tree = OpTreePlus(equation[1])
    leaves = op_tree.get_leaves()
    leaves = [x.value for x in leaves]
    val = equation[0]
    if val in leaves:
        valid_equations.append(equation)
        valid_values.append(val)
    print(f"{i}/{len(invalid_equations)} processed in OpTreePlus")
    i += 1

print("\n----------------------------------")
print(sum(valid_values))
