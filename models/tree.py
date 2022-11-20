class TreeNode:
    def __init__(self, data, /):
        self.data = data
        self.children = []

    @property
    def left(self):
        return self.children[0]
    
    @property
    def right(self):
        return self.children[-1]
    
    @property
    def leaves(self):
        return self._leaves(self)
    
    def _leaves(self, node, leaves=None):
        if leaves is None:
            leaves = []
        
        if not node.children:
            leaves.append(node)
        
        for child in node.children:
            self._leaves(child, leaves)
        
        return leaves


    def __eq__(self, other):
        return (
            isinstance(other, TreeNode)
            and self.data == other.data
            and all(c1 == c2 for c1, c2 in zip(self.children, other.children))
        )
