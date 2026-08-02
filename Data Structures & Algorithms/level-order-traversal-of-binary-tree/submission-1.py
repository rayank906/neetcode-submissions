# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            1. init res
            2. init queue with the root node
            3. while curr len queue > 0:
                3b. init temp
                4. for all elems in q
                    5. pop from q, add to temp
                    6. if left, right children exist, add them to the q
                7. add temp to res
            8. return res
        """
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            temp = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                temp.append(curr.val)
            res.append(temp)
        return res
        