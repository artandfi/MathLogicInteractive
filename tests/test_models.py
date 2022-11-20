from unittest import TestCase
from models.tree import TreeNode


class TestTreeOperations(TestCase):
    def setUp(self):
        nodes = [TreeNode(i) for i in range(5)]
        nodes[0].children.extend([nodes[1], nodes[3], nodes[4]])
        nodes[1].children.append(nodes[2])

        self.root1 = nodes[0]
        self.root2 = nodes[0]
        self.leaves = [TreeNode(i) for i in range(2, 5)]
    
    def test_node_equality(self):
        self.assertEqual(self.root1, self.root2)
    
    def test_node_leaves(self):
        self.assertEqual(self.root1.leaves, self.leaves)

