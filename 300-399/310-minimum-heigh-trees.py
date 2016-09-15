class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        mht_nodes = []

        # Special cases
        if n <= 0:
            return mht_nodes
        elif n == 1 and not len(edges):
            return [0]

        # Construct graph adjacency list
        adj_list = [[] for _ in xrange(n)]
        for e in edges:
            frm, to = e
            adj_list[frm].append(to)
            adj_list[to].append(frm)

        # Find leaf nodes
        leaves = [node for node, x in enumerate(adj_list) if len(x) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf][0]
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves

# Explanation
# Given an undirected tree, we need to find the roots of the tree with the
# minimum possible height. Consider the special case where the undirected
# graph is simply a path. Then the MHT roots will be the middle or middle
# two nodes of the path (depending on n % 2). The approach would to be to
# traverse from the leaves to the center.
#
# A similar approach works in the general case of an undirected graph. Simply
# construct the graph using an adjacency list constructed from the edge list
# and find the list of graph leaf nodes. Check the adjacency lists for each
# leaf and delete the leaf. If that neighbor now is a leaf (only 1 adjacent)
# then add it to the leaves list. Once we only have 1 or 2 nodes left in the
# graph, we have found the roots of the MHT.

# Runtime - O(n)
# This is a graph traversal, and we aren't doing anything more expensive.
# Constructing the adjacency list will be O(n), the initial search for finding
# leaf nodes is O(n), and the number of total leaves is O(n), so the total
# runtime will be O(n).

# Space Complexity
# The total number of edges in an undirected tree is n-1, but we store each
# edge twice, giving 2(n-1). However, space utilization is still O(n).
