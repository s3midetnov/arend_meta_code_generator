import random


class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.is_leaf = (left is None and right is None)  # Fixed!

    def pretty_print(self, prefix="", is_left=True):
        """Prints the tree in a visually structured way."""
        if self.right:
            self.right.pretty_print(prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + repr(self.value))
        if self.left:
            self.left.pretty_print(prefix + ("    " if is_left else "│   "), True)

    def get_leaves_left_to_right(self):
        """
        Returns a list of all leaf values in left-to-right order.
        """
        if self.is_leaf:
            return [self.value]
        leaves = []
        if self.left:
            leaves.extend(self.left.get_leaves_left_to_right())
        if self.right:
            leaves.extend(self.right.get_leaves_left_to_right())
        return leaves


def random_group_tree(free_group_element: list) -> TreeNode:
    if len(free_group_element) == 0:
        return None  # Don't create a node at all
    if len(free_group_element) == 1:
        return TreeNode(free_group_element[0], None, None)
    else:
        split_ind = random.randint(1, len(free_group_element))  # Note: up to len, not len-1
        left = free_group_element[:split_ind]
        right = free_group_element[split_ind:]

        left_tree = random_group_tree(left) if left else None
        right_tree = random_group_tree(right) if right else None

        # Handle edge cases where one side might be None
        if left_tree is None:
            return right_tree
        if right_tree is None:
            return left_tree

        return TreeNode('', left=left_tree, right=right_tree)


def tree_to_expression(tree):
    """
    Converts the tree to an expression string with G.* operations.
    Leaf nodes return their value, internal nodes return (left G.* right).
    """
    if tree is None:
        return ""

    if tree.is_leaf:
        return str(tree.value)

    left_expr = tree_to_expression(tree.left) if tree.left else ""
    right_expr = tree_to_expression(tree.right) if tree.right else ""

    return f"({left_expr} G.* {right_expr})"