from pydantic import BaseModel
from typing import List
from models.task import Task


class Exam(BaseModel):
    description: str = ""
    tasks: List[Task]

    @property
    def max_score(self):
        return sum(task.max_score for task in self.tasks)
