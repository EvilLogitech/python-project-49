#!/usr/bin/env python3
from brain_games.scripts.game_carcass import start_game
import brain_games.games.progression as progression


def play_game():
    start_game(progression.get_rules, progression.make_game_step)


def main():
    print(__name__)


if __name__ == '__main__':
    main()
