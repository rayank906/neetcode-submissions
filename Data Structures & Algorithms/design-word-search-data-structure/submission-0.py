class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        """
            initialise a root TrieNode
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
            1. using a ptr to root,
            2. for every char in word,
            3. if it doesn't exist in the children, make TrieNode() for it
            4. move ptr to the next TrieNode
            5. set last character flag to True
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        """
            1. using a ptr to root,
            2. for every char in word,
            3. if it doesn't exist in the children and != '.', return False
            4. move ptr to next TrieNode
            5. return curr.word
        """
        curr = self.root

        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr =  curr.children[word[i]]
            return curr.word
        return dfs(0, curr)       


        
