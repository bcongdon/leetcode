# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def traverse_(self, root):
        paths = []
        if not (root.left or root.right):
            return [[root.val]]
        if root.right:
            paths.extend([x + [root.val] for x in self.traverse_(root.right)])
        if root.left:
            paths.extend([x + [root.val] for x in self.traverse_(root.left)])
        return paths

    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        paths = self.traverse_(root)
        return ['->'.join(reversed([str(i) for i in x])) for x in paths]
