from utils import test


def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    r = 1
    maxSubstring = 0
    while r < len(s):
        if s[r] in s[l:r]:
            maxSubstring = max(maxSubstring, len(s[l:r]))
            l += 1 + s[l:r].index(s[r])
        r += 1

    return max(maxSubstring, len(s[l:r]))


test(3, lengthOfLongestSubstring, "abcabcbb")
test(1, lengthOfLongestSubstring, "bbbbb")
test(3, lengthOfLongestSubstring, "pwwkew")
test(3, lengthOfLongestSubstring, "ohomm")
test(10, lengthOfLongestSubstring, "abcdefcghijkl")
test(3, lengthOfLongestSubstring, "dvdf")
