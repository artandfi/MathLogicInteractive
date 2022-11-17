from constants import DATA_PATH
from models.exam import Exam
from models.propositional_logic.tasks import (
    EvaluateFormulaRandomTask,
    ParenthesesRandomTask,
    TautologyPredefinedTask,
    TautologyRandomTask,
    TautologicalConsequenceRandomTask
)


class PropositionalLogicExam(Exam):
    folder = f"{DATA_PATH}/module1"
    description = ""
    task_classes = [
        EvaluateFormulaRandomTask,
        ParenthesesRandomTask,
        TautologyPredefinedTask,
        TautologyRandomTask,
        TautologicalConsequenceRandomTask
    ]
