from unittest import TestCase
from models.task import Task
from models.exam import Exam
from models.module import Module


class TestModels(TestCase):
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
