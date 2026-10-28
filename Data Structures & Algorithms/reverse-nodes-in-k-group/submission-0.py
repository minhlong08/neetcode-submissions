# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        previousGroupTail = dummy

        # Count the length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        groups = length // k

        for _ in range(groups):
            groupHead = previousGroupTail.next
            cur = groupHead
            prev = None

            # reverse the group
            for _ in range(k):
                rest = cur.next
                cur.next = prev
                prev = cur
                cur = rest

            # connect the group
            # prev is now the head of the reverse group
            previousGroupTail.next = prev
            # cur is now storing rest of the list
            # groupHead which is the old head of the group after reverse is the tail
            groupHead.next = cur

            # update the previousGroupTail
            previousGroupTail = groupHead

        return dummy.next

