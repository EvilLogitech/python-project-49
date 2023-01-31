#!/usr/bin/env python3
from brain_games.scripts.game_carcass import start_game
import brain_games.games.even as even


def play_game():
    start_game(even.get_rules, even.make_game_step)


def main():
    print(__name__)


if __name__ == '__main__':
    main()
