# leetcode problem no. 144

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, current):
        self.answer.append(current.val)
        if current.left is not None:
            self.dfs(current.left)
        if current.right is not None:
            self.dfs(current.right)

    def preorderTraversal(self, root):
        if root is None:
            return []
        self.answer = []
        self.dfs(root)
        return self.answer
