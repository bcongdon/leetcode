# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow, fast = head, head
        # Reverse list while finding mid point
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # Move forward if odd length list
        if fast:
            slow = slow.next
        # Compare reversed first half with normal second half
        while rev and slow and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        # Is palindrome if reversed list has been expended
        return not rev
