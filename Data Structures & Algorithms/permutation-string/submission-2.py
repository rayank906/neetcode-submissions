class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u' ,'v', 'w', 'x', 'y', 'z']
        map1, map2 = {}, {}
        for let in alphabet:
            map1[let] = 0
            map2[let] = 0

        for char in s1:
            map1[char] += 1
        
        l = 0
        for i in range(len(s1)):
            map2[s2[i]] += 1
        if map1 == map2:
            return True
        
        for r in range(len(s1), len(s2)):
            map2[s2[l]] -= 1
            l += 1
            map2[s2[r]] += 1
            if map1 == map2:
                return True
        return False


"""
    sliding window + hashmap
    1. make a hashmap of s1, make a window of size s1 to use on s2
    2. make a window hashmap for s2 of size s1
    3. compare hashmaps
    4. if !=, slide the window by removing the character at the left
    5. else, return True
    6. return False if the end is reached
"""
        