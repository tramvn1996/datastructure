#a function to test if a linked list is  palindrome
#iterate with 2 fast and slow iterators
#then slow will stop at the middle of the linked list
def is_linked_list(L):
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    #compare the first half and the reverse of the second half
    first_half_iter , second_half_iter = L, reverse_linked_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = (second_half_iter.next, first_half_iter.next)

    return True

    #time complexity O(n), space O(1)
