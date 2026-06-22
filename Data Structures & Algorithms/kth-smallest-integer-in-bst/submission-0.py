# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        count = [k]
        return self.inOrder(root, count)
        
    def inOrder(self, root: Optional[TreeNode], count: List[int]) -> int | None:
        if not root:
            return None
        
        left = self.inOrder(root.left, count)

        count[0] = count[0] - 1
        if left:
            return left

        if count[0] == 0:
            return root.val

        

        right = self.inOrder(root.right, count)
        if right:
            return right
        return None