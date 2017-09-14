#as computing lca from binary tree, we want to implement another method that optimize when 2 nodes
#are close to their ancestor
# how to:
# alternating moving updwards from the 2 nodes and storing the nodes visited as we move up
# each time we visit a node, we check to see if it has been visited before

def lca(node_0, node_1):
    iter_0, iter_1 = node_0, node_1
    nodes_on_path_to_root = set()
    while iter_0, iter_1:
        #ascend tree in tandem for these 2 nodes
        if iter_0:
            if iter_0 in nodes_on_path_to_root:
                return iter_0
            nodes_on_path_to_root.add(iter_0)
            iter_0 = iter_0.parent

        if iter_1:
            if iter_1 in nodes_on_path_to_root:
                return iter_1
            nodes_on_path_to_root.add(iter_1)
            iter_1 = iter_1.parent
    raise ValueError('node0 and node1 are not in the same tree')

    #trading time for space
    # for the binary_tree approach time is O(h) and space is O(1)
    #here time and space is O(D0+D1) where D0 and D1 is the distance from lca to node_0 and node_1
    # in worst case, the noes are leaves, lca is root, we end up using O(h) time and space
