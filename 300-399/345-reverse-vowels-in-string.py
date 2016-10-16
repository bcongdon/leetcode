class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lo, hi = 0, len(s) - 1
        vowels = 'aeiouAEIOU'
        chars = [''] * len(s)
        while lo <= hi:
            if s[lo] not in vowels:
                chars[lo] = s[lo]
                lo += 1
                continue
            if s[hi] not in vowels:
                chars[hi] = s[hi]
                hi -= 1
                continue
            chars[lo], chars[hi] = s[hi], s[lo]
            hi -= 1
            lo += 1
        return ''.join(chars)
