#find a node in position kth in an inorder traversal
# inorder traversal is traversing from the left-subtree -> root -> right tree

#the idea is that if k > L(where L is the number of nodes in the left-subtree)
#-> k is not on the left subtree
#else if k < L -> k is on the left
def find_kth_node(tree, k):
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k:
            k -= left_size + 1
            tree = tree.right

        elif left_size ==k-1:
            return tree
        else:
            tree=tree.left
    return None
#since we descend the tree in each iteration, the time complexity is O(h)
