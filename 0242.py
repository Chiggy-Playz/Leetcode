# https://leetcode.com/problems/valid-anagram/
# Valid Anagram

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
