from player import Player
from board import IllegalBoardPosition
from possibilities  import POSSIBILITIES


class GamePlay:

    def __init__(self, board):
        self.is_first_player = True
        self.board = board
        self.is_finish = False
        self.player1 = Player("Player 1", character="X")
        self.player2 = Player("Player 2", character="O")
    
    def do_mark(self):
        is_invalid_chioce = True #flag for enter on loop
        while(is_invalid_chioce):
            is_invalid_chioce = False
            choice = int(input("Choose an position from 1 to 9: ") or "11")

            try:
                player = self.get_player_turn()
                self.board.mark_on_position(character=player.character, position=choice -1)
                player.update_possibilities(board=self.board)
                self.board.print_board()

                if not self.has_winner_or_tie():
                    self.change_player()
            except IllegalBoardPosition as err:
                print(err)
                is_invalid_chioce = True

    def get_player_turn(self):
        return self.player1 if self.is_first_player else self.player2
    
    def has_winner_or_tie(self):
        if self.is_winner():
            print(f"|<>| -- {self.get_player_turn()} WIN -- |<>|")
            self.is_finish = True
        if self.is_tie():
            print("|<>| -- GAVE TIE -- |<>|")
            self.is_finish = True
        return self.is_finish

    def is_winner(self) -> bool:
        player = self.get_player_turn()
        marked = self.board.get_positions_by_character(player.character)
        for possibility in player.possibilities:
            if len(possibility.intersection(marked)) == 3:
                return True
        return False
    


    def is_tie(self):
        return not self.board.has_position_free()

    def change_player(self):
        self.is_first_player = not self.is_first_player
