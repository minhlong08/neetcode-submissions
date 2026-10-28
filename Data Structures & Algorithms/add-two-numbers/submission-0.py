# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = cur = ListNode()
        # keep track of the carry
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            newDigit = digit1 + digit2 + carry
            if newDigit > 9:
                carry = newDigit // 10
                newDigit = newDigit % 10
            else:
                carry = 0
            
            cur.next = ListNode(newDigit)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummyNode.next
        