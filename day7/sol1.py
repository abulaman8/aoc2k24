from typing import List

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


class Node:
    def __init__(self,
                 value: int,
                 parent: "Node | None" = None,
                 left: "Node | None" = None,
                 right: "Node | None" = None
                 ):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class OpTree:
    def __init__(self, nums: List[int]):
        self.root = Node(nums[0])
        self.construct_tree(nums[1:], self.root)

    def construct_tree(self, nums: List[int], parent: Node):
        if nums:
            temp = nums[0]
            left = Node(temp * parent.value, parent)
            right = Node(temp + parent.value, parent)
            parent.left = left
            parent.right = right
            self.construct_tree(nums[1:], left)
            self.construct_tree(nums[1:], right)

    def get_leaves(self):
        leaves = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not node.left and not node.right:
                leaves.append(node)
        return leaves

    def print_tree(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == "__main__":

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
    print(f"{len(invalid_equations)}/{len(data)} invalid equations")
