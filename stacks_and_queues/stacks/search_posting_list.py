# a Posting list is a linked-list with a jump field
#write an algorithm to compute jump-first order
#Assume each node has an integer field that holds their order, and is
#initialized to be -1

#recursively
def search_posting_list(L):
    def update_order(L):
        if L and L.order==-1:
            L.order=order[0]
            order[0]+=1
            update_order(L.jump)
            update_order(L.next)
    order[0]=0
    update_order(L)

#iteratively

def search_posting(L):
    s=[L]
    order=0
    while s:
        curr = s.pop()
        if curr and curr.order==-1:
            curr.order=order
            order+=1

            s+=[curr.next, curr.jump]
