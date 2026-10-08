# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)

            # Split at this current node (take both left and right)
            path = root.val + left + right
            res = max(res, path)

            # Do not split at this current node
            # -> Return node value + the max sum of left tree or right tree
            return root.val + max(left,right)


        dfs(root)
        return res

        