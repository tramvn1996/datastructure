#create a cache for looking up prices of books identified by their ISBN
# implement lookup, insert, and remove
# use the Least Recently Used for eviction
# if an ISBN is already present, insert should not change the price,
#but it should update that entry to be the most recently used entry
# lookup also should update that entry to be the most recently Used

class LRUCache:
    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return False, None
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return True, price

    def insert(self, isbn, price):
        #we add the value for key only if key is not present
        #we don't update existing value
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._capacity <= len(self._isbn_price_table):
            self._isbn_price_table.popitem(last=False)
            #popitem implement LIFO if last=True, else FIFO
        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None

        #the time complexity  for each look up is O(1) for the hash table, and
        #O(1) for updating the queue -> O(1) overall
        
