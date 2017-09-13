# a binary tree in which each node contains a binary digit
# design an algorithm  to compute the sum of the binary numbers
# each time we visit a node, we compute its value by encoding its parent
# then if it's the leaf, we return the int
# but if it has children, we move on to its left and right children

def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0
    partial_path_sum = partial_path_sum*2 + tree.data
    if not tree.left and not tree.right: #tree leaf
        return partial_path_sum
    #non-leaf
    return (sum_root_to_leaf(tree.left, partial_path_sum), sum_root_to_leaf(tree.right, partial_path_sum))

    #time O(n) space O(h)
