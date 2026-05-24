class Node:
    
    def __init__(self, key, val):
        """This represents a Node in the doubly linked list with key and value
        given when Noded object is initialized. prev and next pointers are set
        to None initially."""
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # cache is initiated as empty dict with mapping keys to node
        self.left = Node(0,0)  # dummy node initialization 
        self.right = Node(0,0)  # dummy node initialization 
        # and now we link the above dummy node together, keep in mind that our linked list right now is just these two dummy nodes thats it
        self.left.next = self.right  # left pointer's next is pointing at right pointer
        self.right.prev = self.left  # right pointer's prev is pointing at left pointer -- hence chain created
        # this also forms a structure where the node right after self.left ie at self.left.next is the Least Used Node
        # and the node right before self.right ie self.right.prev is the most recently used node

    # lets build our helper functions like insert and remove that we will use in the upcoming functions
    def insert(self, node):
        """Inserting the node just before the tummy tail node which is self.right,
        making the newly added node the Most Recently Used MRU"""
        prev = self.right.prev  # points to the node currently at the end of the list
        prev.next = node  # this updates the next pointer of node currently at the end of the list to our newly added node

        nxt = self.right  # this points at the dummy tail node which is self.right
        nxt.prev = node  #  updates the prev pointer of the dummy tail node to point to our new node
        node.next = nxt  # sets the next pointer of new node to point to dummy node (nxt is the dummy node from above see)
        
        node.prev = prev  # sets the prev pointer of the new node to the point to the node that was previously the last node in the list

    def remove(self, node):
        """We remove the given node by unlinking the node from the list by updating the
        next and prev pointers of its neighboring nodes to bypass it. """
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev  # node.prev node's next is now gonna point at nxt which was node.next's node. 
                                         # node.next node's prev pointer is now gonna point at prev which was node.prev's node. 


    def get(self, key: int) -> int:
        """Given the key, if its present in our cache dict, we return its value by .val,
        but before that we remove it and then insert it (inserted right before self.right)
        that way it becomes the most recently used cache as well."""
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """Adds key-value pair to the cache dict, it already exists updates the vaue and moves
        node to the front. If cache exceeds capacity, we evict the least recently used item
        ie the node right next to self.left which is self.left.next"""
        if key in self.cache:  # checking if the key is already in the cache
            self.remove(self.cache[key])  # the value at given key removed as the key was already in the cache
        self.cache[key] = Node(key, value)  # this updates/creates a new Node with the given key-value pair
        self.insert(self.cache[key])  # and now this will insert that newly built or updated node to our linked list

        # we must also check if after inserting this node we are over capacity or not:
        if len(self.cache) > self.capacity:
            lru = self.left.next  # if length of cache does exceed the capacity, then we declare node next to self.left ie self.left.next as Least Recently Used
            self.remove(lru)  # remove the lru node from the linked list
            del self.cache[lru.key]  # also deleting the value associated with lru's key in cache dictionary 

        
