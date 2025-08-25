from common import *
from utils import equal_lists_unordered, test, time_it

def numIslands(grid: list[list[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    uf = UnionFind(m*n)

    for y in range(m):
        for x in range(n):
            if grid[y][x] != "1":
                continue

            for dx, dy in [(1,0), (0, -1)]:
                nx, ny = x+dx, y+dy
                if (0 <= nx < n) and (0 <= ny < m) and grid[ny][nx] == "1":                  
                    uf.merge(y * n + x, ny * n + nx)

    islands = set()
    for y in range(m):
        for x in range(n):
            if grid[y][x] == "1":
                islands.add(uf.find(y * n + x))
    return len(islands)

test(
    1,
    None,
    numIslands,
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
)

test(
    3,
    None,
    numIslands,
    [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],
)


test(
    1,
    None,
    numIslands,
    [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]],
)