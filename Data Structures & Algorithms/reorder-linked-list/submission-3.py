# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None # cut off the 2 half

        # reverse the 2nd list
        prev = None
        while second:
            rest = second.next
            second.next = prev
            prev = second
            second = rest

        # Merge the 2 list
        first = head
        second = prev

        while second:
            rest1, rest2 = first.next, second.next
            first.next = second
            second.next = rest1
            first, second = rest1, rest2