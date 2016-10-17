class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        tot = 0
        s = s.upper()
        for idx, i in enumerate(s):
            # Subtractive Notation
            if idx + 1 < len(s) and numerals[s[idx + 1]] > numerals[i]:
                tot -= numerals[i]
            # Additive Notation
            else:
                tot += numerals[i]
        return tot
