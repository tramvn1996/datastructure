#successor of node 0 is the node 1 that appears immediately after node 0 in a
# binary tree inorder traversal (lef->root->right)

#approach:
#if the node has a right subtree -> the successor must be in that right tree
# if the right sub-tree is not null -> the successor lie in the left-most position on that tree

def find_successor(node):
    if node.right:
        node=node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node.parent.right is node:
        node = node.parent

    return node.parent

    #time complexity is O(h)
