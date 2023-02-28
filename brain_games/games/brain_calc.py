import random


RULE = "What is the result of the expression?"
MIN_NUM, MAX_NUM = 0, 10


def information():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    operation = random.choice(['+', '-', '*'])
    num2 = random.randint(MIN_NUM, MAX_NUM)
    question = f'{num1} {operation} {num2}'
    return question, calculate(num1, num2, operation)


def calculate(num1, num2, operation):
    try:
        if operation == '+':
            right_answer = num1 + num2
        if operation == '-':
            right_answer = num1 - num2
        if operation == '*':
            right_answer = num1 * num2
        return str(right_answer)
    except UnboundLocalError:
        return "Input data outside specified conditions"
