#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}')


if __name__ == '__main__':
    welcome_user()
    