# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while(carry or l1 or l2):
            if l1:
                carry +=l1.val
                l1 = l1.next
            if l2:
                carry +=l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry = carry // 10
            curr = curr.next
        return dummy.next
        