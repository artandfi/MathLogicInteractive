from unittest import TestCase
from models.task import Task
from models.exam import Exam
from models.module import Module
from models.tree import Tree, TreeNode


class TestAssessmentModels(TestCase):
    def setUp(self):
        tasks = [
            Task(correct_answer=1, max_score=1.5),
            Task(correct_answer=1, max_score=2)
        ]
        exam = Exam(tasks=tasks)
        self.module = Module(exam=exam)
    
    def test_module_max_score(self):
        self.assertEqual(self.module.max_score, sum(task.max_score for task in self.module.exam.tasks))

    def test_exam_max_score(self):
        self.assertEqual(self.module.exam.max_score, sum(task.max_score for task in self.module.exam.tasks))


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
