# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque()

        queue.append(root)

        while queue:
            add = []
            for i in range(len(queue)):
                cur = queue.popleft()
                add.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(add)
        return res

"""
    1. Base case, if not root, return []
    2. Make a queue
    3. Append root to queue
    4. while queue, 
        pop all curr elements from queue using a for (left)
        append all popped curr elements to a sublist in res
    5. push children of popped element to the right
    6. repeat until queue is empty

    TimeC: O(n), traverse through the whole tree
    SpaceC: O(n), for additional queue and res array
"""
        