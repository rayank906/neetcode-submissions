# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
            1. make a traversal helper
            2. keep track of maxCount and currCount
            3. once base case hit, update maxCount and reset currCount
            4. return maxCount
        """
        maxCount = 0
        
        def dfs(root, curr):
            nonlocal maxCount

            if not root:
                maxCount = max(maxCount, curr)
                curr = 0
                return
            
            curr += 1
            dfs(root.left, curr)
            dfs(root.right, curr)
        
        dfs(root, 0)
        return maxCount
        