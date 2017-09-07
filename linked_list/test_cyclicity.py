#Test if there's a cyclicity within a linked list
#which means that there's a cycle within a list
def has_cycle(head):
    #method calculating how long the cycle is
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start=start.next
            if start is end:
                return step
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:

            #find the start of the cycle
            cycle_iter = head
            for _ in range(cycle_len(slow)):
                cycle_iter = cycle_iter.next
            it= head #now the distance between node it and cycle_iter
                    #is the length of the cycle_iter
            while it is not cycle_iter:
                it=it.next
                cycle_iter=cycle_iter.next
            return it #start of the cycle_iter
    return None #no cycle detected
