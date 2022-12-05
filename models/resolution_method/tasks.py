import dearpygui.dearpygui as dpg
from models.task import PredefinedTask


class ResolutionMethodPredefinedTask(PredefinedTask):
    def render(self):
        super().render()
        self.answer_input = dpg.add_combo(items=self.answer_options, default_value=self.answer_options[0])
