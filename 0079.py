from common import null, TreeNode, ListNode, DoubleListNode
from utils import time_it, test

def exist(board: list[list[str]], word: str) -> bool:

    m = len(board)  # rows
    n = len(board[0])  # cols

    def search(word: str, y: int, x: int, previous: list[tuple[int, int]]):
        if word == "":
            return True
        
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dy, dx = (y + dir[1], x + dir[0])

            if (dy,dx) in previous:
                continue

            if not ((0 <= dy < m) and (0 <= dx < n)):
                continue

            if board[dy][dx] == word[0]:
                if search(word[1:], dy, dx, previous.copy() + [(y, x)]):
                    return True
        
        return False


    # First we find the starting character
    for row, line in enumerate(board):
        for col, char in enumerate(line):
            if char == word[0]:
                if search(word[1:], row, col, [(row, col)]):
                    return True

    return False

test(
    True,
    None,
    exist,
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    "" \
    "ABCCED",
)

test(
    False,
    None,
    exist,
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    "ABCB",
)

test(
    True,
    None,
    exist,
    [["C","A","A"],["A","A","A"],["B","C","D"]],
    "AAB"
)

test(
    False,
    None,
    exist,
    [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],
    "aaaaaaaaaaaaa",
)