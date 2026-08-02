# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indexes = defaultdict(int)
        for i in range(len(inorder)):
            indexes[inorder[i]] = i

        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1

            if len(preorder) == 1:
                return root
            
            idx = indexes[root.val]
            
            root.left = dfs(l, idx - 1)
            root.right = dfs(idx + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)
        


"""
    Base case: array of size 0, return None
    array of size 1, make root and return root
    0. to avoid looping when searching for index in inorder, make a hashmap of idx
    and values for inorder
    1. root of binary tree is first element of preorder
        root = TreeNode(preorder[0])
    2. access hashmap for idx of root.val in inorder
    3. assign root.left to inorder[:i], preorder(1:i + 1)
    4. assign root.right to inorder[i + 1:], preorder(i + 1:)

    TimeC: O(n) looping through preorder once, hashmap for O(1) access
    SpaceC: O(h) for the recursive call stack
"""
        