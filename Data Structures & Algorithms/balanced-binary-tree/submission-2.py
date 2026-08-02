# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]

            return [balanced, 1 + max(left[1], right[1])]

        balanced = dfs(root)
        return balanced[0]

"""
    1. base case, empty, return True
    2. helper function for height traversal returns a pair of bool and int
        a. takes in a root
        ai. if null, return [True, 0]
        b. traverses left
        c. traverses right
        d. check if left and right differ by 1 and if they are both balanced
        e. return the balance status and the maximum of the height of left and right
    3. call helper function on root.left and root.right
    4. run dfs helper
    5. return the boolean in the pair that is returned

    TC: O(n) since we go as deep as possible before starting computations
    SC: O(n) for the recursive call stack
"""
        