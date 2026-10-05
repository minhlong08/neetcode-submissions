# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None # cut of the 2 half

        # reverse the 2nd list
        prev = None
        while second:
            rest = second.next
            second.next = prev
            prev = second
            second = rest

        first = head
        second = prev

        while second:
            rest1 = first.next
            rest2 = second.next

            first.next = second
            second.next = rest1

            first, second = rest1, rest2