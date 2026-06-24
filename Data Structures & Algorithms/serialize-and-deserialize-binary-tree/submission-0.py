# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = ""
        queue = collections.deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()

            if node:
                res += str(node.val)
                res += ','

                queue.append(node.left)
                queue.append(node.right)
            else:
                res += 'null'
                res += ','

        print(res)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        listNode = [item for item in data.split(',') if item]

        if not listNode or listNode[0] == 'null':
            return None

        root = TreeNode(listNode[0])
        queue = deque([root])

        index = 1

        while queue and index < len(listNode):
            current_node = queue.popleft()

            if listNode[index] != 'null':
                current_node.left = TreeNode(listNode[index])
                queue.append(current_node.left)
            index += 1

            if index < len(listNode) and listNode[index] != 'null':
                current_node.right = TreeNode(listNode[index])
                queue.append(current_node.right)
            index += 1

        return root
