# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def buildTree(nums):
            if not nums:
                return None
            
            maxi = float('-inf')
            idx = -1
            for i in range(len(nums)):
                if nums[i] > maxi:
                    maxi = nums[i]
                    idx = i

            root = TreeNode(maxi)
            root.left = buildTree(nums[0 :idx])
            root.right = buildTree(nums[idx + 1 : len(nums)])
            return root

        return buildTree(nums)