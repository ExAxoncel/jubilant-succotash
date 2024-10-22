# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        len = 0
        curr = head
        while curr:
            len += 1
            curr = curr.next

        if n == len:
            return head.next

        curr = head
        for _ in range(len - n - 1):
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

        return head
