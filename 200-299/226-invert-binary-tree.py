class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.invertTree(root.right)
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        return root

# Explanation
# Pretty trivial, but I thought Max Howell's tweet was funny, so here
# ya go.

# Runtime - O(n)
# Pretty clearly a traversal, so runtime will be O(n). We have to touch each
# node in the tree exactly one time.

# Space Complexity - O(n)
# Using recursion, so at worst case we could have O(n) frames on the stack.
# This could be done iteratively in O(1) space in the manner described below:

from collections import deque


def invertTreeIterative(self, root):
    to_be_swapped = deque([root])
    while len(to_be_swapped) > 0:
        node = to_be_swapped.popleft()
        if not node:
            continue
        to_be_swapped.extend([node.left, node.right])
        node.left, node.right = node.right, node.left
    return root
