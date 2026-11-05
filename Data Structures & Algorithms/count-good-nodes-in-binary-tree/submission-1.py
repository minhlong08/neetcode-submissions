# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxSeen):
            nonlocal count
            if not node:
                return
            
            # increase the count if current node is larger than every node in the leading path
            if node.val >= maxSeen:
                count += 1
                maxSeen = node.val
            
            dfs(node.left, maxSeen)
            dfs(node.right, maxSeen)
        
        dfs(root, float('-inf'))
        return count
        