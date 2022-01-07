NUM_ROW = 6
NUM_COL = 7

class ConnectFourGame:

    def __init__(self, board, num_turns, game_won):
        self.board = board # 2d array
        self.num_turns = num_turns
        self.games_won = game_won

    def check_win(self):
        win = (self.check_hor_win() | self.check_ver_win() | self.check_lDiag_win() | self.check_rDiag_win())
        if win:
            self.games_won += 1
        return win

    def check_hor_win(self):
        for j in range(NUM_ROW - 3):
            for i in range(NUM_COL):
                if self.board[i][j] == self.board[i][j+1] and self.board[i][j+1] == self.board[i][j+2] and self.board[i][j+2] == self.board[i][j+3]:
                    return True
        return False

    def check_ver_win(self):
        for i in range(NUM_COL - 3):
            for j in range(NUM_ROW):
                if self.board[i][j] == self.board[i+1][j] and self.board[i+1][j] == self.board[i+2][j] and self.board[i+2][j] == self.board[i+3][j]:
                    return True
        return False

    def check_lDiag_win(self):
        for i in range(3, NUM_COL):
            for j in range(3, NUM_ROW):
                if self.board[i][j] == self.board[i-1][j-1] and self.board[i-1][j-1] == self.board[i-2][j-2] and self.board[i-2][j-2] == self.board[i-3][j-3]:
                    return True
        return False

    def check_rDiag_win(self):
        for i in range(3, NUM_COL):
            for j in range(NUM_ROW-3):
                if self.board[i][j] == self.board[i-1][j+1] and self.board[i-1][j+1] == self.board[i-2][j+2] and self.board[i-2][j+2] == self.board[i-3][j+3]:
                    return True
        return False

