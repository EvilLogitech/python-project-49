#!/usr/bin/env python3
import prompt

NUMBER_OF_ROUNDS = 3


def stop_game(result, name, user_answer='', correct_answer=''):
    good_result = f'Congratulations, {name}!'
    bad_result = f"'{user_answer}' is wrong answer ;(. "
    bad_result += f"Correct answer was '{correct_answer}'.\n"
    bad_result += f"Let's try again, {name}!"
    print(good_result if result else bad_result)


def start_game(game_rules, make_a_step):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n{game_rules}')
    game_result = True
    for _ in range(NUMBER_OF_ROUNDS):
        # Make step of game, get data
        game_step = make_a_step()
        answer = prompt.string(f'Question: {game_step[0]}\nYour answer: ')
        if answer == game_step[1]:
            print("Correct!")
        else:
            game_result = False
            stop_game(game_result, name, answer, game_step[1])
            break
    if game_result:
        stop_game(game_result, name)
