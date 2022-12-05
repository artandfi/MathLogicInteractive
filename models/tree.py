class TreeNode:
    """A node in the tree-like structure."""
    def __init__(self, data, /):
        self.data = data
        self.children = []

    @property
    def left(self):
        """Leftmost child of the node."""
        return self.children[0]
    
    @property
    def right(self):
        """Rightmost child of the node."""
        return self.children[-1]
    
    @property
    def leaves(self):
        """
            A list of leaves of the node.

            Returns:
                List[TreeNode]
        """
        return self._leaves(self)
    
    def _leaves(self, node, leaves=None):
        """
            Utility method for recursion in leaves method.
            Shouldn't be called elsewhere.

            Args:
                self (OperatorNode): Instance of this class.
                node (OperatorNode): Current node.
                leaves (Optional[List[OperatorNode]]): List of leaves at the current step.
            Returns:
                List[TreeNode]
        """
        if leaves is None:
            leaves = []
        
        if not node.children:
            leaves.append(node)
        
        for child in node.children:
            self._leaves(child, leaves)
        
        return leaves

    def __eq__(self, other):
        """
            Recursive check for equality of this node and the other.

            Args:
                self (OperatorNode): Instance of this class.
                other (OperatorNode): Another node.
            Returns:
                bool
        """
        return (
            isinstance(other, TreeNode)
            and self.data == other.data
            and all(c1 == c2 for c1, c2 in zip(self.children, other.children))
        )
