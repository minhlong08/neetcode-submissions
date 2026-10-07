# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append([root])
        res = []
        while q:
            curLevelList = q.popleft()
            curLevel = [node.val for node in curLevelList]
            res.append(curLevel)
            
            nextLevel = []
            for node in curLevelList:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            if nextLevel:
                q.append(nextLevel)

        return res