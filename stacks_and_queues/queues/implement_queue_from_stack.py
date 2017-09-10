#write a function that implement enqueue and dequeu for a stack
class Queue:
    def __init__(self):
        self._enq, self._deq = [],[]

    def enqueue(self, x):
        self._enq.append(x)


        #transfer all the element into another stack to get the bottom element out

    def dequeue(self, x):
        if not self._deq:
            #transfer to another stack
            while self._enq:
                self._deq.append(self._enq.pop())

        if not self._deq: #deq still empty'
            raise IndexError("empty queue")
        return self._deq.pop()

        
