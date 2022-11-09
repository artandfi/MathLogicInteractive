from unittest import TestCase
from task import Task
from test import Test
from module import Module


class TestModels(TestCase):
    def setUp(self):
        tasks = [
            Task(correct_answer=1, max_score=1.5),
            Task(correct_answer=1, max_score=2)
        ]
        test = Test(tasks=tasks)
        self.module = Module(test=test)
    
    def test_module_max_score(self):
        self.assertEqual(self.module.max_score, sum(task.max_score for task in self.module.test.tasks))

    def test_test_max_score(self):
        self.assertEqual(self.module.test.max_score, sum(task.max_score for task in self.module.test.tasks))
