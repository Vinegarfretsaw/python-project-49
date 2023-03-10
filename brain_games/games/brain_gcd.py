import random
import math


RULE = "Find the greatest common divisor of given numbers."
MIN_NUM, MAX_NUM = 1, 100


def get_information():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    question = f'{num1} {num2}'
    right_answer = str(math.gcd(num1, num2))
    return question, right_answer
