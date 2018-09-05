#a function to reverse a linked list
# Using iterative with time complexity O(n) and space O(1)
# 1 > 2 > 3 > null
# null < 3 < 2 < 1

#While traversing the list, change the current node's next pointer to the point
# to its previous element
#since a node doesnot have reference to its previous node, store its previous
#element beforehand
#add another pointer to store the next node before changing the reference

def reverse_list(L):
    prev, curr = ListNode(), ListNode()
    prev = null
    curr = L
    while (curr != null):
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp

    return prev
    #time complexity is O(n) and space O(1)
