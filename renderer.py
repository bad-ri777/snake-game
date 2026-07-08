from engine import GameState

BOARD_ROW_OFFSET = 1


def draw(stdscr, state: GameState) -> None:
    stdscr.clear()
    draw_score(stdscr, state)
    for row, col in state.snake:
        stdscr.addch(row + BOARD_ROW_OFFSET, col, "O")
    food_row, food_col = state.food
    stdscr.addch(food_row + BOARD_ROW_OFFSET, food_col, "*")
    stdscr.refresh()


def draw_score(stdscr, state: GameState) -> None:
    stdscr.addstr(0, 0, f"Score: {state.score}")


def draw_game_over(stdscr, state: GameState) -> None:
    stdscr.clear()
    message = f"Game Over! Score: {state.score}"
    row = state.height // 2 + BOARD_ROW_OFFSET
    col = max(state.width // 2 - len(message) // 2, 0)
    stdscr.addstr(row, col, message)
    stdscr.refresh()
