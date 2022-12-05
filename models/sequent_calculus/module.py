import dearpygui.dearpygui as dpg
from constants import DATA_PATH
from models.module import Module
from models.sequent_calculus.exam import SequentCalculusExam


class SequentCalculusModule(Module):
    name = "Sequent Calculus"
    folder = f"{DATA_PATH}/module3"
    exam_class = SequentCalculusExam

    def render(self):
        wrap = dpg.get_viewport_client_width() * 0.95
        dpg.add_text(self.contents[0], wrap=wrap)

        super().render()
