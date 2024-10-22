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
        length = 0
        current_node = head
        while current_node:
            length += 1
            current_node = current_node.next

        if n == length:
            return head.next

        current_node = head
        for _ in range(length - n - 1):
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

        return head
