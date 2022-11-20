import re
import dearpygui.dearpygui as dpg
from models.operators import impl, operator_strings
from models.task import PredefinedTask, RandomTask
from models.propositional_logic.formula_nodes import OperatorNode
from algo.propositional_logic import generate_propositional_formula_root, is_tautology


class EvaluateFormulaRandomTask(RandomTask):
    def __init__(self, path, number):
        super().__init__(path, number)
        self.formula_root = generate_propositional_formula_root(self.operators, self.operators_num, self.letters_num)
        self.description = self.description.replace("#", self.formula_root.formula, 1)
        literal_values = [f"{literal} = {str(value)}" for literal, value in self.formula_root.literal_values.items()]

        self.description = self.description.replace("#", ", ".join(literal_values))
        self.correct_answer = str(self.formula_root.value)

    def render(self):
        super().render()
        self.answer_input = dpg.add_combo(items=self.answer_options, default_value=self.answer_options[0])


class ParenthesesRandomTask(RandomTask):
    def __init__(self, path, number):
        super().__init__(path, number)
        self.formula_root = generate_propositional_formula_root(self.operators, self.operators_num, self.letters_num)
        self.correct_answer = self.formula_root.formula
        formula_no_parens = re.sub(r"\(|\)", "", self.correct_answer)
        self.description = self.description.replace("#", formula_no_parens)
        
        impl_str = operator_strings[impl]
        impl_count = self.correct_answer.count(impl_str)
        self.correct_answer = f"{formula_no_parens.replace(impl_str, f'{impl_str}(', impl_count-1)}{')'*(impl_count-1)}"
        print(self.correct_answer)

    def render(self):
        super().render()
        self.answer_input = dpg.add_input_text()


class TautologyPredefinedTask(PredefinedTask):
    def render(self):
        super().render()
        self.answer_input = dpg.add_combo(items=self.answer_options, default_value=self.answer_options[0])


class TautologyRandomTask(RandomTask):
    def __init__(self, path, number):
        super().__init__(path, number)
        self.formula_root = generate_propositional_formula_root(self.operators, self.operators_num, self.letters_num)
        self.description = self.description.replace("#", self.formula_root.formula)
        self.correct_answer = "Yes" if is_tautology(self.formula_root) else "No"
    
    def render(self):
        super().render()
        self.answer_input = dpg.add_combo(items=self.answer_options, default_value=self.answer_options[0])


class TautologicalConsequenceRandomTask(RandomTask):
    def __init__(self, path, number):
        super().__init__(path, number)
        self.lhs_root = generate_propositional_formula_root(self.operators, self.operators_num, self.letters_num)
        self.rhs_root = generate_propositional_formula_root(self.operators, self.operators_num, self.letters_num)
        self.description = self.description.replace("#", self.lhs_root.formula, 1)
        self.description = self.description.replace("#", self.rhs_root.formula)
        self.formula_root = OperatorNode(impl)
        self.formula_root.children.append(self.lhs_root)
        self.formula_root.children.append(self.rhs_root)
        self.correct_answer = "Holds" if is_tautology(self.formula_root) else "Doesn't hold"
    
    def render(self):
        super().render()
        self.answer_input = dpg.add_combo(items=self.answer_options, default_value=self.answer_options[0])
