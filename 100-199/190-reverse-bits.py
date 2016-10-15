class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            bit = (n & (1 << i)) >> i
            new_place = 32 - i - 1
            out |= (bit << new_place)
        return out
