from models.tree import TreeNode
from models.operators import impl, operator_strings, operator_priority


class OperatorNode(TreeNode):
    def __init__(self, operator):
        super().__init__(operator)
        self.operator = operator
        self.literal_values = None
    
    def __str__(self):
        return operator_strings[self.operator]

    @property
    def value(self):
        return self.operator(*[child.value for child in self.children])
    
    @property
    def priority(self):
        return operator_priority[self.operator]

    @property
    def formula(self):
        terms = []
        self._traverse(self, terms)
        return "".join(terms)
    
    def _traverse(self, node, terms):
        for child in node.children[:-1]:
            self._traverse_with_parens(node, child, terms)
            
        terms.append(str(node))

        if node.children:
            self._traverse_with_parens(node, node.children[-1], terms)
    
    def _traverse_with_parens(self, node, child, terms):
        needs_parens = (
            node.priority < child.priority
            or isinstance(node, OperatorNode)
            and isinstance(child, OperatorNode)
            and node.operator == child.operator == impl
        )

        terms.extend(["("] if needs_parens else [])
        self._traverse(child, terms)
        terms.extend([")"] if needs_parens else [])


class LiteralNode(TreeNode):
    def __init__(self, name: str, value=False):
        super().__init__(name)
        self.name = name
        self.priority = 0
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    def __str__(self):
        return self.name
