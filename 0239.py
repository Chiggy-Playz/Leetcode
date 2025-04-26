import heapq
from typing import List
from common import null, TreeNode, ListNode, DoubleListNode
from utils import time_it, test

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    
    result = []
    i = 0
    k = k-1

    # Make a max heap
    heap = [(num*-1, i) for i, num in enumerate(nums[i:k+1])]
    heapq.heapify(heap)

    while k < len(nums):
        result.append(-heap[0][0])

        i += 1
        k += 1

        while heap and heap[0][1] < i:
            heapq.heappop(heap)
        
        if k < len(nums):
            heapq.heappush(heap, (-nums[k],k))

    return result


print(maxSlidingWindow(
    [1],
    1
))

# [3,3,5,5,6,7]
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7