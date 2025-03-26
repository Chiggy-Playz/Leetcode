# https://leetcode.com/problems/house-robber/description/


def rob(nums: list[int]) -> int:

    def dp(houses: list[int]) -> int:

        if not houses:
            return 0

        if len(houses) == 1:
            return houses[0]

        choose = houses[0] + dp(houses[2:])
        nochoose = dp(houses[1:])
        return max([choose, nochoose])

    return dp(nums)


print(rob([8, 9, 8]))
