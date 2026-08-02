# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root
        
        idx = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                idx = i
                break
        
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root
        


"""
    Base case: array of size 0, return None
    array of size 1, make root and return root
    1. root of binary tree is first element of preorder
        root = TreeNode(preorder[0])
    2. loop through inorder to find root.
    3. assign root.left to inorder[:i], preorder(1:i + 1)
    4. assign root.right to inorder[i + 1:], preorder(i + 1:)

    TimeC: O(n^2) looping through preorder once
    SpaceC: O(h) for the recursive call stack
"""
        