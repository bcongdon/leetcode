# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverse_(self, head, prev):
        ret = None
        if not head.next:
            ret = head
        else:
            ret = self.reverse_(head.next, head)
        head.next = prev
        return ret

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        return self.reverse_(head, None)
