from common import DoubleListNode, ListNode, TreeNode
from utils import test, time_it


def myAtoi(s: str) -> int:
    s2 = ""
    for char in s:
        if (char == " "):
            if s2:
                break
            else:
                continue


        if (char in "+-") and (not s2):
            s2 += char
            continue

        if char.isdigit():
            s2 += char
        else:
            break

    if len(s2) == 1 and not s2[0].isdigit():
        s2 = ""

    num = int(s2 or "0")
    minimum = -(2**31)
    maximum = -minimum - 1
    if num < minimum:
        num = minimum
    if num > maximum:
        num = maximum

    return num



test(42, None, myAtoi, "42")
test(-42, None, myAtoi, "   -042")