# https://leetcode.com/problems/group-anagrams/description/
# Group Anagram


# Mine. m*n*log(n) time complexity
def groupAnagramsOld(strs: list[str]) -> list[list[str]]:
    words = {}

    for index, word in enumerate(map(lambda v: str(sorted(v)), strs)):
        if word in words:
            words[word].append(strs[index])
        else:
            words[word] = [strs[index]]
    return list(words.values())

# Alternate way. m*n time complexity
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    words = {}

    for str in strs:
        chars = [0] * 26  # a-z
        for c in str:
            chars[ord(c) - ord("a")] += 1
        key = tuple(chars)
        if key in words:
            words[key].append(str)
        else:
            words[key] = [str]

    return list(words.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
