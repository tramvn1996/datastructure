#we need to design a stack which supports push and pop
#we need to implement max, which returns the max value in the stack

import collections

#to implement the max function, we'll implement each element in the stack is a tuple
# the tuple will have 2 parts, element value itself and the max element
#the max value will change whenever there's a value greater than the max value

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element','max'))

def __init__(self):
    self.element_with_cached_max = []

def empty(self):
    return len(self.element_with_cached_max) == 0

def push(self):
    self.element_with_cached_max.append(
    self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max()))
    )
def max(self):
    if self.empty():
        raise IndexError("empty stack")

    return self.element_with_cached_max[-1].max

def pop(self):
    if self.empty():
        raise IndexError("empty stack")
    return self.element_with_cached_max.pop().element


#we can reduce space complexity by using another array, which stores the max value
# and its count
#the array element is our stack, which stores all the elements. but this time,
#we're not storing max in our stack

class Stack:
    class MaxWithCount:
        def _init_(self, max, count):
            self.max, self.count =max, count
    def _init_(self):
        self._element=[]
        self._cached_max_with_count = []

    def empty(self):
        return len(self.element)==0

    def max(self):
        if self.empty():
            raise IndexError("stack is empty")
        return self._cached_max_with_count[-1].max


    #to pop the element out of the stack, we're going to pop the stack array
    #however, that value we just popped might be the largest element at the time
    #therefore, we need to check if it's the current max
    #if it is the current max value, then we need to decrement the count of that max value by 1
    #if the count after is 0, we need to remove that max element out of the max array

    def pop(self):
        if self.empty():
            raise IndexError("stack is empty")
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max

        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element

        #when we push an element to the stack, we're just pushing that element to the stack
        #however, we need to update the max array too
        #if the len of the max array is 0, there's no max value -> this is the first element ever
        #-> we need to add the element to the max array
        # else: we need to check the current max (the last item in the max array)
        #if the element is being pushed is the current max, increment the max count
        # if the pushed element is not, and larger than the current max, then we push it to the max array

        def push(self, x):
            self._element.append(x)
            if len(self._cached_max_with_count) == 0:
                self._cached_max_with_count.append(self.MaxWithCount(x,1))

            else:
                current_max = self._cached_max_with_count[-1].max
                if x == current_max:
                    self._cached_max_with_count[-1].count += 1
                elif x > current_max:
                    self._cached_max_with_count.append(self.MaxWithCount(x,1))
