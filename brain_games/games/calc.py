#!/usr/bin/env python3
import random
import operator

GAME_RULES = 'What is the result of the expression?'


def get_question_and_answer():
    """
    Calculator game
    Player get two numbers and an operator
    He need to calculate the result
    """
    num1, num2 = random.randint(0, 100), random.randint(0, 100)
    operations = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    )
    operation_name, operation_method = random.choice(operations)
    correct_answer = operation_method(num1, num2)
    return f'{num1} {operation_name} {num2}', str(correct_answer)
