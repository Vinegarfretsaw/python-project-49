from random import randint


GAME = 'Answer "yes" if the number is even, otherwise answer "no".' 


def play():
    num = randint(1, 100)
    question = f'{num}'
    if is_even(num) is True:
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
