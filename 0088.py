# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
# Merge Sorted Array

def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    i = 0
    j = 0
    inserted = 0

    while j < n:
        while nums2[j] >= nums1[i]:
            if i == (m + inserted):
                break
            i += 1
        nums1.insert(i, nums2[j])
        nums1.pop()
        inserted += 1
        i += 1
        j += 1


print(
    merge(
        [0, 0, 0, 0, 0],
        0,
        [1, 2, 3, 4, 5],
        5,
    )
)
