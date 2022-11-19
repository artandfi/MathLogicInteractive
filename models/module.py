import json
import dearpygui.dearpygui as dpg
from models.exam import Exam
from constants import PROGRESS_FILE


class Module:
    name = "Module name"
    folder = "Module folder"
    exam_class = Exam

    def __init__(self):
        self._load_contents()
        self.exam = self.exam_class()

    def _load_contents(self):
        with open(f"{self.folder}/contents.txt") as f:
            self.contents = f.read().split("#")
    
    def render(self):
        dpg.add_text()
        dpg.add_text("Exam (test)")
        self.exam.render()
    
    def save_progress(self):
        with open(PROGRESS_FILE, "r") as f:
            data = json.load(f)
        
        data[self.name]["scores"] = [task.score for task in self.exam.tasks]
        data[self.name]["completed"] = True
        
        with open(PROGRESS_FILE, "w") as f:
            json.dump(data, f, indent=4)

    @property
    def score(self):
        return self.exam.score

    @property
    def max_score(self):
        return self.exam.max_score
