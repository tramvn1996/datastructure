#function to reverse a sub list in linked list
#locate the sublist, then reverse it
def reverse_sublist(L, start, finish):
    dummy_head=sublist_head = ListNode(0,L)
    for _ in range(1, start):
        sublist_head=sublist_head.next

    #reverse
    sublist_iter = sublist_head.next
    for _ in range(finish-start):
        temp = sublist_iter.next
        sublist_iter.next , temp.next, sublist_head.next = (
            temp.next, sublist_head.next, temp
        )
    return dummy_head.next
