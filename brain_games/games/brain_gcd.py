import random
import math


GAME = "Find the greatest common divisor of given numbers."


def play():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    right_answer = math.gcd(num1, num2)
    return question, right_answer
