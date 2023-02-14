import random

GAME = "What number is missing in the progression?"

def play():
    num1 = random.randint(1, 10)
    num2 = random.randint(90, 100)
    step = random.randint(1, 10)
    question = f'{progression}'
    return question, progression(num1, num2, step), right_answer()


def progression(num1, num2, step):
    progression = []
    for i in range(num1, num2, step):
        progression.append(i)
    progression.sort()
    return progression

def right_answer():
    right_answer = []
    for _ in progression:
        right_answer = random.choice(progression.index)
        break
    for _ in right_answer:
        right_answer = '..'
    return right_answer