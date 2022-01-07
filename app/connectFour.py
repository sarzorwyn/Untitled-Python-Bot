NUM_ROW = 6
NUM_COL = 7


class ConnectFour:

    def __init__(self, board, num_turns, active_player, game_won):
        self.board = board  # 2d array
        self.num_turns = num_turns  # number of turns to check if board filled
        self.active_player = active_player  # {1, 2}
        self.games_won = game_won  # tracks the score

    @staticmethod
    def new_game():
        """Creates a new empty board for a new game

        :return: a game object
        """
        board = [[0] * NUM_COL for i in range(NUM_ROW)]
        game = ConnectFour(board, 0, 0, 0)
        return game

    def board_to_emoji(self):
        """ Converts the game to superior emojis
        """
        twitterOutput = ''

        for row in range(NUM_ROW):
            for col in range(NUM_COL):
                if self.board[row][col] == 1:
                    twitterOutput += "🔴"  # red circle
                if self.board[row][col] == 2:
                    twitterOutput += "🔵"  # blue circle
                else:
                    twitterOutput += "⚪"  # white circle

            twitterOutput += '\n'  # new row new line

        twitterOutput += "1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣\n"

        twitterOutput += 'Player turn ▶ '
        if self.active_player == 1:
            twitterOutput += '🔴'  # red circle and right arrow

        else:
            twitterOutput += '🔵'  # blue circle and right arrow

        return twitterOutput

    def get_valid_moves(self):
        validCols = []

        for col in range(NUM_COL):
            if self.board[0][col] == 0:
                val = col + 1
                validCols.append(str(val))

        return validCols

    def check_win(self):
        """
        Checks if the current player won
        :return: True if player won. False otherwise.
        """
        win = (self.check_hor_win() | self.check_ver_win() | self.check_lDiag_win() | self.check_rDiag_win())
        return win

    def check_hor_win(self):
        """
        Checks for horizontal win condition
        :return: True if player won. False otherwise.
        """
        for j in range(NUM_COL - 3):
            for i in range(NUM_ROW):
                if self.board[i][j] != 0 and self.board[i][j] == self.board[i][j+1] and self.board[i][j+1] == self.board[i][j+2] and self.board[i][j+2] == self.board[i][j+3]:
                    return True
        return False

    def check_ver_win(self):
        """
        Checks for vertical win condition
        :return: True if player won. False otherwise.
        """
        for i in range(NUM_ROW - 3):
            for j in range(NUM_COL):
                if self.board[i][j] != 0 and self.board[i][j] == self.board[i+1][j] and self.board[i+1][j] == self.board[i+2][j] and self.board[i+2][j] == self.board[i+3][j]:
                    return True
        return False

    def check_lDiag_win(self):
        """
        Checks for left diagonal win condition
        :return: True if player won. False otherwise.
        """
        for i in range(3, NUM_ROW):
            for j in range(3, NUM_COL):
                if self.board[i][j] != 0 and self.board[i][j] == self.board[i-1][j-1] and self.board[i-1][j-1] == self.board[i-2][j-2] and self.board[i-2][j-2] == self.board[i-3][j-3]:
                    return True
        return False

    def check_rDiag_win(self):
        """
        Checks for right diagonal win condition
        :return: True if player won. False otherwise.
        """
        for i in range(3, NUM_ROW):
            for j in range(NUM_COL-3):
                if self.board[i][j] != 0 and self.board[i][j] == self.board[i-1][j+1] and self.board[i-1][j+1] == self.board[i-2][j+2] and self.board[i-2][j+2] == self.board[i-3][j+3]:
                    return True
        return False

    def play_turn(self, col):
        """
        Current player starts turn
        :param col: Player choice of column
        :return: True if player won. False otherwise.
        """

        self.active_player = (self.num_turns % 2) + 1
        self.num_turns += 1
        self.place_piece(int(col) - 1)
        if self.check_win():
            self.games_won += 1
            return True
        return False

    def place_piece(self, col):
        """
        Place a piece in the board.
        :param col: Player choice of column
        :return: True if valid. False otherwise
        """
        if self.board[0][col] != 0:
            return False
        for j in range(NUM_ROW):
            if self.board[j][col] != 0:
                break
        if self.board[j][col] != 0:
            self.board[j-1][col] = self.active_player
        else:
            self.board[j][col] = self.active_player
        return True

