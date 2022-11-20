import os
import json
from callbacks import reset_progress
from models.task import Task
from models.exam import Exam
from models.module import Module


tmp_path = "tmp.json"


class TaskMock(Task):
    def __init__(self, path, number):
        pass
    
    @property
    def score(self):
        return 1


class ExamMock(Exam):
    def __init__(self):
        pass


class ModuleMock(Module):
    progress_file_path = tmp_path

    def __init__(self):
        self.name = "mock"


def test_save_progress():
    module = ModuleMock()
    module.exam = ExamMock()
    module.exam.tasks = [TaskMock("", 1), TaskMock("", 2)]

    prior_data = {
        "mock": {
            "scores": [0, 0],
            "completed": False
        }
    }
    saved_data = {
        "mock": {
            "scores": [1, 1],
            "completed": True
        }
    }

    try:
        with open(tmp_path, "w+") as f:
            json.dump(prior_data, f)

        module.save_progress()
        
        with open(tmp_path, "r") as f:
            data = json.load(f)

        assert data == saved_data
    finally:
        os.remove(tmp_path)


def test_reset_progress():
    modules = [ModuleMock()]
    data = {
        "mock": {
            "scores": [5, 5, 5],
            "completed": True
        }
    }
    reset_data = {
        "mock": {
            "scores": [0, 0, 0],
            "completed": False
        }
    }
    
    try:
        with open(tmp_path, "w+") as f:
            json.dump(data, f)

        reset_progress(modules, tmp_path)
        
        with open(tmp_path, "r") as f:
            data = json.load(f)

        assert data == reset_data
    finally:
        os.remove(tmp_path)
