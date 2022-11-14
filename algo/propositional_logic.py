import random
from string import ascii_uppercase
from models.propositional_formula import OperatorNode, LiteralNode
from models.operators import arity


def generate_propositional_formula(available_operators, operators_num, letters_num):
    if operators_num == 0:
        letter = random.choice(ascii_uppercase[:letters_num])
        value = random.choice((True, False))

        return LiteralNode(letter, value)

    operator = random.choice(available_operators)
    node = OperatorNode(operator)
    operators_num_split = random.choice(all_number_splits_into_addends(operators_num-1, arity[operator]))

    for op_no in operators_num_split:
        subformula = generate_propositional_formula(available_operators, op_no, letters_num)
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
