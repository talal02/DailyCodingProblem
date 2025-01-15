"""
Easy

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

class Node:
  def __init__(self, value: int, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def first_solution(node: Node) -> int:
  count = 0
  if not node:
    return 0
  if not node.left and not node.right:
    return 1
  if node.left and node.right:
    if node.value == node.left.value and node.value == node.right.value:
      count += 1
  count += first_solution(node.left) + first_solution(node.right)
  return count

"""
Explanation of first_solution:
- We are counting the number of unival subtrees by checking if the current node is a unival subtree.
- We are then recursively calling the function on the left and right children of the current node.
- We are adding the count of unival subtrees from the left and right children to the count of unival subtrees from the current node.
- We are returning the total count of unival subtrees.
"""

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(first_solution(root)) # 5