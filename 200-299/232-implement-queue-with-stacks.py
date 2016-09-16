class Queue(object):
    def swap(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack = list()
        self.outStack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.outStack:
            self.swap()
        if self.outStack:
            self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.outStack:
            self.swap()
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.inStack and not self.outStack

# Explanation
# Have one stack handle inputs and the other handle outputs. When you need
# to output, take all of the elements in the 'in' stack and put them in the
# 'out' stack. The result is queue behavior.

# Runtime

# Space Complexity - O(n)
