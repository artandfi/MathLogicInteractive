from pydantic import BaseModel
from typing import List
from task import Task


class Test(BaseModel):
    description: str = ""
    tasks: List[Task]

    @property
    def max_score(self):
        return sum(task.max_score for task in self.tasks)