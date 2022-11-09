from typing import List, Optional
from pydantic import BaseModel
from test import Test


class Module(BaseModel):
    readings: List[str] = []
    description: str = ""
    training_test: Optional[Test] = None
    test: Test

    @property
    def max_score(self):
        return self.test.max_score
