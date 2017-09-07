#delete the last k-th node in a singly linked list
# Using 2 iterators:
# First one will loop k nodes
# Second one will loop in tandem with the 1st one until the end

def remove_kth_last(L,k):
    dummy_head = ListNode(0,L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummy_head.next
    
