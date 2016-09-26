# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        sorted_head, sorted_tail = None, None
        if l1.val < l2.val:
            sorted_head, sorted_tail = l1, l1
            l1 = l1.next
        else:
            sorted_head, sorted_tail = l2, l2
            l2 = l2.next
        while l1 and l2:
            if l1.val < l2.val:
                sorted_tail.next, l1 = l1, l1.next
                sorted_tail = sorted_tail.next
            else:
                sorted_tail.next, l2 = l2, l2.next
                sorted_tail = sorted_tail.next
        while l1:
            sorted_tail.next, l1 = l1, l1.next
            sorted_tail = sorted_tail.next
        while l2:
            sorted_tail.next, l2 = l2, l2.next
            sorted_tail = sorted_tail.next
        return sorted_head
