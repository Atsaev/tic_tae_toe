# gameparts/parts.py

class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def check_win(self, player):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return f'{player} выиграл!'
        for col in range(self.field_size):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return f'{player} выиграл!'

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return f'{player} выиграл!'

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return f'{player} выиграл!'

        return False

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
