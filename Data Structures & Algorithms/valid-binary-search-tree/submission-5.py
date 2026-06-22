# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True


        return self.checkBst(root, -math.inf, math.inf)
    
    def checkBst(self, root: Optional[TreeNode], low: float, high: float) -> bool:
        if not root:
            return True
        
        if not (low < root.val < high):
            return False

        left = self.checkBst(root.left, low, root.val)
        right = self.checkBst(root.right, root.val, high)

        return left and right
        