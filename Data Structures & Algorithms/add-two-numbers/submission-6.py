# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new list and have curr point to it and then add the values we want to this list with ListNode()
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
            # dummy -> 7 creates dummy -> 7 -> 3 adds the new node to the list
            curr.next = ListNode(new_val)

            # Move pointers dummy -> 7 -> 3 -> pointing to the next one
            curr = curr.next
            # Moves l1 to next item in list
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

        