# a function to check if the tree is balanced
# a tree is balanced if the difference betwee the left subtree and
# the right subtree <= 1

#using recursion to recurse to the furthest left leaf, and then move on to its
#corresponding right root/leaf

def is_balanced_binary(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced','height'))

    #First value of the return value indicates if tree is balanced, and
    #if balance, return the height of the tree
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) #Base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False,0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balance = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balance, height)
    return check_balanced(tree).balanced

    #space O(h) h->height of the tree, time O(n) -> n is number of nodes in the tree
