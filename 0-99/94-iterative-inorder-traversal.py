# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal = []
        prevNodes, curr = [], root
        if not root:
            return []
        while True:
            if not curr and not prevNodes:
                break
            while curr:
                prevNodes.append(curr)
                curr = curr.left
            if prevNodes:
                curr = prevNodes.pop()
            traversal.append(curr.val)
            curr = curr.right
        return traversal

# Explanation
# Use a stack to remember previous nodes in the traversal. Add left nodes
# while possible, then pop the stack, touch that node, and move to that node's
# right child. Continue until the stack is empty and curr node is None.

# Runtime - O(n)

# Space Complexity - O(n)
