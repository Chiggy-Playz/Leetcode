# https://leetcode.com/problems/different-ways-to-add-parentheses/description/?envType=daily-question&envId=2024-09-19
# Different Ways to Add Parentheses

def diffWaysToCompute(expression: str) -> list[int]:

    stack = []

    current = ""
    for char in expression:
        if char not in "+-*":
            current += char
        else:
            stack.append(current)
            stack.append(char)
            current = ""
    stack.append(current)

    def r(stk: list[str]) -> list[str]:
        result = []
        for i in range(len(stk)):
            if stk[i] not in "+-*":
                continue

            # We have found an operator
            new_stk = stk[:i-1] + ["(" +  "".join(stk[i-1:i+2]) + ")"] + stk[i+2:]
            if len(new_stk) == 1:
                result.append(new_stk[0])
                break
            result.extend(r(new_stk))
        return result

    return list(map(eval, set(r(stack)))) or [eval(expression)]

print(diffWaysToCompute("0"))
