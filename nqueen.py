def solveNQueens(n):
    def is_valid(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        # Check left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i] == j:
                return False
        # Check right diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i] == j:
                return False
        return True

    def backtrack(row, board):
        if row == n:
            results.append(["." * col + "Q" + "." * (n - col - 1) for col in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    results = []
    board = [-1] * n  # Track column positions for each row
    backtrack(0, board)
    return results

# Example usage:
n = 4
solutions = solveNQueens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()