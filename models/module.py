from typing import List, Optional
from pydantic import BaseModel
from models.exam import Exam


class Module(BaseModel):
    readings: List[str] = []
    description: str = ""
    training_test: Optional[Exam] = None
    exam: Exam

    @property
    def max_score(self):
        return self.exam.max_score
