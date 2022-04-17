class IllegalBoardPosition(Exception):
    def __init__(self, message):
        super().__init__(message)

class Board:
    """Representation of game board."""
    EMPTY_POSITION = '_'

    def __init__(self):
        self.board = ['_',"_","_","_","_","_","_","_","_"]

    def has_position_free(self):
        """Check if has any free position."""
        return "_" in set(self.board)
    
    def mark_on_position(self, character: str, position: int):
        """Set a character to position."""
        if position < 0 or position > 8:
            raise IllegalBoardPosition("Position doesn't exists.")
        if self.board[position] != "_":
            raise IllegalBoardPosition("Position already marked.")
        self.board[position] = character
    
    def print_board(self):
        for index, line in enumerate(self.board,1):
            print(f"{line}",end="")
            if index % 3 == 0:
                print("\n")
            else:
                print("", end="|")

    def get_positions_by_character(self, character: str):
        return [index if character == position else None for index, position in enumerate(self.board, 1)]
    
    def get_free_positions(self):
        return self.get_positions_by_character(Board.EMPTY_POSITION)
    
    def get_characts(self):
        player_characters = set(self.board) 
        player_characters.remove(Board.EMPTY_POSITION)
        return player_characters
