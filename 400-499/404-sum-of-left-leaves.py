# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        val = 0
        val += self.sumOfLeftLeaves(root.left)
        val += self.sumOfLeftLeaves(root.right)
        if root.left and not (root.left.left or root.left.right):
            val += root.left.val
        return val
