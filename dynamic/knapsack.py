import collections

Items = collections.namedtuple('Items', ('weight value'))

item_arr = [[1,2],[2,4],[4,6]]

def knapsack(n, capacity):

    items = []
    for item in n:
        items.append(Items(item[0],item[1]))



    def helper(index, capacity):

        #if the weight > capacity, then return 0

        if index <0:
            return 0

        if arr[index][capacity] == -1:
            with_curr =  (0 if capacity < items[index].value else items[index].weight + helper(index-1, capacity-items[index].weight))

            without_curr = helper(index-1, capacity)
            arr[index][capacity] = max(with_curr, without_curr)

        return arr[index][capacity]

    arr = [[-1]*(capacity+1)]*len(n)
    return helper(len(n)-1, capacity)

print(knapsack(item_arr, 4))
