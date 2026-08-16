class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            - build adj list of edges between words
                - starting at begin
                - check all words it maps to, add to adjlist
                - for word in wordlist,
                - go through each char and see if theres a 1 char diff
                - if 1 char diff, add to adjlist

            - run bfs on the adj list
                - add start word on queue
                - while q, pop all elem off q
                - if endword, return count
                - add all neighbors to queue
                - incr count
        """
        graph = {w: [] for w in wordList}
        graph[beginWord] = []
        if endWord not in graph:
            return 0
        
        def oneDiff(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
                    if count > 1:
                        return False
            return True if count != 0 else False
        
        for word in wordList:
            if oneDiff(word, beginWord):
                graph[beginWord].append(word)
                graph[word].append(beginWord)
            
        for word1 in wordList:
            for word2 in wordList:
                if oneDiff(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        
        q = deque()
        visit = set()
        count = 1
        q.append(beginWord)
        visit.add(beginWord)

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                
                for neigh in graph[word]:
                    if neigh not in visit:
                        q.append(neigh)
                        visit.add(neigh)
            count += 1
        return 0

        

        