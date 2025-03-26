from utils import test


def search(nums: list[int], k: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == k:
            return mid
        # k is greated than middle
        elif nums[mid] < k:
            # Check if k is in the right half
            # Or check if origin is in this half
            if k <= nums[r] or nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            # check if k is in the left half
            if nums[l] <= k or nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1


# 4 5 6 7 0 1 2
# 0 1 2 4 5 6 7
# 6 7 0 1 2 4 5

# 7 8 0 1 2 3 4 5 6

# print(search([4,5,6,7,0,1,2], 0))
# print(search([4,5,6,7,8,1,2,3], 8))

test(4, search, [4, 5, 6, 7, 0, 1, 2], 0)
test(4, search, [4, 5, 6, 7, 8, 1, 2, 3], 8)
test(-1, search, [4, 5, 6, 7, 0, 1, 2], 3)
print("Done")
