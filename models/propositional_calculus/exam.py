from constants import DATA_PATH
from models.exam import Exam
from models.propositional_calculus.tasks import InferencePredefinedTask, TautologyTheoremPredefinedTask, TautologyTheoremRandomTask


class PropositionalCalculusExam(Exam):
    folder = f"{DATA_PATH}/module2"
    description = ""
    task_classes = [
        InferencePredefinedTask,
        InferencePredefinedTask,
        TautologyTheoremPredefinedTask,
        TautologyTheoremRandomTask
    ]
