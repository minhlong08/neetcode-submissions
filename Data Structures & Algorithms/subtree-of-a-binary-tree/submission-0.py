# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSametree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 and root2:
            return False
        elif root1 and not root2:
            return False
        else:
            if root1.val != root2.val:
                return False
            left = self.isSametree(root1.left, root2.left)
            right = self.isSametree(root1.right, root2.right)

            return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and not subRoot:
            return False
        else:
            if self.isSametree(root, subRoot):
                return True
            
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)

            return left or right





