class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            0. hardcode a mapping of letters to digits
            1. choose a letter for a given digit
            2. recurse with the next digit
            3. if idx oob, append curr pattern to result
        """
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        def recurse(i, curr, res):
            if i >= len(digits):
                if curr:
                    res.append("".join(curr))
                return
            
            for letter in digit_map[digits[i]]:
                curr.append(letter)
                recurse(i + 1, curr, res)
                curr.pop()
        
        res = []
        recurse(0, [], res)
        return res
        