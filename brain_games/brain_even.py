from random import randint
import prompt

def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')


def is_even(num):
    global correct_answer
    if num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"


def game():
    welcome_user()
    counter = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter < 3:
        num = randint(1, 100)
        print("Question: " , num)
        answer = input()
        is_even(num)
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            counter += 1
        print(f'Congratulations, {name}!')
