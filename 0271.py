# https://leetcode.com/problems/encode-and-decode-strings/description/
# Encode Decode Strings


class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for str in strs:
            res += f"{len(str)}.{str}"
        return res

    def decode(self, s: str) -> list[str]:

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != ".":
                j += 1

            length = int(s[i:j])
            i = j + length + 1
            res.append(s[j + 1 : i])

        return res


s = Solution()

for i in ([""], [], ["this", "is", "a", "try"]):
    assert s.decode(s.encode(i)) == i
