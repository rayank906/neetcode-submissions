class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class PrefixTree:

    def __init__(self):
        """
            1. initialise a trie node root
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
            1. using a ptr to root,
            2. for each character in word,
            3. if char doesn't exist as a child of the ptr, make a trienode for it
            4. move the ptr forward
            5. set end of word to true
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
            2. for each character in word,
            3. if char doesn't exist, return False
            4. move curr forward
            5. return curr.word
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        """
            1. using a ptr to root,
            2. for each character in word,
            3. if char doesn't exist, return False
            4. move curr forward
            5. return True
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
"""
    1. make a helper trienode to construct the trie class
        contains a hashmap of children and bool to indicate end of word
"""        