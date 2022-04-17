from board import Board
from gameplay import GamePlay

def main():
    active_game_loop = True
    game_play = GamePlay(Board())

    while(active_game_loop):
        game_play.do_mark()
        if game_play.is_finish:
            active_game_loop = False

if __name__ == "__main__":
    main()