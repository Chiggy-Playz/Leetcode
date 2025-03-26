# https://leetcode.com/problems/generate-parentheses


def bruteforce(n: int) -> list[str]:
    if n == 0:
        return []
    if n == 1:
        return ["()"]

    result = []

    for i in range(n - 1, 0, -1):
        normal = ["(" + sub + ")" for sub in bruteforce(i)]
        postfix = bruteforce(n - 1 - i)
        if postfix:
            for post in postfix:
                result.extend([n + post for n in normal])
        else:
            result.extend(normal)
        result.extend(["()" + sub for sub in bruteforce(n - 1)])

    return list(set(result))


def dp(n: int) -> list[str]:

    result = []

    def backtrack(current, open, close):
        if (open + close) == 2 * n:
            result.append(current)
            return
        
        if open < n:
            backtrack(current + "(", open + 1, close)
        
        if close < open:
            backtrack(current + ")", open, close + 1)


    backtrack("", 0, 0)
    return result


print(bruteforce(3))
print(dp(3))
