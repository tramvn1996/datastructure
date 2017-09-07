#test overlapping for lists that can be cyclic
#first test if the lists are cyclic:
#if neither of them is cyclic, we can use the overlapping method
#if one of them is cyclic, that means there's no overlapping
#if both are cyclic, there's 2 possibilities:
#case 1:
#if the meeting point is before the cycle, then we use the previous overlapping method
#case 2:
#if the meeting point is inside the cycle, then we use the test_cyclicity
#to see if they'll meet

def overlapping_lists(L1, L2):
    #Store the start of the cycle if any
    root1, root2 = has_cycle(L1), has_cycle(L2)

    if not root1 and not root2: #both lists don't have cycle
        return overlapping_with_no_cycle(L1, L2)
    elif (root1 and not root2) or (not root1 and root2):
        #one list has cycle and the other doesn't
        return None

    #Both lists have cycle
    temp = root2
    while True:
        temp = temp.next
        if (temp is root1) or (temp is root2):
            break

    if temp is not root1:
        return None #cycles are disjoint

    #calculate distance between a and b
    def distance(a,b):
        dis = 0
        if a is not b:
            a=a.next
            dis+=1
        return dis

    #L1 and L2 end in the same cycle, locate the overlapping node if
    #they first overlap before cycle starts
    stem1_length, stem2_length = distance(L1, root1), distance(L2, root2)
    if stem1_length>stem2_length:
        L2, L1 =L1, L2 #L2 is the longer stem_length
        root1, root2 = root2, root1
    for _ in range(abs(stem2_length- stem1_length)):
        L2=L2.next
    while (L1 is not L2) and (L1 is not root1) and (L2 is not root2):
        L1, L2 = L1.next, L2.next

    #if L1==L2 before reaching root1, then it means they overlap before cycle
    #otherwise, we can return any node on the cycle
    return L1 if L1 is L2 else root1
