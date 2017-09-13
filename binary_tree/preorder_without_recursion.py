#implement preorder traversal without recursion
#using stack (last-in, first-out),
#preorder: root -> left-subtree -> right-subtree


def preorder_traversal(tree):
    path, result = [tree],[]
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left] #append left last, since we want to pop left first
    return result

    #time O(n), space O(1)
