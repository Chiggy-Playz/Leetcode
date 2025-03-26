# https://leetcode.com/problems/valid-palindrome/description/
# 0125. Valid Palindrome

def isPalindrome(s: str) -> bool:

    alphanumeric_str = ""
    for char in s:
        if char.isalnum():
            alphanumeric_str += char.lower()

    i = 0
    j = len(alphanumeric_str) - 1

    while i < j:
        if alphanumeric_str[i] != alphanumeric_str[j]:
            return False
        i += 1
        j -= 1
    return True


def palindromeButCooler(s: str) -> bool:

    l, r = 0, len(s) - 1

    while l < r:
        if not s[l].lower().isalnum():
            l += 1
        elif not s[r].lower().isalnum():
            r += 1
        elif s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
