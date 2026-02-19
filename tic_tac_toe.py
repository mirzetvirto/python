"""
Tic Tac Toe Game
A simple implementation of the classic Tic Tac Toe game with AI opponent.
"""

class TicTacToe:
    """Main Tic Tac Toe game class."""
    
    def __init__(self):
        """Initialize the game board and state."""
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
        self.current_player = self.human
    
    def print_board(self):
        """Display the current game board."""
        print("\n")
        for i in range(3):
            print(f" {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ")
            if i < 2:
                print("-----------")
        print("\n")
    
    def print_positions(self):
        """Display available positions for reference."""
        print("Position numbers:")
        for i in range(3):
            print(f" {i*3} | {i*3+1} | {i*3+2} ")
            if i < 2:
                print("-----------")
        print()
    
    def is_winner(self, player):
        """Check if the given player has won."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[i] == player for i in condition) 
                   for condition in win_conditions)
    
    def is_board_full(self):
        """Check if the board is full."""
        return ' ' not in self.board
    
    def get_available_moves(self):
        """Return list of available move positions."""
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def minimax(self, depth, is_maximizing):
        """
        Minimax algorithm to determine the best AI move.
        
        Args:
            depth: Current depth in the game tree
            is_maximizing: True if AI's turn, False if human's turn
        
        Returns:
            Score of the position
        """
        if self.is_winner(self.ai):
            return 10 - depth
        if self.is_winner(self.human):
            return depth - 10
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            max_score = float('-inf')
            for move in self.get_available_moves():
                self.board[move] = self.ai
                score = self.minimax(depth + 1, False)
                self.board[move] = ' '
                max_score = max(score, max_score)
            return max_score
        else:
            min_score = float('inf')
            for move in self.get_available_moves():
                self.board[move] = self.human
                score = self.minimax(depth + 1, True)
                self.board[move] = ' '
                min_score = min(score, min_score)
            return min_score
    
    def get_best_move(self):
        """Determine the best move for the AI using minimax."""
        best_score = float('-inf')
        best_move = None
        
        for move in self.get_available_moves():
            self.board[move] = self.ai
            score = self.minimax(0, False)
            self.board[move] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def make_move(self, position):
        """Make a move at the given position.""" 
        if position < 0 or position > 8 or self.board[position] != ' ':
            return False
        
        self.board[position] = self.current_player
        return True
    
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = self.ai if self.current_player == self.human else self.human
    
    def play(self):
        """Main game loop."""
        print("=" * 40)
        print("Welcome to Tic Tac Toe!")
        print("=" * 40)
        print("You are X, AI is O")
        
        self.print_positions()
        
        while True:
            self.print_board()
            
            if self.current_player == self.human:
                while True:
                    try:
                        position = int(input("Enter your move (0-8): "))
                        if self.make_move(position):
                            break
                        else:
                            print("Invalid move! Position already taken or out of range.")
                    except ValueError:
                        print("Please enter a valid number between 0 and 8.")
            else:
                position = self.get_best_move()
                print(f"AI plays at position {position}")
                self.make_move(position)
            
            if self.is_winner(self.current_player):
                self.print_board()
                if self.current_player == self.human:
                    print("🎉 You won! Congratulations!")
                else:
                    print("AI wins! Better luck next time.")
                break
            
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break
            
            self.switch_player()
        
        print("=" * 40)


def main():
    """Entry point for the game."""
    while True:
        game = TicTacToe()
        game.play()
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()