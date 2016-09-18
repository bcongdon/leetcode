from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        levels = []
        queue = deque([root])
        while len(queue) > 0:
            num_nodes_in_level = len(queue)
            curr_level = []
            while num_nodes_in_level > 0:
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left and curr_node.left.val != 'null':
                    queue.append(curr_node.left)
                if curr_node.right and curr_node.right.val != 'null':
                    queue.append(curr_node.right)
                num_nodes_in_level -= 1
            levels.append(curr_level)
        return levels

# Explanation
# See #199

# Runtime - O(n)

# Space Complexity - O(n)
