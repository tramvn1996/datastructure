#add a method that re-arrange the linked list
#so the even-numbered nodes are followed by odd-numbered nodes

def even_odd_merge(L):
    if not L:
        return L
    even_dummy_head, odd_dummy_head = ListNode(), ListNode()
    tail , turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tail[turn].next = L
        L=L.next
        tail[turn] = tail[turn].next
        turn ^=1 #alternate between 0 and 1

    tail[1].next = None
    tail[0].next = odd_dummy_head.next
    return even_dummy_head.next

    #time complexity is O(n) and space is O(1)
