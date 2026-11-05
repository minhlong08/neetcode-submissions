# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        while q:
            lastNode = None

            # traversing this level of the tree to find the last node
            # the node can be view from right side is the last node of each level
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    lastNode = node
                    q.append(node.left)
                    q.append(node.right)
            # add the last node to the result
            if lastNode:
                res.append(lastNode.val)

        return res