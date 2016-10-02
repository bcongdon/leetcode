class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
        elif root.right:
            return 1 + self.minDepth(root.right)
        elif root.left:
            return 1 + self.minDepth(root.left)
        else:
            return 1
