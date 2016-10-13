class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo, hi = 0, len(s) - 1
        s = str(s.lower())
        while lo < hi:
            if not s[lo].isalnum():
                lo += 1
                continue
            if not s[hi].isalnum():
                hi -= 1
                continue
            if s[lo] != s[hi]:
                return False
            else:
                lo += 1
                hi -= 1
        else:
            return True
