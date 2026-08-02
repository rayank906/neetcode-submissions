class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node): # Insert as MRU
        temp = self.right.prev
        temp.next = self.right.prev = node
        node.prev, node.next = temp, self.right

    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.next = node.prev = None
        

    def get(self, key: int) -> int:
        """
            1. if key in hashmap, remove from linked list then add back
                and return value
            2. else return -1
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        """
            1. if key in cache, 
                a. remove value from linked list
                b. make new node for key val pair and add to hashmap
                c. insert into linked list
            2. else 
                a. make new node for key val pair and add to hashmap
                b. insert into linked list
            4. if length of cache > capacity, remove left ptr in linked list
            5. delete from cache
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            temp = self.left.next
            self.left.next = temp.next
            temp.next.prev = self.left
            temp.next = temp.prev = None
            self.cache.pop(temp.key)

        

"""
    1. Hashmap to store key-val pairs, where value is a node
    2. Linked list with left and right dummy to keep track of LRU and MRU
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)