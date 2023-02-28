import prompt


WIN = 3


def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.RULE)
    counter = 0
    while counter < WIN:
        question, right_answer = game.information()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            exit()
    print(f"Congratulations, {name}!")
