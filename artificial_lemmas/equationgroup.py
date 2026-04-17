import random
from operationtree import *


def random_correct_bracket_sequence(n_types, pairs, brackets=None):
    if brackets is None:
        brackets = [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]
    if n_types > len(brackets):
        raise ValueError("Not enough bracket types provided")

    brackets = brackets[:n_types]

    result = []
    stack = []
    opens_left = pairs

    while opens_left > 0 or stack:
        # Decide whether to open or close
        if opens_left == 0:
            # must close
            open_br, close_br = stack.pop()
            result.append(close_br)
        elif not stack:
            # must open
            open_br, close_br = random.choice(brackets)
            stack.append((open_br, close_br))
            result.append(open_br)
            opens_left -= 1
        else:
            # choose randomly
            if random.random() < 0.5:
                open_br, close_br = random.choice(brackets)
                stack.append((open_br, close_br))
                result.append(open_br)
                opens_left -= 1
            else:
                open_br, close_br = stack.pop()
                result.append(close_br)

    return result


def create_brackets (n_types) -> list:
    brackets = []
    for i in range(n_types):
        brackets.append((f'x{i}', f'X{i}'))
    return brackets

def print_brackets(n_types) -> str:
    brackets = create_brackets(n_types)
    out_str = '{G : Group}('
    for bracket in brackets:
        out_str += bracket[0] + ' '
    out_str += ': G)'
    return out_str

def trivial_free_group_element(n_types, bound_length : int = 100):
    pairs = random.randint(1, bound_length)
    return random_correct_bracket_sequence(n_types, pairs, brackets=create_brackets(n_types))

def random_split_trivial_element(trivial_element: list):
    split_index = random.randint(0, len(trivial_element) - 1)
    left = trivial_element[:split_index]
    right = trivial_element[split_index:]
    right.reverse()
    inverse = list(map(lambda x : x[0].swapcase() + x[1:], right))
    return left, inverse

# with standard letter names
def create_random_group_equation_std(n_types : int, bound_length : int= 100) -> str:
    trivial_element = trivial_free_group_element(n_types = n_types, bound_length = bound_length)
    left_part, right_part = random_split_trivial_element(trivial_element)
    # at this point, in the free group there is an equation left_part = right_part

    left_tree = random_group_tree(left_part)
    right_tree = random_group_tree(right_part)
    left_expression  = tree_to_expression(left_tree) if left_tree else "G.ide"
    right_expression = tree_to_expression(right_tree) if right_tree else "G.ide"
    return f"{left_expression} = {right_expression}"

def create_random_arend_group_proof(n_types : int, bound_length : int = 100, index: int = 0) -> str:
    equation = create_random_group_equation_std(n_types = n_types, bound_length = bound_length)
    st =  r'''\lemma grequation''' + str(index) +  print_brackets(n_types) + ': ' + equation + ' => equation.group'
    return st
