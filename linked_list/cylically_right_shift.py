#a function to cyclic right shift the whole singly linked list k nodes
# method:
# find the tail node t and the length of the list
# connect the current tail to the current head
# make the pointer to the current tail and iterate it to the (n-k)th node
#(since it'll be the position for the current tail)
#set the new_head = new_tail.next
#set the new_tail.next = none

def cyclically_shift(L,k):
    if not L:
        return L
    #compute the length of L
    tail, n = L, 1
    while tail.next: #(is not null)
        n+=1
        tail = tail.next

    k %= n
    if k==0:
        return L

    tail.next = L #make a cycle
    step_to_new_head, new_tail = n-k, tail
    while step_to_new_head:
        step_to_new_head -= 1
        new_tail = new_tail.next
        #this cycle will iterate until it finds the new head
        #and then break the cycle to have a new list


    new_head = new_tail.next
    new_tail.next = None
    return new_head

#time complexity is O(n) and space is O(1)
