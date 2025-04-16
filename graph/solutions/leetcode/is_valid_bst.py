# leetcode problem no. 98

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def isValidBST(self, root):
        self.answer = True
        self.validate(root)
        return self.answer

    def validate(self, current):
        if not self.answer:
            return [-1, -1]
        ans = [current.val, current.val]

        if current.left is None and current.right is None:
            return ans

        if current.left is not None:
            ans_left = self.validate(current.left)
            if ans_left[0] >= current.val or ans_left[1] >= current.val:
                self.answer = False
            ans[0] = ans_left[0] if ans_left[0] < ans[0] else ans[0]
            ans[1] = ans_left[1] if ans_left[1] > ans[1] else ans[1]

        if current.right is not None:
            ans_right = self.validate(current.right)
            if ans_right[0] <= current.val or ans_right[1] <= current.val:
                self.answer = False
            ans[0] = ans_right[0] if ans_right[0] < ans[0] else ans[0]
            ans[1] = ans_right[1] if ans_right[1] > ans[1] else ans[1]

        return ans
