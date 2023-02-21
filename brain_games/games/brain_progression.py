import random


GAME = "What number is missing in the progression?"
MIN_START, MAX_START = 1, 10
MIN_STEP, MAX_STEP = 2, 10
MIN_LENGTH, MAX_LENGTH = 5, 10


def play():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    return progression(start, length, step)


def progression(start, length, step):
    progression = []
    finish = start + step * length
    for i in range(start, finish, step):
        progression.append(i)
    progression.sort()
    random_index = random.randint(0, length - 1)
    right_answer = progression[random_index]
    progression[random_index] = '..'
    final_progression = ' '.join(map(str, progression))
    question = f'{final_progression}'
    return question, right_answer
