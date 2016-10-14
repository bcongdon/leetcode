class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.symmetric(root, root)

    def symmetric(self, a, b):
        if a and b:
            return (a.val == b.val and self.symmetric(a.left, b.right) and
                    self.symmetric(a.right, b.left))
        else:
            return a == b
