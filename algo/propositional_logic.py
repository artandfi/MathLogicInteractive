import random
from string import ascii_uppercase
from collections import OrderedDict
from itertools import groupby, product
from models.propositional_logic.formula_nodes import OperatorNode, LiteralNode
from models.operators import arity


def generate_propositional_formula_root(available_operators, operators_num, letters_num):
    """
        Generates a random propositional formula and returns the root node of its syntax tree.
        
        Args:
            available_operators (Iterable): List of operators that may be included in formula.
            operators_num (int): Number of available operators to include in formula.
            letters_num (int): Number of first letters of the alphabet to include in formula.
        Returns:
            OperatorNode
    """
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
    """
        Utility function for recursion in generate_propositional_formula_root.
        Shouldn't be called directly elsewhere.

        Args:
            available_letters (Iterable): Letters that are available to be used as literals.
            available_operators (Iterable): List of operators that may be included in formula.
            operators_num (int): Number of available operators to include in formula.
            literal_values (OrderedDict[str, bool]): Ordered dictionary of boolean values that correspond to literals. 
    """
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
        Generates all possible splits of non-negative terms adding up to a non-negative number.

        Args:
            number (int): A non-negative number to generate splits of.
            addends_no (int): Number of addends to split the number to.
            res (Optional[int]): Utility argument for result, should NOT be specified when calling.
            split (Optional[List[int]]): Utility argument for split, should NOT be specified when calling.
        Returns:
            List[int]
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


def is_tautology(formula_root: OperatorNode):
    """
        Determines whether a propositional formula represented by the root of its syntax tree is a tautology.

        Args:
            formula_root (OperatorNode): The root of the propositional formula to be checked for being a tautology.
        Returns:
            bool
    """
    literal_groups = sorted(formula_root.leaves, key=str)
    literal_groups = [list(group) for _, group in groupby(literal_groups)]
    cached_values = [group[0].value for group in literal_groups]

    for values in product((True, False), repeat=len(literal_groups)):
        _fill_literal_values(literal_groups, values)
        
        if not formula_root.value:
            _fill_literal_values(literal_groups, cached_values)
            return False
    
    _fill_literal_values(literal_groups, cached_values)
    return True


def _fill_literal_values(literal_groups, values):
    """
        Utility function for filling the literal values in is_tautology function.
        Shouldn't be called directly elsewhere.

        Args:
            literal_groups (Iterable[Iterable[str]]): The groups of the literals.
            values (Iterable[bool]): The values to be assigned to literals in the groups. 
    """
    for literal_group, value in zip(literal_groups, values):
        for literal in literal_group:
            literal.value = value
