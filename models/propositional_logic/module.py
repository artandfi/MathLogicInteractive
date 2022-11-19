import dearpygui.dearpygui as dpg
from constants import DATA_PATH
from models.module import Module
from models.propositional_logic.exam import PropositionalLogicExam


class PropositionalLogicModule(Module):
    name = "Propositional Logic"
    folder = f"{DATA_PATH}/module1"
    exam_class = PropositionalLogicExam

    def render(self):
        wrap = dpg.get_viewport_client_width() * 0.95
        dpg.add_text(self.contents[0], wrap=wrap)
        
        labels = ["Negation", "Disjunction", "Conjunction", "Implication", "Equivalence"]
        headers_list = [
            ["A", "~A"],
            ["A", "B", "AVB"],
            ["A", "B", "A&B"],
            ["A", "B", "A->B"],
            ["A", "B", "A<->B"]
        ]
        cells_list = [
            [["T", "F"], ["F", "T"]],
            [["T", "T", "T"], ["T", "F", "T"], ["F", "T", "T"], ["F", "F", "F"]],
            [["T", "T", "T"], ["T", "F", "F"], ["F", "T", "F"], ["F", "F", "F"]],
            [["T", "T", "T"], ["T", "F", "F"], ["F", "T", "T"], ["F", "F", "T"]],
            [["T", "T", "T"], ["T", "F", "F"], ["F", "T", "F"], ["F", "F", "T"]]
        ]

        for label, headers, cells in zip(labels, headers_list, cells_list):
            self._fill_table(label, headers, cells)

        dpg.add_text(self.contents[1], wrap=wrap)
        super().render()
    
    def _fill_table(self, label, headers, cells):
        with dpg.table(
            label=label,
            header_row=True,
            borders_innerV=True,
            borders_outerV=True,
            borders_innerH=True,
            borders_outerH=True,
            no_host_extendX=True,
            policy=dpg.mvTable_SizingFixedFit
        ):
            for header in headers:
                dpg.add_table_column(label=header)
            
            for row in cells:
                with dpg.table_row():
                    for cell in row:
                        dpg.add_text(cell)
