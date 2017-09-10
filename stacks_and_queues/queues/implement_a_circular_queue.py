#implement a circular queue
# implement a queue API using an array for storing elements
#include a constructor function: takes as argument the initial capacity of the queue
#enqueue and deque function
#a function returns the number of elements stored
#implement dynamic resizing to support storing an arbitrary large number of elements

#solution:
#keep 1 more variable to track the head -> dequeue can calso be performed in O(1) time
# when enqueuing, we need to resize the array

class Queue:
    SCALE_FACTOR = 2
    def __init__(self, capacity):
        self._entries = [None]* capacity
        self._head=self._tail=self._num_queue_elements=0
        #since the array is empty, (_num_queue_elements = 0)

    def enqueue(self, x):
        if self._num_queue_elements==len(self._entries): #resize to add more elements
            #move the head to the front index (or index 0)
            self._entries = (
            self._entries[self._head:]+self._entries[:self._head])

            #reset head and tail
            self._head, self._tail = 0, self._num_queue_elements
            #add more space
            self._entries += [None] * len(self._entries) * Queue.SCALE_FACTOR

        self._entries[self._tail]=x
        self._tail = (self._tail +1 )% len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError('empty queue')
        self._num_queue_elements - = 1
        ret = self._entries[self._head]
        #move the head index to one place to the right
        self._head= (self._head + 1)%len(self._entries)
        return ret

    def size(self):
        return self._num_queue_elements

        #time and space complexity is O(1) since we don't have to shift anything
