import random


RULE = "What number is missing in the progression?"
MIN_START, MAX_START = 1, 10
MIN_STEP, MAX_STEP = 2, 10
MIN_LENGTH, MAX_LENGTH = 5, 10


def get_information():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = get_progression(start, length, step)
    random_index = random.randint(0, length - 1)
    right_answer = str(progression[random_index])
    progression[random_index] = '..'
    final_progression = ' '.join(map(str, progression))
    question = f'{final_progression}'
    return question, right_answer


def get_progression(start, length, step):
    progression = []
    finish = start + step * length
    for i in range(start, finish, step):
        progression.append(i)
    progression.sort()
    return progression
