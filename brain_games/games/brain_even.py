from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM, MAX_NUM = 0, 100


def information():
    num = randint(MIN_NUM, MAX_NUM)
    question = f'{num}'
    if is_even(num):
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
