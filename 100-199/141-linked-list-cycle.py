class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        else:
            return False
