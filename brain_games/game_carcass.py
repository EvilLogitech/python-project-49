#!/usr/bin/env python3
import prompt

rounds_count = 3


def start_game(game_rules, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n{game_rules}')
    for _ in range(rounds_count):
        # Make step of game, get data
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return None
        print("Correct!")
    print(f'Congratulations, {name}!')
