from common import DoubleListNode, ListNode, TreeNode, null
from utils import test, time_it

from functools import cache


def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:

    result = float("inf")
    path = []

    @cache
    def diff(w1, w2):
        c = 0
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                c += 1
        return c

    def bfs(w):
        nonlocal result

        if w == endWord:
            result = min(result, len(path))
            return

        new = []
        for word in wordList:
            if diff(word, w) == 1 and word not in path:
                new.append(word)

        for nword in new:
            path.append(nword)
            bfs(nword)
            path.pop()

    bfs(beginWord)
    return int(result) + 1


print(ladderLength("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
