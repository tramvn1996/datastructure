#we basically sort the array first based on first name, so that the same first
#names are close to each other

#need to initiate first_name, last_name class
class Name:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __equal__ (self, other):
        return self.first_name == other.first_name

    def __It__(self, other):
        return (self.first_name<other.first_name
            if self.first_name!=other.first_name
            else self.last_name<self.last_name)

def remove_first_name_dup(A):
    A.sort()
    write_index = 1
    for cand in A[1:]:
        if cand!=A[write_index-1]:
            A[write_index]=cand
            write_index+=1
    del(A[write_index:])
