# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        
    # Traverse the list
        while fast is not None and fast.next is not None:

        # Move slow by one step
            slow = slow.next

        # Move fast by two steps
            fast = fast.next.next

        # Detect loop
            if slow == fast:
            
            # Move slow to head
            # keep fast at meeting point
                slow = head

            # Move both one step at a time until they meet
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

            # Return the meeting node's data
                return slow

        return None

