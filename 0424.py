from utils import test


# def characterReplacement(s: str, k: int) -> int:
#     l = 0
#     r = 0
#     res = 0
#     counts = {}

#     while r < len(s):
#         counts[s[r]] = counts.get(s[r], 0) + 1
#         # Get max from values
#         max_value = max(counts.values())
#         viable = ((r - l) - max_value + 1) <= k
#         print(f"{l=}, {r=}, {s[l:r+1]=}, {s[r]=}, {counts=}, {max_value=}, {viable=}")
#         if viable:
#             r += 1
#             res = max(res, len(s[l:r]))
#         else:
#             counts[s[l]] -= 1
#             counts[s[r]] -= 1
#             l += 1

#     return res

def characterReplacement(s: str, k: int) -> int:
    l = 0
    r = 0
    result = 0
    chars = {}
    while r < len(s):
        chars[s[r]] = chars.get(s[r], 0) + 1
        if ((r-l+1) - max(chars.values()) <= k):
            result = max(result, r-l+1)
            r += 1
        else:
            chars[s[l]] -= 1
            chars[s[r]] -= 1
            l += 1
    
    return result


test(1, characterReplacement, "ABAB", 0)
test(4, characterReplacement, "ABAB", 2)
test(4, characterReplacement, "ABBB", 2)
