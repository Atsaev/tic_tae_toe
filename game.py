# game.py

from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()

    # Тут запускается основной цикл игры.
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)
                    draw_figures(game.board)
                # проверить на победу,
                    if game.check_win(current_player):
                        print(f'Победили {current_player}.')
                        game_winner.save_result(
                            'results.txt', f'Победили {current_player}.')
                        running = False
                    elif game.is_board_full():
                        print('Ничья!')
                        game_winner.save_result('results.txt', 'Ничья!')
                        running = False
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
