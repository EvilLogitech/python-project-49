#!/usr/bin/env python3
import prompt


def stop_game(result, name, user_answer='', correct_answer=''):
    print(f'Congratulations, {name}!' if result else f"""'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!""")


def start_game(get_rules, make_a_step):
    name = prompt.string('May i have your name? ')
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
