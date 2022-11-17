from unittest import TestCase
from models.tree import Tree, TreeNode


class TestTreeOperations(TestCase):
    def setUp(self):
        nodes = [TreeNode(i) for i in range(5)]
        nodes[0].children.extend([nodes[1], nodes[3], nodes[4]])
        nodes[1].children.append(nodes[2])
        self.tree1 = Tree(nodes[0])
        self.tree2 = Tree(nodes[0])
    
    def test_node_equality(self):
        self.assertEqual(self.tree1.root, self.tree2.root)
    
    def test_tree_equality(self):
        self.assertEqual(self.tree1, self.tree2)
