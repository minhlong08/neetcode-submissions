class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value

        # doubly linked list
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        # cache map key to node
        self.cache = {}

        # capacity
        self.cap = capacity

        # left pointer points to the lru
        # right pointer points to most recent use
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # remove a node from the double linked list
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev


    def insert(self, node):
        # insert a node to the right (most recent)
        prev, nxt = self.right.prev, self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # retrieve the node from hashmap
        curNode = self.cache[key]
        # update this node to most recently use
        self.remove(curNode)
        self.insert(curNode)

        return curNode.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap:
            lruNode = self.left.next
            self.remove(lruNode)
            del self.cache[lruNode.key]
