class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for x in xrange(0, len(s)/2):
            s[x], s[len(s) - x - 1] = s[len(s) - x - 1], s[x]
        return ''.join(s)
