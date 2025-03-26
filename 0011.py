# https://leetcode.com/problems/container-with-most-water/description/
# 11. Container With Most Water


def maxArea(height: list[int]) -> int:

    max_area = 0
    l = 0
    r = len(height) - 1

    while l < r:
        area = abs(r-l) * (min(height[l], height[r]))
        max_area = max(max_area, area)
        if height[l] > height[r]:
            r -=1
        else:
            l += 1

    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
