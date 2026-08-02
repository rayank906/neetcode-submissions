class Solution:
    sizes = []

    def encode(self, strs: List[str]) -> str:
        """
            1. populate sizes arr
                sizes contain len of each substr in str
            2. return "".join(strs)
        """
        self.sizes = []
        for s in strs:
            self.sizes.append(len(s))
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        """
            1. create a res list
            2. init start to 0
            3. for every elem in size
                b. append s[start: start + elem]
                c. update start with elem
            4. return res
        """
        res = []
        start = 0
        for elem in self.sizes:
            res.append(s[start:start + elem])
            start = start + elem
        return res

