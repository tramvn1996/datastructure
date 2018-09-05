#compute the lca of 2 nodes when nodes have a parent fields
# we do this by computing the height difference of 2 nodes
# then increment the longer-heighted nodes first
# then increment both of the nodes in tandem until they reach their first lca

def lca(node0, node1):
    def get_depth(node):
        depth = 0
        while node:
            depth+=1
            node=node.parent
        return depth
    depth0, depth1 = get_depth(node0), get_depth(node1)

    #make node0 as the depper node in order to simplify the code
    if depth0 < depth1:
        node0, node1 = node1, node0

    #ascend from the deeper node
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    #now ascend from both nodes
    while node1 is not node0:
        node0, node1 = node0.parent, node1.parent
    return node0

    #time O(h), space O(1)
