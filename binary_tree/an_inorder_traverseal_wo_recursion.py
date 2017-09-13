#inorder traversal without recursion
#traverse the left subtree -> visit root -> traverse right subtree

def bst_in_sorted_order(tree):
    s, result = [],[]
    while s or tree:
        if tree:
            #add all the left subtree to s
            s.append(tree)
            #going left
            tree=tree.left
        else:
            #going up
            tree = s.pop()
            result.append(tree.data) # append the s.pop() data into result
            #going right
            tree=tree.right #add tree.right to tree->add to s -> append s.pop() to result
    return result

    #time O(n), space O(h)
