class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
            1. sort the array
            2. use two ptrs l and r to 0, len(people) - 1
            3. if l + r > limit, incr boats and move r inwards
            4. if l + r <= limit, incr boats and move both inwards
            5. return num boats
        """
        people.sort()
        boats = 0
        l, r = 0, len(people) - 1
        while l < r:
            weight = people[l] + people[r]
            if weight > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            boats += 1
        if (l == r):
            boats += 1
        return boats
        