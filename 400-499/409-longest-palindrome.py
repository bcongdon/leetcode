class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        longest = 0
        odd_found = False
        for _, v in d.items():
            if v % 2 == 1:
                odd_found = True
                longest += v - 1
            else:
                longest += v
        if odd_found:
            longest += 1
        return longest
