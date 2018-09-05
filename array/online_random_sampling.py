#in contrast to the offine_random_sampling, online method constantly
#update the array with new random selected elements

import random
import itertools

def online_random_sampling(A, k):
    #store the first k elements
    sampling_results = list(itertools.islice(A,k))

    #Have read the first k elements
    num_seen_so_far = k
    for x in A:
        num_seen_so_far += 1
        idx_to_replace=random.randrange(num_seen_so_far)
        if idx_to_replace<k:
            sampling_results[idx_to_replace] = x
    return sampling_results

#Check back to see if it should return 1 elements twice in the result sampling
A=['a','b','c','d','e']
k=3
print(online_random_sampling(A, k))
