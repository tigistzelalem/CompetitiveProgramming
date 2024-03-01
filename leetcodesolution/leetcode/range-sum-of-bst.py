# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

            def range(root, low, high):
               

                if not root:
                    return 0

                count = 0
                if low <= root.val <= high:
                    count += root.val
                if root.val > low:
                   count +=  range(root.left, low, high)
                if root.val < high:
                     count +=  range(root.right, low, high)
            
                return count

            return range(root, low, high)
                
