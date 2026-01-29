# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #this is basically for the best case, jo bohot kam hi hota hai, but hota hai
        if not head or not head.next:
            return head
        
        # 1. Split the LL into two equal halves
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None #break the list

        # 2. Sort both the halves.

        left = self.sortList(left)
        right = self.sortList(right)

        # 3. Merge both the list

        return self.merge(left, right)

        #find the middle of the list using slow and fast pointers, the best approach, easy peezy
    def getMid(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # Merge two sorted linked lists

    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next