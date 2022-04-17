from board import Board

from possibilities import POSSIBILITIES
class Player:
    def __init__(self, name: str, character: str):
        self.possibilities = POSSIBILITIES
        self.name = name
        self.character = character
    
    def update_possibilities(self, board: Board):
        temp_possibilities = []
        enemy_moviments =self._get_enemy_moviments(board)
        
        for possibility in self.possibilities:
            set_posibility = set(list(possibility))
            if not set_posibility.intersection(enemy_moviments):
                temp_possibilities.append(possibility)
        self.possibilities = temp_possibilities
    
    def _get_enemy_character(self, board):
        enemy_char = board.get_characts()
        enemy_char.remove(self.character)
        if not enemy_char:
            return None
        return list(enemy_char)[0]


    def _get_enemy_moviments(self, board):
        enemy_char = self._get_enemy_character(board)
        enemy_moviments = set(board.get_positions_by_character(enemy_char))
        enemy_moviments.remove(None)
        return enemy_moviments


    def __str__(self) -> str:
        return self.name