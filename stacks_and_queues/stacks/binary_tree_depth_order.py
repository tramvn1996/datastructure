#write a program to seperate the nodes from a binary tree
#so that all the nodes that have the same distance to roots are grouped together

def binary_tree_depth_order(tree):
    result, curr_depth_nodes = [], collections.deque([tree]) #initialize a deque with data = tree
    while curr_depth_nodes:
        next_depth_nodes, this_level = collections.deque([]),[]
        #next_depth_nodes is an empty deque

        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft() #remove object of the left of the list
            if curr:
                this_level.append(curr.data)

                #defer the null checks to the null test above
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)
        curr_depth_nodes = next_depth_nodes
    return result

#time complexity is O(n) and space is O(m) where m is the max number of nodes at any depth
#return to review after binary tree
