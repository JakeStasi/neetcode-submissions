# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        curr = dummy

        while l1 or l2 or carry:
            # Set the values from the first list and the second list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the new value
            new_val = val1 + val2 + carry
            # Get the carry value from the new number ie 18//10 = 1
            carry = new_val // 10
            # Get the value we are going to add to the list 18 % 10 = 8
            new_val = new_val % 10
            curr.next = ListNode(new_val)

            # Move pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

        