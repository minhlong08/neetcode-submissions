# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        res = ''
        while q:
            cur = q.popleft()
            if cur:
                res += f"{cur.val},"
                q.append(cur.left)
                q.append(cur.right)
            else:
                res += f"N,"
        return res[0:len(res)-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeValues = data.split(',')
        if nodeValues[0] == 'N':
            return None
        
        root = TreeNode(int(nodeValues[0]))
        q = deque()
        q.append(root)

        i = 1
        while q:
            curNode = q.popleft()
            
            if i < len(nodeValues) and nodeValues[i] != 'N':
                leftVal = int(nodeValues[i])
                curNode.left = TreeNode(leftVal)
                q.append(curNode.left)
            else:
                curNode.left = None

            if (i + 1) < len(nodeValues) and nodeValues[i + 1] != 'N':
                rightVal = int(nodeValues[i + 1])
                curNode.right = TreeNode(rightVal)
                q.append(curNode.right)
            else:
                curNode.right = None

            i += 2

            
        return root
