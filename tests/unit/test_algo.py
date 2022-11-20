from unittest import TestCase
from models.operators import and_, or_, impl, eq
from models.propositional_logic.formula_nodes import LiteralNode, OperatorNode
from algo.propositional_logic import all_number_splits_into_addends, generate_propositional_formula_root, is_tautology


class TestPropositionalLogicAlgorithms(TestCase):
    def test_all_number_splits_into_addends1(self):
        number, addends_no = 3, 1
        splits = [[3]]
        self.assertEqual(splits, all_number_splits_into_addends(number, addends_no))
    
    def test_all_number_splits_into_addends2(self):
        number, addends_no = 7, 2
        splits = [
            [0, 7],
            [1, 6],
            [2, 5],
            [3, 4],
            [4, 3],
            [5, 2],
            [6, 1],
            [7, 0]
        ]
        self.assertEqual(splits, all_number_splits_into_addends(number, addends_no))
    
    def test_all_number_splits_into_addends3(self):
        number, addends_no = 5, 3
        splits = [
            [0, 0, 5],
            [0, 1, 4],
            [0, 2, 3],
            [0, 3, 2],
            [0, 4, 1],
            [0, 5, 0],
            [1, 0, 4],
            [1, 1, 3],
            [1, 2, 2],
            [1, 3, 1],
            [1, 4, 0],
            [2, 0, 3],
            [2, 1, 2],
            [2, 2, 1],
            [2, 3, 0],
            [3, 0, 2],
            [3, 1, 1],
            [3, 2, 0],
            [4, 0, 1],
            [4, 1, 0],
            [5, 0, 0]
        ]
        self.assertEqual(splits, all_number_splits_into_addends(number, addends_no))

    def test_generate_propositional_formula(self):
        generate_propositional_formula_root([and_, or_, impl], 7, 4)
    
    def test_propositional_formula_evaluation1(self):
        formula = "(AvB)&C->B"
        root = OperatorNode(impl)
        root.children.append(OperatorNode(and_))
        root.children.append(LiteralNode("B", False))
        root.left.children.append(OperatorNode(or_))
        root.left.children.append(LiteralNode("C", True))
        root.left.left.children.append(LiteralNode("A", True))
        root.left.left.children.append(LiteralNode("B", False))

        self.assertEqual(formula, root.formula)
        self.assertFalse(root.value)
    
    def test_propositional_formula_evaluation2(self):
        formula = "A&B->(B->(C->A))"
        root = OperatorNode(impl)
        root.children.append(OperatorNode(and_))
        root.children.append(OperatorNode(impl))
        root.left.children.append(LiteralNode("A", True))
        root.left.children.append(LiteralNode("B", False))
        root.right.children.append(LiteralNode("B", False))
        root.right.children.append(OperatorNode(impl))
        root.right.right.children.append(LiteralNode("C", True))
        root.right.right.children.append(LiteralNode("A", True))

        self.assertEqual(formula, root.formula)
        self.assertTrue(root.value)
    
    def test_propositional_formula_evaluation3(self):
        formula = "A<->B<->C"
        root = OperatorNode(eq)
        root.children.append(LiteralNode("A", False))
        root.children.append(OperatorNode(eq))
        root.right.children.append(LiteralNode("B", True))
        root.right.children.append(LiteralNode("C", False))

        self.assertEqual(formula, root.formula)
        self.assertTrue(root.value)
    
    def test_tautology1(self):
        # A->AvB
        formula_root = OperatorNode(impl)
        formula_root.children.append(LiteralNode("A"))
        formula_root.children.append(OperatorNode(or_))
        formula_root.right.children.append(LiteralNode("A"))
        formula_root.right.children.append(LiteralNode("B"))

        self.assertTrue(is_tautology(formula_root))
    
    def test_tautology2(self):
        # AvB->A
        formula_root = OperatorNode(impl)
        formula_root.children.append(OperatorNode(or_))
        formula_root.children.append(LiteralNode("A"))
        formula_root.left.children.append(LiteralNode("A"))
        formula_root.left.children.append(LiteralNode("B"))
        
        self.assertFalse(is_tautology(formula_root))
