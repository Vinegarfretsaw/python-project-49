import random


GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM, MAX_NUM = 2, 100


def play():
    num = random.randint(MIN_NUM, MAX_NUM)
    question = f'{num}'
    if is_prime(num):
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
