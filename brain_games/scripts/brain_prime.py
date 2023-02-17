#!/usr/bin/env python3
from brain_games.game_carcass import start_game
import brain_games.games.prime as game


def main():
    start_game(game.GAME_RULES, game.get_question_and_answer)


if __name__ == '__main__':
    main()
