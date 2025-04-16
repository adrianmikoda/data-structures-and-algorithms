# leetcode problem no. 404

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def check(self, current):
        if current is not None:
            if current.left is not None:
                if current.left.left is None and current.left.right is None:
                    self.answer += current.left.val
                self.check(current.left)
            if current.right is not None:
                self.check(current.right)

    def sumOfLeftLeaves(self, root):
        self.answer = 0
        self.check(root)
        return self.answer
