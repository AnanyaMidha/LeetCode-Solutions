# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        curr_node = head
        s = []

        while curr_node is not None:
            s.append(curr_node.val)
            curr_node = curr_node.next
        while head is not None:
            c = s.pop()
            if head.val != c:
                return False
            head = head.next
        return True
        