# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        #count the number of elemnets in the linked list
        curr, length = head, 0
        while curr:
            length += 1
            curr = curr.next
        #for actual number of rotations
        k %= length
        if k == 0:
            return head
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        new_head = slow.next
        slow.next = None  
        fast.next = head  
      
        return new_head

