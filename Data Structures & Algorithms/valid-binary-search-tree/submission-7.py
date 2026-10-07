# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minValue = float("-inf")
        maxValue = float("inf")

        def validBST(root, minValue, maxValue):
            if not root:
                return True
            
            if root.val <= minValue or root.val >= maxValue:
                return False
            
            return validBST(root.left, minValue, root.val) and validBST(root.right, root.val, maxValue)

        
        return validBST(root, minValue, maxValue)
        