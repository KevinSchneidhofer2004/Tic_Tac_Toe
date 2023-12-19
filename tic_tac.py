class Tic_Tac_Toe:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.board = []

    def create_board(self):
        for i in range(self.y_size):
            row = ["N"] * self.x_size
            self.board.append(row)

    def matrix_view(self):

        self.board.reverse()

        for row in self.board:
            print(row)

        for i in range(0, 25):
            print("-", end="")
        print()

        self.board.reverse()

    def check_field(self, x_coordinate, y_coordinate):
        if self.board[y_coordinate - 1][x_coordinate - 1] == "N":
            return True
        else:
            return False

    def check_win(self, element):
        for i in range(self.y_size):
            if all(cell == element for cell in self.board[i]) or \
               all(row[i] == element for row in self.board):
                return True

        if all(self.board[i][i] == element
               for i in range(min(self.x_size, self.y_size))) or \
                all(self.board[i][self.x_size - i - 1] == element
                    for i in range(min(self.x_size, self.y_size))):
            return True

        return False

    def check_draw(self, element):
        if self.check_win(element) is False:
            draw = all("N" not in sublist for sublist in self.board)
            if draw is True:
                return True
            else:
                return False

    def set_element(self, element, x_coordinate, y_coordinate):
        self.board[y_coordinate][x_coordinate] = element
        self.matrix_view()

    def restart(self):
        self.board = [["N" for i in row] for row in self.board]
