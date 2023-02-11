#!/usr/bin/env python3
from brain_games.game_carcass import start_game
import brain_games.games.even as game


def main():
    start_game(game.GAME_RULES, game.game_round)


if __name__ == '__main__':
    main()
