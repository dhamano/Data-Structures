from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes
    it can hold, the current number of nodes it is holding, a
    doubly-linked list that holds the key-value entries in the
    correct order, as well as a storage dict that provides
    fast access to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        # self.storage = DoublyLinkedList()
        # self.cache = {}
        # LECTURE VERSION
        self.size = 0
        self.storage = dict()
        self.order = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if
    the key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if key in self.cache:
        #     # self.storage.move_to_front(self.cache[key])
        #     self.storage.move_to_end(self.cache[key])
        #     return self.cache[key].value
        # LECTURE VERSION
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-added pair
    should be considered the most-recently used entry in the cache.
    If the cache is already at max capacity before this entry is added,
    then the oldest entry in the cache needs to be removed to make room.
    Additionally, in the case that the key already exists in the cache,
    we simply want to overwrite the old value associated with the key
    with the newly-specified value.
    """
    # def set(self, key, value):
    #     if key in self.cache:
    #         # self.storage.move_to_front(self.cache[key])
    #         self.storage.move_to_end(self.cache[key])
    #         if self.cache[key].value != value:
    #             self.cache[key].value = value
    #     else:
    #         if len(self.cache) == self.limit: # {"item1":node} --- node.value == "1"
    #             # el = self.storage.tail
    #             el = self.storage.head
    #             del_key = ''
    #             for the_key in self.cache:
    #                 if self.cache[the_key].value == el.value:
    #                     del_key = the_key
    #                     return
    #             self.cache.pop(del_key)
    #             self.storage.delete(el)
    #         # self.storage.add_to_head(value)
    #         # self.cache[key] = self.storage.head
    #         self.storage.add_to_tail(value)
    #         self.cache[key] = self.storage.tail

    # LECTURE VERSION
    def set(self, key, value): # {"item1":node} ---- node.value == (item1, 1)
        # cases to handle
        # does the key already exist in the cache
        if key in self.storage:
            # key is here so we should replace the value
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return
        # are we at cap or not?
        # yes - dump oldest item
        if self.size == self.limit:
            # dump the oldest item
            # remove from head/order
            # delete the key/value pair
            # option 1, explicit
            # del self.storage[self.order.head.value[0]]
            # self.order.remove_from_head()

            # option 2
            del self.storage[self.order.remove_from_head()[0]]
            # subtract count
            self.size -= 1
        
        # no - nothing extra needed

        # how do we put stuff into the cache?
        #if cache not full and key not present
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1


# l = LRUCache(3)

# l.set('item1', 'a');
# l.set('item2', 'b');
# l.set('item3', 'c');
# # l.set('item2', 'z');
# l.set('item4', 'd');
# print(l.get('item2'))
