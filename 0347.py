# https://leetcode.com/problems/top-k-frequent-elements/description/
# Top k frequent elements

from collections import defaultdict


def topKFrequent(nums: list[int], k: int) -> list[int]:
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1

    return list(map(lambda k: k[0], sorted(counts.items(), key=lambda k: k[1], reverse=True)))[:k]


def better(nums: list[int], k: int) -> list[int]:

    counts: list[set[int]] = [set() for _ in range(len(nums) + 1)]
    freq = defaultdict(int)

    for num in nums:
        if num in counts[freq[num]]:
            counts[freq[num]].remove(num)
        freq[num] += 1
        counts[freq[num]].add(num)

    result = []
    val = None
    while k > 0:
        if not val:
            val = counts.pop() or None
            continue
        result.append(val.pop())
        k -= 1
    return result


def neet(nums: list[int], k: int) -> list[int]:

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return []

print(
    "[1,1,1,2,2,3] = ",
    topKFrequent([1, 1, 1, 2, 2, 3], 2),
    better([1, 1, 1, 2, 2, 3], 2),
)

print(
    "[1] = ",
    topKFrequent([1], 1),
    better([1], 1),
)
