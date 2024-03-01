# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)

        def buildTree(ans):
            if not ans:
                return None
            mid = len(ans) // 2

            root = TreeNode(ans[mid])
            root.left = buildTree(ans[:mid])
            root.right = buildTree(ans[mid + 1:])
        
            return root
        
        return buildTree(ans)
        
        

