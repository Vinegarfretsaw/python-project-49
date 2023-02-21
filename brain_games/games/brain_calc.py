import random


GAME = "What is the result of the expression?"
MIN_NUM, MAX_NUM = 0, 10


def play():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    operation = random.choice(['+', '-', '*'])
    num2 = random.randint(MIN_NUM, MAX_NUM)
    question = f'{num1} {operation} {num2}'
    return question, calc(num1, num2, operation)


def calc(num1, num2, operation):
    if operation == '+':
        right_answer = num1 + num2
    if operation == '-':
        right_answer = num1 - num2
    if operation == '*':
        right_answer = num1 * num2
    return right_answer
