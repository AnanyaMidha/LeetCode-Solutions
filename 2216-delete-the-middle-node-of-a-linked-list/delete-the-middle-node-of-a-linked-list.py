# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None
        prev = None
        slow, fast = head, head
        

        while fast and fast.next:
            
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next

        return head
        