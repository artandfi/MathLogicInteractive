import dearpygui.dearpygui as dpg


class Exam:
    folder = "Exam folder"
    task_classes = []

    def __init__(self):
        self.tasks = [task_class(f"{self.folder}/task{i+1}.txt", i+1) for i, task_class in enumerate(self.task_classes)]
    
    def render(self):
        for task in self.tasks:
            task.render()
    
    @property
    def score(self):
        return sum(task.score for task in self.tasks)

    @property
    def max_score(self):
        return sum(task.max_score for task in self.tasks)
