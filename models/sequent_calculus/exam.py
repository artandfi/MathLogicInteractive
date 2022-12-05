from constants import DATA_PATH
from models.exam import Exam
from models.sequent_calculus.tasks import SequentTreeRandomTask


class SequentCalculusExam(Exam):
    folder = f"{DATA_PATH}/module3"
    description = ""
    task_classes = [SequentTreeRandomTask, SequentTreeRandomTask]
