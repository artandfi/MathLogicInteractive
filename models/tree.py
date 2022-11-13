class TreeNode:
    def __init__(self, data, /):
        self.data = data
        self.children = []
    
    def __eq__(self, other):
        return (
            isinstance(other, TreeNode)
            and self.data == other.data
            and all(c1 == c2 for c1, c2 in zip(self.children, other.children))
        )



class Tree:
    def __init__(self, root):
        self.root = root
    
    def __eq__(self, other):
        return isinstance(other, Tree) and self.root == other.root