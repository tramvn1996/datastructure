#a program to determine if we can advance through
# an array successfully or not based on the elements in
# the array
def furthest_reach(A):
    furthest_reach_sf, last_index = 0, len(A)-1
    i=0
    # i <= furthest_reach_sf since if we can't advance to the next
    # index, then the pointer can't keep moving

    #furthest_reach_sf == last_index means it reaches the end


    while i <= furthest_reach_sf and furthest_reach_sf < last_index:
        furthest_reach_sf=max(furthest_reach_sf, A[i]+i)
        i += 1

    return furthest_reach_sf >= last_index #return a True/False statement
    


B=[1,1,0,0,0,1]
print(furthest_reach(B))
