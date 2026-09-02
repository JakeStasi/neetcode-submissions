# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use 2 Pointer Approach, fast and slow pointer
        slow = head
        fast = head
        # We check if fast is at the end of the list by checking if it exists, if its at the end then we know our slow pointer is at the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

        