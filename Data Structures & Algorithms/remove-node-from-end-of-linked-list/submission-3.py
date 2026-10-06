# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Compute the lenght of the linked list
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        # Remove the nth node
        target = length - n
        prev = None
        cur = head
        count = 0
        while cur and count != target:
            prev = cur
            cur = cur.next
            count += 1

        if prev:
            prev.next = cur.next
        else: # removing the 1st node of the list
            head = cur.next

        return head

        