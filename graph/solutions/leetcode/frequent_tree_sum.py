# leetcode problem no.508

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def subtreesum(self, current):
        sum = 0
        if current is not None:
            sum += current.val
            sum += self.subtreesum(current.left)
            sum += self.subtreesum(current.right)

            self.d[sum] += 1
        return sum

    def findFrequentTreeSum(self, root):
        self.d = defaultdict(int)
        self.subtreesum(root)
        answer = []
        max_count = max(self.d.values())
        for i in self.d.keys():
            if self.d[i] == max_count:
                answer.append(i)
        return answer
