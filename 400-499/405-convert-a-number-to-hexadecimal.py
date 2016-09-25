class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        elif num < 0:
            num += 2**32
        hex_chars, res = '0123456789abcdef', ''
        while num:
            res = hex_chars[num % 16] + res
            num /= 16
        return res