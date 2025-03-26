# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evalRPN(tokens: list[str]) -> int:
    stack = []
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(y / x),
    }
    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            # Token is op
            stack.append((ops[token])(stack.pop(), stack.pop()))

    return stack.pop()

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))