"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        newHead = Node(head.val)
        
        # pointer to the original head
        cur1 = head
        # pointer to the new head
        cur2 = newHead
        
        # hashmap mapping original node to new Node
        hashMap = {}
        hashMap[head] = newHead
        while cur1.next:
            cur2.next = Node(cur1.next.val)
            cur1 = cur1.next
            cur2 = cur2.next

            hashMap[cur1] = cur2

        # random pointer
        cur1 = head
        cur2 = newHead
        while cur1:
            randomNode = cur1.random
            if randomNode != None:
                cur2.random = hashMap[randomNode]

            cur1 = cur1.next
            cur2 = cur2.next

        return newHead

