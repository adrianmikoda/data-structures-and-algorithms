# leetcode problem no. 230

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.counter = 1
        self.answer = -1

        def DFS(current):

            if current.left is not None:
                DFS(current.left)
            if self.counter == k:
                self.answer = current.val
            self.counter += 1

            if current.right is not None:
                DFS(current.right)

        DFS(root)
        return self.answer
