# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque()

        queue.append(root)

        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return res
        

"""
    bfs on root, retain rightmost queue value only
    1. if not root, return []
    2. make a queue
    3. append root
    4. while queue:
        append queue[-1] to res
        loop through curr values of queue
        pop each value,
        append its children
    5. repeat until queue empty
    6. return res

    TC: O(h), where h is the height of the tree in worst case
    SC: O(n), for res array
"""
        