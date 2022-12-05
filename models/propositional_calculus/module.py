import dearpygui.dearpygui as dpg
from constants import DATA_PATH
from models.module import Module
from models.propositional_calculus.exam import PropositionalCalculusExam


class PropositionalCalculusModule(Module):
    name = "Predicate Calculus"
    folder = f"{DATA_PATH}/module2"
    exam_class = PropositionalCalculusExam

    def render(self):
        wrap = dpg.get_viewport_client_width() * 0.95
        dpg.add_text(self.contents[0], wrap=wrap)

        super().render()
