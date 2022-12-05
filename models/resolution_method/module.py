import dearpygui.dearpygui as dpg
from constants import DATA_PATH
from models.module import Module
from models.resolution_method.exam import ResolutionMethodExam


class ResolutionMethodModule(Module):
    name = "Resolution Method"
    folder = f"{DATA_PATH}/module4"
    exam_class = ResolutionMethodExam

    def render(self):
        wrap = dpg.get_viewport_client_width() * 0.95
        dpg.add_text(self.contents[0], wrap=wrap)
        
        super().render()
