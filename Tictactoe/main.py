class TicTacToe:
    def __init__(self):
        self.board = [" " for x in range(9)]
        self.player = "X"
        self.winner = None

    def draw_board(self):
        print(" %c | %c | %c " % (self.board[0], self.board[1], self.board[2]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[3], self.board[4], self.board[5]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[6], self.board[7], self.board[8]))
        print("   |   |   ")

    def player_move(self):
        print(self.player + "'s move")
        choice = int(input("Enter your move (1-9): ").strip())
        if self.board[choice - 1] == " ":
            self.board[choice - 1] = self.player
        else:
            print("That space is occupied!")
            self.player_move()

    def check_for_winner(self):
        for x in range(0, 3):
            y = x * 3
            if (self.board[y] == self.board[(y + 1)] == self.board[(y + 2)]) and self.board[y] != " ":
                self.winner = self.board[y]
                print(self.winner + " won!")
                return True

        for x in range(3):
            if (self.board[x] == self.board[(x + 3)] == self.board[(x + 6)]) and self.board[x] != " ":
                self.winner = self.board[x]
                print(self.winner + " won!")
                return True

        if (self.board[0] == self.board[4] == self.board[8]) and self.board[0] != " ":
            self.winner = self.board[0]
            print(self.winner + " won!")
            return True

        if (self.board[2] == self.board[4] == self.board[6]) and self.board[2] != " ":
            self.winner = self.board[2]
            print(self.winner + " won!")
            return True

    def switch_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def main(self):
        self.draw_board()
        while not self.check_for_winner():
            self.player_move()
            self.draw_board()
            self.check_for_winner()
            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.main()
