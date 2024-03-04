# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        def count(node, counts):
            if not node:
                return
            
            count(node.left, counts)
            counts[node.val] += 1
            count(node.right, counts)
        
        count(root, counts)
        prevFreq = 0
        ans = []

        for node, freq in counts.items():
            if freq > prevFreq:
                ans = [node]
                prevFreq = freq
            elif freq == prevFreq:
                ans.append(node)
        return ans

       
           
            

