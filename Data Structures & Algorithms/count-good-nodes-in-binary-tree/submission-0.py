# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(root, max_seen):
            count = 0
            if not root:
                return 0
            
            if max_seen <= root.val:
                count += 1
                max_seen = max(max_seen, root.val)
            
            return count + dfs(root.left, max_seen) + dfs(root.right, max_seen)
        
        max_seen = root.val

        return dfs(root, max_seen)

"""
    1. make a global good count
    2. make traversal function
        a. args {root, max_seen}
        b. if max_seen <= root.val, increment count
        c. max_seen = max(max_seen, root.val)
        d. recursively traverse through left and right subtrees
    3. return count

    TimeC: O(n), we are visiting every node in tree
    SpaceC: O(h), where h is the height of recursive call stack
"""
        