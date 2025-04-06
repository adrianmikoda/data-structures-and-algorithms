# leetcode problem no. 102

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        answer = []
        q = deque([(root, 0)])

        while q:
            current = q.popleft()
            u = current[0]
            d = current[1]

            if len(answer) == d:
                answer.append([])
            answer[d].append(u.val)
            if u.left is not None:
                q.append((u.left, d+1))
            if u.right is not None:
                q.append((u.right, d+1))
        return answer
