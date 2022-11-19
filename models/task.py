import re
import dearpygui.dearpygui as dpg
from models.operators import operator_strings


class Task:
    def __init__(self, path, number):
        self.path = path
        self.number = number
        self.correct_answer = None
        self.answer_input = None
        self._load_contents()
    
    def _load_contents(self):
        with open(self.path, "r") as f:
            self._contents = [line.strip() for line in f.readlines()]
            
        self.description = self._contents[1]
        self.max_score = float(self._contents[2])
    
    def render(self):
        dpg.add_text(f"{self.number}. {self.description}")
    
    @property
    def score(self):
        return self.max_score if self.correct_answer == dpg.get_value(self.answer_input) else 0
        

class PredefinedTask(Task):
    def _load_contents(self):
        super()._load_contents()

        self.answer_options = self._contents[3].split(", ")
        correct_answer = list(filter(re.compile(r"\*.+").match, self.answer_options))[0]
        i = self.answer_options.index(correct_answer)
        correct_answer = correct_answer[1:]
        self.answer_options[i] = correct_answer
        self.correct_answer = correct_answer


class RandomTask(Task):
    def _load_contents(self):
        super()._load_contents()

        strings_to_operators = dict((v, k) for k, v in operator_strings.items())
        self.operators = [strings_to_operators[s] for s in self._contents[3].split(", ")]
        self.operators_num = int(self._contents[4])
        self.letters_num = int(self._contents[5])
        self.answer_options = self._contents[6].split(", ")
        self.correct_answer = None
