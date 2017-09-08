#similar to the dutch flag problem, reorganize the list into 2 categories:
#1 is numbers < pivot
#2 is numbers >= pivot

def list_pivoting(L, x):
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()

    while L:
        if L.data < x:
            less_iter = L
            lest_iter = less_iter.next
        elif: L.data ==x:
            equal_iter = L
            equal_iter = equal_iter.next
        else:
            greater_iter = L
            greater_iter = greater_iter.next
        L = L.next

    #combine
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_iter.next

    return less_head.next
    
