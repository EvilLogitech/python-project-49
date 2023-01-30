#!/usr/bin/env python3
import prompt
import random

def get_number():
    return random.randint(0, 100)
    

def is_even(num):
    return True if num %2 == 0 else False


def game():
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}\nAnswer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        num = get_number()
        correct_answer = 'yes' if is_even(num) else 'no'
        res = prompt.string(f'Question: {num}\nYour answer: ')
        if res == correct_answer:
            count += 1
        else:
            print(f"""'{res}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!""")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    game()


if __name__ == '__main__':
    main()
