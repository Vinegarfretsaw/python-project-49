import random


RULE = "What is the result of the expression?"
MIN_NUM, MAX_NUM = 0, 10


def get_information():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    operation = random.choice(['+', '-', '*'])
    num2 = random.randint(MIN_NUM, MAX_NUM)
    question = f'{num1} {operation} {num2}'
    return question, calculate(num1, num2, operation)


def calculate(num1, num2, operation):
    while True:
        if operation == '0':
            break
        if operation not in ['+', '-', '*']:
            continue
        else:
            if operation == '+':
                right_answer = num1 + num2
            elif operation == '-':
                right_answer = num1 - num2
            elif operation == '*':
                right_answer = num1 * num2
            return str(right_answer)
        