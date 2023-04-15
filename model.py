import game_logic
import sample_shell
import random


class ColumnGame:
    def __init__(self) -> None:
        self._game = game_logic.ColumnsGameState()
        self._matches = set()
        self.randomizer = game_logic.Randomizer(self._game)
        self.faller = self.randomizer.create_random_faller()
        self._score = 0


    def play_game(self) -> None:
        try:
            self.faller.drop_faller()
        except game_logic.NewFallerNeededError:
            self._score += self._game.remove_matches()
            self.faller = self.randomizer.create_random_faller()