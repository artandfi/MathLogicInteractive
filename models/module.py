import dearpygui.dearpygui as dpg
from models.exam import Exam


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
        dpg.add_text("Exam (test)")
        self.exam.render()

    @property
    def score(self):
        return self.exam.score

    @property
    def max_score(self):
        return self.exam.max_score
