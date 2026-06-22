# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle point using fast and slow pointer
        # The half will be slow
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        l1 = head
        l2 = slow

        if l1 == l2:
            return

        # Cut up l1 from l2
        cur1 = l1
        while cur1 and cur1.next != l2:
            cur1 = cur1.next

        cur1.next = None

        # Reverse l2
        prev = None
        cur = l2
        while cur:
            rest = cur.next
            cur.next = prev
            prev = cur
            cur = rest

        l2 = prev

        # Merge l1 and l2 to get the reorder list
        dummy = node = ListNode()
        flag = 0
        while l1 and l2:
            if flag % 2 == 0:
                node.next = l1
                l1 = l1.next
                flag += 1
            else:
                node.next = l2
                l2 = l2.next
                flag += 1
            node = node.next
        
        node.next = l1 or l2

        head = dummy.next

        