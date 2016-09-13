class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minStack) > 0:
            if x < self.minStack[-1][0]:
                self.minStack.append([x, 1])
            elif x == self.minStack[-1][0]:
                self.minStack[-1][1] += 1
        else:
            self.minStack.append([x, 1])

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
            if self.minStack[-1][1] <= 0:
                self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1][0]

# Explanation:
#   Obviously, really quite easy to implement a stack in Python with the built
#   funcitons. 'Tricky' part with this problem is the getMin aspect. Naive
#   solution would be to do some kind of sort, but this is unnecessary.
#
#   This solution uses an O(n) space secondary stack to hold the min values.
#   It does a bit of 'compression' by holding the min value and the count of
#   the times that min value has been inserted.
#
#   Note that if a value has been inserted and is not the current minimum value
#   it can never be the minimum value. So, if I insert [5, 6, 1], 5 is the
#   initial minimum value, and 1 becomes the new minimum value once it has been
#   inserted. However, because it's a stack, 6 can never be the minimum value
#   of the stack.
#
#   Using this property, the secondary stack approach is quite intuitive.
#
#   There is a constant space approach as well, which is far less intuitive:
#   Always hold the difference between the minimum value and the inserted value
#   in the stack. So, inserting [5,6,1] would yield a stack of [0,1,-4]. Every
#   time you find a new minimum, set a minimum counter to be that new minimum.
#   Every time you need to do a pop or top, return self.nums[-1] + self.min
#   If you encounter a negative number in pop/top, set the new minimum to be
#   min - top to reconstruct the old minimum. (i.e., 1 - -4 reconstructs 5)
