import random

GAME = "What number is missing in the progression?"

def play():
    start = random.randint(1, 10)
    step = random.randint(2, 10)
    length = random.randint(5, 10)
    question, right_answer = progression(start, length, step)
    return question, right_answer

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
    return final_progression, right_answer