import random


GAME = "Find the greatest common divisor of given numbers."


def play():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    return question, gcd(num1, num2)


def gcd(num1, num2):
    same_divider = []
    divider1 = []
    divider2 = []
    for i in range(1, num1):
        if num1 % i == 0:
            divider1.append(i)
    for i in range(1, num2):
        if num2 % i == 0:
            divider2.append(i)
    for i in divider1:
        for j in divider2:
            if i == j:
                same_divider.append(i)
                right_answer = max(same_divider)
    return right_answer
