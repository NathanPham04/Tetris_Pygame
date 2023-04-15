import game_logic

def _print_board(game_state: game_logic.ColumnsGameState) -> None:
    """Will print out the board according to a game state"""
    board = game_state.board
    columns = game_state.get_columns()
    rows = game_state.get_rows()
    for row in range(2, rows):
        print("|", end="")
        for col in range(columns):
            print(f' {board[col][row].val} ', end="")
        print("|")
    lower_line = "-" * 3 * columns
    print(f" {lower_line} ")


def _initial_input() -> game_logic.ColumnsGameState:
    """This will take in the initial input of
    board size, columns, contents
    and then will print the board accordingly"""
    game = game_logic.ColumnsGameState()
    ready = input("READY? (YES OR NO): ")
    if ready == 'YES':
        _print_board(game)
        return game
    else:
        quit()

def run():
    try:
        game = _initial_input()
    except game_logic.GameOverError:
        print("GAME OVER")
        quit()


if __name__ == "__main__":
    run()
