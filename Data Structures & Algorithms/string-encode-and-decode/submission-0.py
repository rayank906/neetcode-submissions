class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += strs[i]
            res += "é"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        hold = ""
        for char in s:
            if char == "é":
                res.append(hold)
                hold = ""
            else:
                hold += char
        
        return res
