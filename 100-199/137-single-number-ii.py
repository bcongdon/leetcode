class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        # Iterate through integer bits
        for x in xrange(32):
            curr_b = 0
            # Sum up all the bits
            for n in nums:
                if n & (1 << x):
                    curr_b += 1
            # Number of bits not divisible by 3, so part of the solution
            if curr_b % 3 != 0:
                # Not at MSB
                if x != 31:
                    out += (1 << x)
                # At MSB and out is negative
                elif curr_b % 3 == 1:
                    out -= (1 << 31)
        return out

# Explanation
# Similar bit manipulation approach to #136, but this time we cannot just xor
# the whole bit sequence. We have to count the number of bits in each place,
# and see if the number of bits is not divisible by 3 - indicating a bit in the
# solution.
#
# This is slightly complicated by needing to deal with negative (signed)
# integers. In this case, 