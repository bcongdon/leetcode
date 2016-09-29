from random import random


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        tail, c_max, c_val = self.head, 0, None
        while tail:
            r = random()
            if r > c_max:
                c_val, c_max = tail.val, r
            tail = tail.next
        return c_val
