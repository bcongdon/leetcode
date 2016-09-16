class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {'(': ')', '{': '}', '[': ']'}
        stack = list()
        for c in s:
            # Open paren
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0 or matches[stack.pop()] != c:
                    return False
        else:
            return len(stack) == 0

# Explanation
# Classic stack-based solution to matching parenthesis. Make sure that when
# you have a closing delimeter, the top of the stack has the appropriately
# matching opening delimeter.

# Runtime - O(n)
# Needs to iterate through the string exactly 1 time

# Space Complexity - O(n)
# The stack could have up to n/2 items in it for valid strings, or n items in
# it for invalid strings. These are both O(n)
