class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        # Remove trailing whitespace
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            return 0
        for j in xrange(i, -1, -1):
            if s[j] == ' ':
                return i - j
        return i + 1
