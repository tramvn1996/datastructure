#test if 2 linked list cycle-free have any overlapping
#start with the longer list first and run to the node that
#leave the length of the shorter list, then increment until tail
def overlapping(L1, L2):
    def length(L):
        length = 0
        while L:
            length += 1
            L= L.next
        return length
    L1_len, L2_len = length(L1),length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1 #L2 is the longer list
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    while L1 and L2 and L1 is not L2:
        L1=L1.next
        L2=L2.next
    return L1
    
