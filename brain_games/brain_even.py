from random import randint
import prompt

def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def is_even(num):
    global correct_answer
    if num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"


def game():
    counter = 0
    while counter < 3:
        num = randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print("Question: " , num)
        answer = input()
        is_even(num)
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        else:
            print("Correct!")
            counter += 1
    print(f'Congratulations, {name}!')
