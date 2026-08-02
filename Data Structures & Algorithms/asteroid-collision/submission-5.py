class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        collide = False
        for ast in asteroids:
            if ast > 0:
                res.append(ast)
            else:
                while res and res[-1] > 0 and ast < 0:
                    if abs(ast) > res[-1]:
                        res.pop()
                    elif abs(ast) < res[-1]:
                        break
                    else:
                        res.pop()
                        collide = True
                        break
                if (not res or res[-1] < 0) and not collide:
                    res.append(ast)
                collide =  False
        return res

"""
    1. use a stack for result
    2. while res and top > 0 and ast < 0
        if abs(ast) > top:
            pop top
        elif abs(ast) < top:
            break
        else:
            pop top
            break
    3. if not stack or res[-1] < 0:
        push ast
"""
        