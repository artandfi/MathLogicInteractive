import json
import dearpygui.dearpygui as dpg
from models.exam import Exam
from constants import PROGRESS_FILE


class Module:
    name = "Module name"
    folder = "Module folder"
    exam_class = Exam
    progress_file_path = PROGRESS_FILE

    def __init__(self):
        self.exam = self.exam_class()
        self._load_contents()

    def _load_contents(self):
        with open(f"{self.folder}/contents.txt") as f:
            self.contents = f.read().split("#")
        
        with open(PROGRESS_FILE, "r") as f:
            self.completed = json.load(f)[self.name]["completed"]
    
    def render(self):
        dpg.add_text()
        
        if not self.completed:
            dpg.add_text("Exam (test)")
            self.exam.render()
        else:
            dpg.add_text("You've already passed the exam!")
    
    def save_progress(self):
        with open(self.progress_file_path, "r") as f:
            data = json.load(f)
        
        data[self.name]["scores"] = [task.score for task in self.exam.tasks]
        data[self.name]["completed"] = True
        
        with open(self.progress_file_path, "w") as f:
            json.dump(data, f, indent=4)
    
    def refresh(self):
        self.exam = self.exam_class()
        self.completed = False

    @property
    def score(self):
        return self.exam.score

    @property
    def max_score(self):
        return self.exam.max_score
