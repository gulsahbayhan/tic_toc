# Tic-Tac-Toe — 5-Stage Implementation Plan

## Context
`tic_tac_toe.py` currently holds only placeholder functions (`blabla`, `blablabla`) and a `__main__` block that prints a welcome line. The pseudocode lives in `psudocode_example.md` (note: not `pseudocode.md`). Goal: turn that pseudocode into a working two-player CLI game, built in 5 stages that each leave the script runnable with `uv run python tic_tac_toe.py`.

**Rules for all code:** names below (agreed), docstring on every function, 4–10 body lines per function, beginner-friendly Python (lists, loops, if/else, `all()`), no classes. Python 3.13.

**Board model:** a list of 9 strings, starting `["1", "2", ..., "9"]`. A square is taken when it holds `"X"` or `"O"`. Position `p` (1–9) maps to index `p - 1`.

**Repo copy of the plan:** this file (`PLAN.md`).

## Function map (final)
| Function | Pseudocode block | Stage |
|---|---|---|
| `display_board(board)` | OUTPUT board | 1 |
| `print_welcome()` *(helper)* | 1 – welcome + rules (board is shown by `play_turn`) | 1 → 2 |
| `play_game()` | 3 + 4 – variables + main loop | 1 → grows each stage |
| `choose_symbols()` → `(player1, player2)` | 2 – choose symbols | 2 |
| `get_current_player(move_count, p1, p2)` | `move_count MOD 2` | 2 |
| `get_move(board, player)` → `int` | PROMPT / INPUT position | 2 (validated in 5) |
| `place_move(board, position, symbol)` | PLACE symbol | 2 |
| `play_turn(board, player)` *(helper)* | display + get + place | 2 |
| `check_winner(board, symbol)` → `bool` | 3 in a row | 3 |
| `check_draw(move_count)` → `bool` | `move_count == 9` | 4 |
| `is_game_over(board, symbol, move_count)` *(helper)* | win/draw messages | 3 → 4 |
| `is_valid_move(board, position_text)` → `bool` | taken / not 1–9 | 5 |

The three *(helper)* names are extra; they exist only to keep `play_game` under the 10-line limit.

## Stage 1 — Board + display
- Delete `blabla` / `blablabla`.
- `display_board(board)`: print 3 rows like ` X | 2 | O ` with `---+---+---` separators.
- `print_welcome(board)`: print welcome, short rules (“pick 1–9, 3 in a row wins”), then `display_board(board)`. *(Stage 2: dropped the board param and display — `play_turn` shows the board, avoiding a double print.)*
- `play_game()`: create board, call `print_welcome(board)`.
- `__main__`: call `play_game()`.
- **Check:** run script → welcome, rules, numbered empty grid.

## Stage 2 — Turn-taking
- `choose_symbols()`: `input()` X or O for Player 1, uppercase it, return `("X","O")` or `("O","X")`.
- `get_current_player`: return `p1` if `move_count % 2 == 0` else `p2`.
- `get_move`: `int(input(f"Player {player}, choose 1-9: "))` (no validation yet).
- `place_move`: `board[position - 1] = symbol`.
- `play_turn`: `display_board` → `get_move` → `place_move`.
- `play_game`: add `move_count`, `game_over`, `while not game_over` loop; temporarily `game_over = move_count == 9`.
- **Check:** players alternate, symbols appear, game stops after 9 moves.

## Stage 3 — Win detection
- Module constant `WIN_LINES`: the 8 index triples (3 rows, 3 cols, 2 diagonals).
- `check_winner(board, symbol)`: loop `WIN_LINES`, return True if `all(board[i] == symbol for i in line)`.
- `is_game_over`: if winner → show final board, print “X wins the game!”, return True; else return False.
- `play_game`: `game_over = is_game_over(board, player, move_count)`.
- **Check:** play a row, a column, a diagonal → correct winner announced, loop ends.

## Stage 4 — Draw detection
- `check_draw(move_count)`: return `move_count == 9`.
- `is_game_over`: after the win check, `elif check_draw(...)` → final board + “It's a draw!”, return True. Removes the Stage 2 temporary stop.
- **Check:** play a full board with no line → draw message; a win on move 9 still reports a win.

## Stage 5 — Input validation
- `is_valid_move(board, position_text)`: False unless `position_text.isdigit()`, `1 <= int(...) <= 9`, and the square isn't `"X"`/`"O"`.
- `get_move`: loop `input()` until `is_valid_move`, printing “Invalid move, try again.” otherwise; return `int`.
- `choose_symbols`: re-ask until answer is `X` or `O`.
- **Check:** enter `abc`, `0`, `10`, empty, an occupied square, `x` lowercase → re-prompts, never crashes.

## Process
After each stage: run the game manually, verify the stage's check, count lines per function (4–10 body lines, excluding docstring), then pause for your OK before the next stage. Only Stage 1 is implemented after this plan is approved.
