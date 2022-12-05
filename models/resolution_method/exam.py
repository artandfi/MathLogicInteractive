from constants import DATA_PATH
from models.exam import Exam
from models.resolution_method.tasks import ResolutionMethodPredefinedTask


class ResolutionMethodExam(Exam):
    folder = f"{DATA_PATH}/module4"
    description = ""
    task_classes = [ResolutionMethodPredefinedTask, ResolutionMethodPredefinedTask]
