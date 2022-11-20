import os
import json
from tempfile import NamedTemporaryFile
from callbacks import reset_progress
from models.module import Module


class ModuleMock(Module):
    def __init__(self):
        self.name = "mock"


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
    tmp_path = "tmp.json"
    
    try:
        with open(tmp_path, "w+") as f:
            json.dump(data, f)

        reset_progress(modules, tmp_path)
        
        with open(tmp_path, "r") as f:
            data = json.load(f)

        assert data == reset_data
    finally:
        os.remove(tmp_path)
