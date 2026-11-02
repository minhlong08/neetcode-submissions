# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def dfs(node):
            nonlocal flag
            if not node:
                return -1

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if abs(leftHeight - rightHeight) > 1:
                flag = False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return flag