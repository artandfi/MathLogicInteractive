from pydantic import BaseModel
from typing import Any


class Task(BaseModel):
    description: str = ""
    correct_answer: Any
    max_score: float = 0.0
