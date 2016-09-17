from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        map(lambda s: anagrams[''.join(sorted(s))].append(s), strs)
        return anagrams.values()

# Explanation
# Super straight-forward, I just liked the elegance of this solution.

# Runtime - O(n*aloga) where a is the longest string in s
# Need to do n sorts, which each take aloga time.
