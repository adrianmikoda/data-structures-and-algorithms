# leetcode problem no. 104

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, current, depth):
        if current is None:
            self.answer = depth-1 if depth-1 > self.answer else self.answer
            return
        self.dfs(current.left, depth+1)
        self.dfs(current.right, depth+1)

    def maxDepth(self, root):
        self.answer = 0
        self.dfs(root, 1)
        return self.answer
