from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        last_nodes, queue = [], deque([root])
        while len(queue) > 0:
            num_nodes_in_level = len(queue)
            while num_nodes_in_level > 0:
                curr_node = queue.popleft()
                if num_nodes_in_level == 1:
                    last_nodes.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                num_nodes_in_level -= 1
        return last_nodes

# Explanation
# Do a DFS traversal on the tree to get a level-order traversal. Use the
# 'num_nodes_in_level' variable to know when you've hit the edge of a level.

# Runtime - O(n)
# This is a traversal, so it's done in O(n) time. Since we only need the
# right most element in each leve, I suspect there may be a sublinear-on-
# average approach to this problem.

# Space Complexity - O(n)
