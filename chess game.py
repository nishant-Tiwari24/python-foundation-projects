class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = "white"

    def initialize_board(self):
        # Initialize an 8x8 board with pieces in their starting positions
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                if i == 0:
                    if j == 0 or j == 7:
                        row.append("rook_black")
                    elif j == 1 or j == 6:
                        row.append("knight_black")
                    elif j == 2 or j == 5:
                        row.append("bishop_black")
                    elif j == 3:
                        row.append("queen_black")
                    elif j == 4:
                        row.append("king_black")
                elif i == 1:
                    row.append("pawn_black")
                elif i == 6:
                    row.append("pawn_white")
                elif i == 7:
                    if j == 0 or j == 7:
                        row.append("rook_white")
                    elif j == 1 or j == 6:
                        row.append("knight_white")
                    elif j == 2 or j == 5:
                        row.append("bishop_white")
                    elif j == 3:
                        row.append("queen_white")
                    elif j == 4:
                        row.append("king_white")
                else:
                    row.append("empty")
            board.append(row)
        return board

    def print_board(self):
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(i+1, end=" ")
            for piece in row:
                if piece == "empty":
                    print("-", end=" ")
                else:
                    print(piece[0].upper(), end=" ")
            print()

    def is_valid_move(self, start, end):
        # Check if the move is valid (e.g. piece can move to that square)
        # This is a very basic implementation, you would need to add more rules
        start_x, start_y = start
        end_x, end_y = end
        piece = self.board[start_x-1][start_y-1]
        if piece == "empty":
            return False
        if piece.endswith(self.current_player):
            if piece.startswith("pawn"):
                # Pawns can move forward one square, but capture diagonally
                if start_x == end_x and abs(start_y - end_y) == 1:
                    return True
                elif start_y == end_y and abs(start_x - end_x) == 1:
                    return True
            elif piece.startswith("knight"):
                # Knights move in an L-shape
                if abs(start_x - end_x) == 2 and abs(start_y - end_y) == 1:
                    return True
                elif abs(start_x - end_x) == 1 and abs(start_y - end_y) == 2:
                    return True
            # Add more rules for other pieces
        return False

    def make_move(self, start, end):
        if self.is_valid_move(start, end):
            start_x, start_y = start
            end_x, end_y = end
            piece = self.board[start_x-1][start_y-1]
            self.board[end_x-1][end_y-1] = piece
            self.board[start_x-1][start_y-1] = "empty"
            self.current_player = "black" if self.current_player == "white" else "white"
        else:
            print("Invalid move!")

    def play_game(self):
        while True:
            self.print_board()
            start = input("Enter start position (e.g. 1a): ")
            end = input("Enter end position (e.g. 2b): ")
            start_x = int(start[0])
            start_y = ord(start[1]) - 96
            end_x = int(end[0])
            end_y = ord(end[1]) - 96
            self.make_move((start_x, start_y), (end_x, end_y))

game = ChessGame()
game.play_game()