#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(N):
    """
    Solve the N Queens problem
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    
    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def print_solution(board):
        """
        Print the N Queens solution
        """
        solution = [[i, board[i]] for i in range(N)]
        print(solution)

    def solve(board, col):
        """
        Recursive function to solve N Queens
        """
        if col == N:
            print_solution(board)
            return
        for row in range(N):
            if is_safe(board, row, col, N):
                board[col] = row
                solve(board, col + 1)

    board = [-1] * N  # Initialize the board with -1 values
    solve(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)
    
    N = sys.argv[1]
    solve_nqueens(N)

