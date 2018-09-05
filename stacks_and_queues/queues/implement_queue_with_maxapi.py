#implement a queue with Max API
#to do this, we create another queue to store max value
#when enque, if the new element > max_array[-1]-> remove everything else and add the new max to the queue head
##if the new element < the current max -> enqueue it to the max array

#when dequeue, if the dequeue is the current max -> dequeue the max array too
#otherwise, the max array remain unchanged

class QueueWithMax:
    def __init__(self):
        self._entries = collections.deque()
        self._candidate_for_max = collections.deque()

    def enqueue(self, x):
        self._entries.append(x)

        while self._candidate_for_max and self._candidate_for_max[-1] < x:
            self._candidate_for_max.pop()
        self._candidate_for_max.append(x)

    def dequeue(self):
        if self._entries:
            result = self._entries.popleft()
            if result == self._candidate_for_max:
                self._candidate_for_max.popleft()
            return result
        raise IndexError('empty queues')

    def max(self):
        if self._candidate_for_max:
            return self._candidate_for_max[0]
        raise IndexError("empty queue")

    #time complexity O(1) 
