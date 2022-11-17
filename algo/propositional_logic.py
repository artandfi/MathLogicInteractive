import random
from string import ascii_uppercase
from collections import OrderedDict
from models.propositional_logic.formula_nodes import OperatorNode, LiteralNode
from models.operators import arity


def generate_propositional_formula_root(available_operators, operators_num, letters_num):
    available_letters = ascii_uppercase[:letters_num]
    literal_values = OrderedDict((letter, random.choice((True, False))) for letter in available_letters)
    
    root = _generate_propositional_formula_root(available_letters, available_operators, operators_num, literal_values)
    formula = root.formula

    for literal in available_letters:
        if literal not in formula:
            del literal_values[literal]
    
    root.literal_values = literal_values
    return root


def _generate_propositional_formula_root(available_letters, available_operators, operators_num, literal_values):
    if operators_num == 0:
        letter = random.choice(available_letters)
        value = literal_values[letter]
        return LiteralNode(letter, value)

    operator = random.choice(available_operators)
    node = OperatorNode(operator)
    operators_num_split = random.choice(all_number_splits_into_addends(operators_num-1, arity[operator]))

    for op_no in operators_num_split:
        subformula = _generate_propositional_formula_root(available_letters, available_operators, op_no, literal_values)
        node.children.append(subformula)
    
    return node


def all_number_splits_into_addends(number, addends_no, res=None, split=None):
    """
        Generates all possible splits of addends_no addends adding up to number.
    """
    if res is None:
        res = []
    if split is None:
        split = []
    
    if addends_no == 1:
        split.append(number)
        res.append(split)
    else:
        for i in range(0, number+1):
            split.append(i)
            n = len(split)
            all_number_splits_into_addends(number-i, addends_no-1, res, split[:])
            del split[n-1:]
    
    return res


def is_tautology(formula_root):
    pass
