class Solution(object):
    def adder(self, a, b):
        cin, sum_out = 0, 0
        for i in range(32):
            a_bit = (a & (1 << i)) >> i
            b_bit = (b & (1 << i)) >> i
            s = b_bit ^ a_bit ^ cin
            sum_out |= (s << i)
            cin = ((a_bit | b_bit | cin) & ~s) | (cin & a_bit & b_bit)
        return sum_out

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s = self.adder(a, b)

        # Annoyances due to Python not having a fixed integer bit length
        if s & 0x80000000:
            return -self.adder(~(s & 0x7FFFFFFF) & 0x7FFFFFFF, 1)
        return s
