#delete a node from a singly linked list
def delete_node(node_to_delete):
    node_to_delete.data = node_to_delete.next.data #change the current node's data
        #to next node's data
    node_to_delete.next = node_to_delete.next.next
    #change the direction to the node after the next node
    
