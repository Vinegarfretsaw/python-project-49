import random


GAME = "What is the result of the expression?"


def play():
    num1 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    num2 = random.randint(1, 10)
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
