# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, root.val, root.val)])
        max_val = 0

        while queue:
            curr, max_,  min_ = queue.popleft()
            curr_val = curr.val

            diff1 = curr_val - min_
            diff2 = max_ - curr_val
            
            max_val = max(max_val, diff1, diff2)

            if curr.left:
                queue.append((curr.left, max(curr_val, max_), min(curr_val, min_)))
            if curr.right:
                queue.append((curr.right, max(curr_val, max_), min(curr_val, min_)))

        return max_val

        

            

            

        
