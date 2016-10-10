from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx, rep = OrderedDict(), {}
        for i, c in enumerate(s):
            if c in idx:
                rep[c] = True
            else:
                idx[c] = i
        for k, v in idx.items():
            if k not in rep:
                return v
        else:
            return -1
