# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):
    def isValidBST_(self, root, min_, max_):
        if not root:
            return True
        if root.left and root.left.val > root.val:
            return False
        if root.right and root.right.val < root.val:
            return False
        if root.val <= min_ or root.val >= max_:
            return False
        return (self.isValidBST_(root.right, root.val, max_) and
                self.isValidBST_(root.left, min_, root.val))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBST_(root, -sys.maxint - 1, sys.maxint)
