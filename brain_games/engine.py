import prompt


WIN = 3


def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.GAME)
    counter = 0
    while counter < WIN:
        question, right_answer = game.play()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != str(right_answer):
            print(f"'{answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            counter += 1
    if counter == WIN:
        print(f"Congratulations, {name}!")
