class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_idx, b_idx = len(a) - 1, len(b) - 1
        sum_str, carry_in = '', 0
        while a_idx >= 0 or b_idx >= 0:
            curr_sum = carry_in
            if a_idx >= 0:
                curr_sum += 1 if a[a_idx] == '1' else 0
            if b_idx >= 0:
                curr_sum += 1 if b[b_idx] == '1' else 0
            sum_str += '0' if curr_sum in [0, 2] else '1'
            carry_in = 1 if curr_sum > 1 else 0
            a_idx, b_idx = a_idx - 1, b_idx - 1
        sum_str += '1' if carry_in else ''
        return sum_str[::-1]

# Explanation
# Implementation of a simple add + keep track of carr_out binary adder

# Runtime - O(max(a + b))
# Where a and b are the lengths of binary strings a and b

# Space Complexity - O(max(a + b))
# Where a and b are the lengths of binary strings a and b
