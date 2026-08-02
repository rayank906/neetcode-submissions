class Solution:

    def encode(self, strs: List[str]) -> str:
        """
            1. for every s in strs
            2. append len(s) + s + # to result
            3. return "".join(result)
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
            1. init i to 0
            2. while i < len(s)
            3. gather nums until pound sign
            3. append s[i + 1: i + 1 + nums] to res
            4. i = i + 1 + nums
            5. return res
        """
        i = 0
        res = []
        nums = []
        while i < len(s):
            if s[i] == '#':
                num = int("".join(nums))
                res.append(s[i + 1 : i + 1 + num])
                i = i + 1 + num
                nums = []
            else:
                nums.append(s[i])
                i += 1
        return res

