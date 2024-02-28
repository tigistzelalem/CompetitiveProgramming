# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_map = defaultdict(list)
        ans = []

        def dfs(node, row, col):
            if not node:
                return

            hash_map[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col +1)
        
        dfs(root, 0, 0)
        low = min(hash_map.keys())
        high = max(hash_map.keys())

        for i in range(low, high + 1):
            hash_map[i].sort()
            for j in range(len(hash_map[i])):
                hash_map[i][j] = hash_map[i][j][1]
            ans.append(hash_map[i])
        
        return ans

