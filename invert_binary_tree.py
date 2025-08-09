class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root is None:
        return None
    # Swap the left and right children
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# Helper function to print tree in preorder
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Example usage:
# Constructing binary tree:    1
#                            /   \
#                           2     3
#                          / \   / \
#                         4   5 6   7
root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7))
    )

print("Original tree (preorder):")
preorder(root)  # Output: 1 2 4 5 3 6 7

invert_tree(root)

print("\nInverted tree (preorder):")
preorder(root)  # Output: 1 3 7 6 2 5 4