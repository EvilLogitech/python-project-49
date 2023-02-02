#!/usr/bin/env python3
from brain_games.scripts.game_carcass import start_game
import brain_games.games.calc as game


def main():
    start_game(game.get_rules, game.make_game_step)


if __name__ == '__main__':
    main()
