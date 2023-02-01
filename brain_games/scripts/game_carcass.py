#!/usr/bin/env python3
import prompt


def stop_game(result, name, user_answer='', correct_answer=''):
    good_result = f'Congratulations, {name}!'
    bad_result = f"'{user_answer}' is wrong answer ;(. "
    bad_result += f"Correct answer was '{correct_answer}'.\n"
    bad_result += f"Let's try again, {name}!"
    print(good_result if result else bad_result)


def start_game(get_rules, make_a_step):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n{get_rules()}')
    count = 0
    game_res = False
    while count < 3:
        # Make step of game, get data
        game_step = make_a_step()
        res = prompt.string(f'Question: {game_step[0]}\nYour answer: ')
        if res == game_step[1]:
            count += 1
        else:
            stop_game(game_res, name, res, game_step[1])
            break
        if count == 3:
            game_res = True
            stop_game(game_res, name)
            break


def main():
    print(__name__)


if __name__ == '__main__':
    main()
